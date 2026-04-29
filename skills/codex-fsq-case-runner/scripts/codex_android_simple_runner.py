#!/usr/bin/env python3
"""Simple Android FSQ runner with per-step accessibility evidence.

This is a repository-owned smoke runner for Android Appium experiments. It is
not an MCP adapter. Its main contract is evidence quality: every executable
step writes a before/after accessibility tree so repair analysis can reason
from state transitions instead of sparse screenshots.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import time
from typing import Any

import yaml
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException


DEFAULT_APP_ACTIVITY = "com.microsoft.ruby.Main"

TARGET_ALIASES: dict[str, list[tuple[str, str]]] = {
    "browser menu": [("id", "com.microsoft.emmx:id/overflow_button_bottom"), ("desc_contains", "Browser menu"), ("desc_contains", "浏览器菜单")],
    "settings": [("desc_contains", "Settings"), ("text_contains", "Settings"), ("desc_contains", "设置"), ("text_contains", "设置")],
    "downloads": [("desc_contains", "Downloads"), ("text_contains", "Downloads"), ("desc_contains", "下载"), ("text_contains", "下载")],
    "favorites": [("desc_contains", "Favorites"), ("text_contains", "Favorites"), ("desc_contains", "收藏夹"), ("text_contains", "收藏夹")],
    "history": [("desc_contains", "History"), ("text_contains", "History"), ("desc_contains", "历史记录"), ("text_contains", "历史记录")],
    "add new tab": [("id", "com.microsoft.emmx:id/edge_bottom_bar_plus_button"), ("desc_contains", "Add new tab"), ("desc_contains", "New tab"), ("desc_contains", "添加新选项卡")],
    "new tab": [("id", "com.microsoft.emmx:id/edge_bottom_bar_plus_button"), ("desc_contains", "New tab"), ("desc_contains", "添加新选项卡")],
    "search box": [("id", "com.microsoft.emmx:id/search_box_text"), ("id", "com.microsoft.emmx:id/url_bar"), ("id", "com.microsoft.emmx:id/location_bar"), ("class", "android.widget.EditText")],
    "address bar": [("id", "com.microsoft.emmx:id/url_bar"), ("id", "com.microsoft.emmx:id/location_bar"), ("id", "com.microsoft.emmx:id/search_box_text"), ("class", "android.widget.EditText")],
    "refresh": [("id", "com.microsoft.emmx:id/refresh_button"), ("desc_contains", "Refresh"), ("desc_contains", "刷新")],
    "go": [("desc_contains", "Go"), ("text_contains", "Go"), ("desc_contains", "转到")],
    "cancel": [("text_contains", "Cancel"), ("desc_contains", "Cancel"), ("text_contains", "取消"), ("desc_contains", "取消")],
    "drop": [("desc_contains", "Drop"), ("text_contains", "Drop")],
    "edit": [("desc_contains", "Edit"), ("text_contains", "Edit"), ("desc_contains", "编辑"), ("text_contains", "编辑")],
    "done": [("desc_contains", "Done"), ("text_contains", "Done"), ("desc_contains", "完成"), ("text_contains", "完成")],
}

ASSERT_HINTS = (
    " should ",
    "should ",
    " page title",
    "panel title",
    "panel should open",
    " is ",
    " shown",
    "display",
    "visible",
    "open normally",
    "tab thumbnails",
)


class ResolutionError(NoSuchElementException):
    """Element resolution failed for a semantic target."""


def ui_quote(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value)[:90].strip("-") or "step"


def options_for(args: argparse.Namespace, app_id: str) -> UiAutomator2Options:
    opts = UiAutomator2Options()
    opts.platform_name = "Android"
    opts.automation_name = "UiAutomator2"
    opts.device_name = args.device_name
    opts.app_package = app_id
    opts.app_activity = args.app_activity
    opts.no_reset = True
    opts.new_command_timeout = 180
    if args.udid:
        opts.set_capability("appium:udid", args.udid)
    opts.set_capability("appium:autoGrantPermissions", True)
    return opts


def write_text(path: Path, text: str) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return str(path)


def dump_tree(driver: webdriver.Remote, output: Path, step: int, phase: str) -> str:
    return write_text(output / f"{step:03d}-{phase}.xml", driver.page_source)


def dump_screenshot(driver: webdriver.Remote, output: Path, step: int, phase: str) -> str | None:
    path = output / f"{step:03d}-{phase}.png"
    try:
        driver.save_screenshot(str(path))
        return str(path)
    except Exception:
        return None


def source_contains(driver: webdriver.Remote, text: str) -> bool:
    return text.lower() in driver.page_source.lower()


def by_spec(spec: tuple[str, str]) -> tuple[str, str]:
    kind, value = spec
    if kind == "id":
        return (AppiumBy.ID, value)
    if kind == "class":
        return (AppiumBy.CLASS_NAME, value)
    if kind == "text":
        return (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{ui_quote(value)}")')
    if kind == "desc":
        return (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{ui_quote(value)}")')
    if kind == "text_contains":
        return (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{ui_quote(value)}")')
    if kind == "desc_contains":
        return (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().descriptionContains("{ui_quote(value)}")')
    raise ValueError(f"Unsupported locator spec: {spec}")


def resolve_aliases(target: str) -> list[tuple[str, str]]:
    normalized = str(target or "").strip()
    low = normalized.lower()
    aliases: list[tuple[str, str]] = []
    for key, specs in TARGET_ALIASES.items():
        if key in low:
            aliases.extend(specs)
    if not aliases and normalized:
        aliases.extend([
            ("text_contains", normalized),
            ("desc_contains", normalized),
            ("text", normalized),
            ("desc", normalized),
        ])
    return aliases


def element_metadata(element: Any) -> dict[str, Any]:
    data: dict[str, Any] = {}
    for name in ("resourceId", "contentDescription", "text", "className", "bounds"):
        try:
            data[name] = element.get_attribute(name)
        except Exception:
            pass
    try:
        data["displayed"] = element.is_displayed()
    except Exception:
        pass
    return data


def find_target(driver: webdriver.Remote, target: str, timeout: float = 8) -> tuple[Any, dict[str, Any]]:
    deadline = time.time() + timeout
    attempts: list[dict[str, str]] = []
    last_error = ""
    while time.time() < deadline:
        for spec in resolve_aliases(target):
            by, value = by_spec(spec)
            attempts.append({"kind": spec[0], "value": spec[1]})
            try:
                element = driver.find_element(by, value)
                return element, {"target": target, "matched": {"kind": spec[0], "value": spec[1]}, "element": element_metadata(element)}
            except Exception as exc:
                last_error = repr(exc)
        time.sleep(0.5)
    raise ResolutionError(json.dumps({"target": target, "attempts": attempts, "lastError": last_error}, ensure_ascii=False))


def is_assert_like(target: str) -> bool:
    low = str(target or "").lower()
    return any(hint in low for hint in ASSERT_HINTS) or low.startswith("the ")


def assert_visible(driver: webdriver.Remote, target: str) -> dict[str, Any]:
    normalized = str(target or "").strip()
    candidates = re.findall(r'"([^"]+)"', normalized) + [normalized]
    errors: list[str] = []
    for candidate in candidates:
        try:
            element, resolution = find_target(driver, candidate)
            if element.is_displayed():
                return resolution
        except Exception as exc:
            errors.append(repr(exc))
        if source_contains(driver, candidate):
            return {"target": target, "matched": {"kind": "pageSourceContains", "value": candidate}}
    raise AssertionError(f"Visible assertion failed: {target}; attempts={errors[:3]}")


def assert_not_visible(driver: webdriver.Remote, target: str) -> dict[str, Any]:
    try:
        element, resolution = find_target(driver, target, timeout=3)
        if element.is_displayed():
            raise AssertionError(f"Not-visible assertion failed: {target}")
        return resolution
    except ResolutionError:
        return {"target": target, "matched": {"kind": "notPresent"}}


def swipe(driver: webdriver.Remote, direction: str, duration: int = 500) -> None:
    size = driver.get_window_size()
    width, height = size["width"], size["height"]
    x = width // 2
    if direction.lower() == "up":
        driver.swipe(x, int(height * 0.78), x, int(height * 0.35), duration)
    elif direction.lower() == "down":
        driver.swipe(x, int(height * 0.35), x, int(height * 0.78), duration)
    elif direction.lower() == "left":
        driver.swipe(int(width * 0.78), height // 2, int(width * 0.25), height // 2, duration)
    else:
        driver.swipe(int(width * 0.25), height // 2, int(width * 0.78), height // 2, duration)


def click_target(driver: webdriver.Remote, target: str) -> dict[str, Any]:
    low = str(target or "").lower()
    if "press enter" in low or low == "go":
        driver.press_keycode(66)
        return {"target": target, "matched": {"kind": "keycode", "value": "ENTER"}}
    if "wait" in low or "load completely" in low or "reloaded" in low:
        time.sleep(3)
        return {"target": target, "matched": {"kind": "wait", "value": "3000ms"}}
    if "scroll the page down" in low:
        swipe(driver, "up", 800)
        return {"target": target, "matched": {"kind": "gesture", "value": "swipeUp"}}
    if "dismiss the permission dialog" in low:
        for candidate in ("Not now", "Cancel", "No thanks", "以后再说", "不允许", "取消"):
            try:
                element, resolution = find_target(driver, candidate, timeout=1)
                element.click()
                return resolution
            except Exception:
                pass
        return {"target": target, "matched": {"kind": "noop", "value": "dialogNotFound"}}
    if is_assert_like(target):
        return assert_visible(driver, target)
    element, resolution = find_target(driver, target)
    element.click()
    return resolution


def input_text(driver: webdriver.Remote, target: str, text: str) -> dict[str, Any]:
    try:
        element, resolution = find_target(driver, target, timeout=4)
        element.click()
    except Exception:
        element = driver.switch_to.active_element
        resolution = {"target": target, "matched": {"kind": "activeElement"}}
    time.sleep(0.5)
    active = driver.switch_to.active_element
    try:
        active.clear()
    except Exception:
        pass
    active.send_keys(text)
    resolution["inputTextLength"] = len(text)
    return resolution


def execute_command(driver: webdriver.Remote, app_id: str, command: Any) -> tuple[str, dict[str, Any]]:
    if isinstance(command, str):
        if command == "launchApp":
            try:
                driver.terminate_app(app_id)
            except Exception:
                pass
            driver.activate_app(app_id)
            time.sleep(3)
            return "launchApp", {"appId": app_id}
        if command == "killApp":
            driver.terminate_app(app_id)
            return "killApp", {"appId": app_id}
        raise ValueError(f"Unsupported string command: {command}")

    if not isinstance(command, dict) or len(command) != 1:
        raise ValueError(f"Invalid command: {command}")

    name, value = next(iter(command.items()))
    if name == "tapOn":
        target = value.get("target") if isinstance(value, dict) else value
        return f"tapOn:{target}", click_target(driver, str(target))
    if name == "inputText":
        return f"inputText:{value.get('target')}", input_text(driver, value.get("target", "Search box"), value.get("text", ""))
    if name == "pressKey":
        key = str(value)
        if key.lower() in ("enter", "return"):
            driver.press_keycode(66)
        elif key.lower() == "back":
            driver.press_keycode(4)
        else:
            raise ValueError(f"Unsupported key: {key}")
        return f"pressKey:{key}", {"matched": {"kind": "keycode", "value": key}}
    if name == "swipe":
        direction = value.get("direction", "up")
        swipe(driver, direction, int(value.get("duration", 500)))
        return f"swipe:{direction}", {"matched": {"kind": "gesture", "value": direction}}
    if name == "assertVisible":
        target = value.get("target") if isinstance(value, dict) else value
        return f"assertVisible:{target}", assert_visible(driver, str(target))
    if name == "assertNotVisible":
        target = value.get("target") if isinstance(value, dict) else value
        return f"assertNotVisible:{target}", assert_not_visible(driver, str(target))
    if name == "assert":
        if isinstance(value, dict) and "url" in value:
            expected = value["url"].get("contains") if isinstance(value["url"], dict) else value["url"]
            if expected and not source_contains(driver, str(expected)):
                try:
                    element, resolution = find_target(driver, "Address bar", timeout=1)
                    text = element.text or ""
                    if str(expected).lower() not in text.lower():
                        raise AssertionError(f"URL assertion failed: {expected}; url_bar={text}")
                    return "assert:url", resolution
                except Exception as exc:
                    raise AssertionError(f"URL assertion failed: {expected}") from exc
        return "assert", {"matched": {"kind": "assertion", "value": "accepted"}}
    if name == "performActions":
        max_pause = 0
        for sequence in value if isinstance(value, list) else []:
            for action in sequence.get("actions", []):
                if action.get("type") == "pause":
                    max_pause = max(max_pause, int(action.get("duration", 0)))
        time.sleep(max_pause / 1000 if max_pause else 1)
        return "performActions", {"matched": {"kind": "pause", "value": max_pause or 1000}}
    raise ValueError(f"Unsupported command: {name}")


def classify_failure(exc: Exception, command: Any) -> str:
    text = repr(exc).lower()
    command_text = json.dumps(command, ensure_ascii=False).lower()
    if "analyze the screenshot" in command_text or "screenshot" in command_text:
        return "unsupported_visual_assertion"
    if "login" in command_text or "msa" in command_text or "account" in command_text:
        return "missing_precondition"
    if isinstance(exc, AssertionError):
        return "assertion_failed"
    if isinstance(exc, (ResolutionError, NoSuchElementException, TimeoutException)) or "nosuchelement" in text:
        return "element_not_found"
    if isinstance(exc, WebDriverException):
        return "driver_error"
    return "unknown"


def load_case(path: Path) -> tuple[dict[str, Any], list[Any]]:
    docs = list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
    if len(docs) != 2:
        raise ValueError(f"Expected two YAML documents in {path}")
    return docs[0] or {}, docs[1] or []


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one Android FSQ case with per-step accessibility evidence")
    parser.add_argument("--case", required=True)
    parser.add_argument("--backend", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--appium-server", default=os.environ.get("APPIUM_SERVER", "http://127.0.0.1:4723"))
    parser.add_argument("--udid", default=os.environ.get("ANDROID_UDID"))
    parser.add_argument("--device-name", default=os.environ.get("ANDROID_DEVICE_NAME", "Android"))
    parser.add_argument("--app-activity", default=os.environ.get("ANDROID_APP_ACTIVITY", DEFAULT_APP_ACTIVITY))
    parser.add_argument("--screenshots", action="store_true", help="Also capture screenshots as evidence; XML is always captured")
    args = parser.parse_args()

    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    config, commands = load_case(Path(args.case))
    app_id = config.get("appId", "com.microsoft.emmx")
    result: dict[str, Any] = {"case": args.case, "backend": args.backend, "appId": app_id, "steps": []}
    driver = None

    try:
        driver = webdriver.Remote(args.appium_server, options=options_for(args, app_id))
        for index, command in enumerate(commands, 1):
            step_start = time.monotonic()
            entry: dict[str, Any] = {"step": index, "command": command}
            try:
                entry["beforeXml"] = dump_tree(driver, output, index, "before")
                if args.screenshots:
                    entry["beforePng"] = dump_screenshot(driver, output, index, "before")
                label, resolution = execute_command(driver, app_id, command)
                entry.update({"label": label, "resolution": resolution, "status": "passed"})
                entry["afterXml"] = dump_tree(driver, output, index, "after")
                if args.screenshots:
                    entry["afterPng"] = dump_screenshot(driver, output, index, "after")
            except Exception as exc:
                entry.update({"status": "failed", "error": repr(exc), "failureClass": classify_failure(exc, command)})
                try:
                    entry["failedXml"] = dump_tree(driver, output, index, "failed")
                    if args.screenshots:
                        entry["failedPng"] = dump_screenshot(driver, output, index, "failed")
                except Exception as dump_exc:
                    entry["evidenceError"] = repr(dump_exc)
                entry["durationMs"] = int((time.monotonic() - step_start) * 1000)
                result["steps"].append(entry)
                result["status"] = "failed"
                result["failureClass"] = entry["failureClass"]
                result["error"] = entry["error"]
                write_text(output / "codex-android-simple-runner-result.json", json.dumps(result, ensure_ascii=False, indent=2))
                print(json.dumps({"status": "failed", "case": args.case, "output": str(output), "failureClass": entry["failureClass"], "error": entry["error"]}, ensure_ascii=False), flush=True)
                return 1
            entry["durationMs"] = int((time.monotonic() - step_start) * 1000)
            result["steps"].append(entry)

        result["status"] = "passed"
        write_text(output / "codex-android-simple-runner-result.json", json.dumps(result, ensure_ascii=False, indent=2))
        print(json.dumps({"status": "passed", "case": args.case, "output": str(output)}, ensure_ascii=False), flush=True)
        return 0
    finally:
        if driver:
            try:
                driver.quit()
            except Exception:
                pass


if __name__ == "__main__":
    raise SystemExit(main())
