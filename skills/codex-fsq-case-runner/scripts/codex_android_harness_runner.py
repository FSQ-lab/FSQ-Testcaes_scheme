#!/usr/bin/env python3
"""Run one Android FSQ case through Android_Harness AppiumSession.

Codex-produced runner for Android_Harness experiments. It keeps the evidence
contract from the simple runner, but uses the team harness' AppiumSession and
action registry. Gestures that need coordinates must derive them from an
accessibility element rect, never from screenshot guessing.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys
import time
import traceback
from typing import Any

import yaml

DEFAULT_HARNESS_PATH = "/Users/qunmi/Documents/github/Android_Harness"
DEFAULT_APP_ID = "com.microsoft.emmx"

ASSERT_HINTS = (
    " should ",
    "should ",
    " page title",
    "panel title",
    "panel should open",
    " shown",
    "display",
    "visible",
    "open normally",
    "thumbnails",
    "with ",
    " count ",
)

ALIASES: dict[str, list[dict[str, Any]]] = {
    "browser menu": [{"resourceId": "com.microsoft.emmx:id/overflow_button_bottom"}, {"descriptionContains": "Browser menu"}, {"descriptionContains": "More options"}],
    "settings": [{"text": "Settings"}, {"descriptionContains": "Settings"}, {"textContains": "Settings"}],
    "downloads": [{"text": "Downloads"}, {"descriptionContains": "Downloads"}, {"textContains": "Downloads"}],
    "favorites": [{"text": "Favorites"}, {"descriptionContains": "Favorites"}, {"textContains": "Favorites"}],
    "history": [{"text": "History"}, {"descriptionContains": "History"}, {"textContains": "History"}],
    "add new tab": [{"resourceId": "com.microsoft.emmx:id/edge_bottom_bar_plus_button"}, {"descriptionContains": "Add new tab"}, {"descriptionContains": "New tab"}],
    "search box": [{"resourceId": "com.microsoft.emmx:id/search_box_text"}, {"resourceId": "com.microsoft.emmx:id/url_bar"}, {"resourceId": "com.microsoft.emmx:id/location_bar"}, {"className": "android.widget.EditText"}, {"descriptionContains": "Search"}, {"textContains": "Search"}],
    "address bar": [{"resourceId": "com.microsoft.emmx:id/url_bar"}, {"resourceId": "com.microsoft.emmx:id/location_bar"}, {"resourceId": "com.microsoft.emmx:id/search_box_text"}, {"className": "android.widget.EditText"}, {"descriptionContains": "Search"}, {"textContains": "Search"}],
    "go": [{"descriptionContains": "Go"}, {"text": "Go"}, {"textContains": "Go"}],
    "refresh": [{"resourceId": "com.microsoft.emmx:id/refresh_button"}, {"descriptionContains": "Refresh"}, {"textContains": "Refresh"}],
    "search engine": [{"text": "Search engine"}, {"textContains": "Search engine"}, {"descriptionContains": "Search engine"}],
    "search section": [{"text": "Search"}, {"textContains": "Search"}, {"descriptionContains": "Search"}],
    "google": [{"text": "Google"}, {"textContains": "Google"}, {"descriptionContains": "Google"}],
    "bing": [{"text": "Bing"}, {"textContains": "Bing"}, {"descriptionContains": "Bing"}],
    "move address bar to top": [{"textContains": "Move address bar to top"}, {"textContains": "Top"}, {"descriptionContains": "top"}],
    "move address bar to bottom": [{"textContains": "Move address bar to bottom"}, {"textContains": "Bottom"}, {"descriptionContains": "bottom"}],
}


def load_harness(harness_path: str):
    if harness_path not in sys.path:
        sys.path.insert(0, harness_path)
    from appium_harness.actions import run_action
    from appium_harness.session import AppiumSession, Platform

    return AppiumSession, Platform, run_action


def write_text(path: Path, text: str) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return str(path)


def write_json(path: Path, data: Any) -> str:
    return write_text(path, json.dumps(data, ensure_ascii=False, indent=2))


def safe_slug(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-")[:140] or "case"


def command_name(command: Any) -> str:
    if isinstance(command, str):
        return command
    if isinstance(command, dict) and command:
        return next(iter(command.keys()))
    return type(command).__name__


def gesture_for_target(target: str) -> dict[str, str] | None:
    low = str(target or "").lower()
    if "long press" in low and "address bar" in low:
        return {"type": "long_press", "target": "address bar"}
    return None


def rect_center(rect: dict[str, Any]) -> tuple[int, int]:
    return (int(rect["x"]) + int(rect["width"]) // 2, int(rect["y"]) + int(rect["height"]) // 2)


def selectors_for(target: str) -> list[dict[str, Any]]:
    raw = str(target or "").strip()
    low = raw.lower()
    selectors: list[dict[str, Any]] = []

    for quoted in re.findall(r'"([^"]+)"', raw):
        selectors.extend([{ "text": quoted }, { "textContains": quoted }, { "descriptionContains": quoted }])

    if "select" in low and "google" in low:
        return ALIASES["google"]
    if "select" in low and "bing" in low:
        return ALIASES["bing"]

    for key, values in ALIASES.items():
        if key in low:
            selectors.extend(values)
    if selectors:
        return selectors

    if raw:
        return [{"text": raw}, {"textContains": raw}, {"descriptionContains": raw}]
    return []


def is_assert_like(target: str) -> bool:
    low = str(target or "").lower()
    return low.startswith("the ") or any(hint in low for hint in ASSERT_HINTS)


def source_contains(session: Any, text: str) -> bool:
    return bool(text) and text.lower() in session.dump_hierarchy().lower()


def dump_tree(session: Any, output: Path, step: int, phase: str) -> str | None:
    try:
        return write_text(output / f"{step:03d}-{phase}.xml", session.dump_hierarchy())
    except Exception as exc:
        write_json(output / f"{step:03d}-{phase}.error.json", {"error": repr(exc)})
        return None


def first_element(session: Any, selectors: list[dict[str, Any]], timeout: float = 8.0) -> tuple[str, dict[str, Any]]:
    deadline = time.monotonic() + timeout
    attempts: list[dict[str, Any]] = []
    while time.monotonic() < deadline:
        for selector in selectors:
            attempts.append(selector)
            element_id = session._find_element(selector)
            if element_id:
                return element_id, {"matched": selector, "attempts": attempts[-8:]}
        time.sleep(0.35)
    raise LookupError(json.dumps({"attempts": attempts[-20:]}, ensure_ascii=False))


def long_press_target(session: Any, target: str) -> dict[str, Any]:
    gesture = gesture_for_target(target)
    if not gesture:
        raise LookupError(f"Unsupported gesture target: {target}")
    selectors = selectors_for(gesture["target"])
    element_id, resolution = first_element(session, selectors, timeout=8.0)
    rect = session.transport.get_element_rect(element_id)
    x, y = rect_center(rect)
    session.long_press(x, y, duration=1.0)
    return {"ok": True, "gesture": gesture, "rect": rect, "point": {"x": x, "y": y}, **resolution}


def viewport_swipe(session: Any, direction: str, duration_ms: int = 500) -> dict[str, Any]:
    info = session.info()
    width = int(info.get("screenWidth") or 1080)
    height = int(info.get("screenHeight") or 1920)
    if direction == "up":
        start, end = [width / 2, height * 0.78], [width / 2, height * 0.35]
    elif direction == "down":
        start, end = [width / 2, height * 0.35], [width / 2, height * 0.78]
    elif direction == "left":
        start, end = [width * 0.82, height * 0.65], [width * 0.20, height * 0.65]
    else:
        start, end = [width * 0.20, height * 0.65], [width * 0.82, height * 0.65]
    session.swipe((start[0], start[1]), (end[0], end[1]), duration=duration_ms / 1000.0)
    return {"ok": True, "gesture": "swipe", "direction": direction, "start": start, "end": end}


def assert_visible(session: Any, run_action: Any, target: str) -> dict[str, Any]:
    selectors = selectors_for(target)
    if selectors:
        result = run_action(session, "ui.wait", {"selectors": selectors, "timeout": 8})
        if result.get("found"):
            return result
    candidates = re.findall(r'"([^"]+)"', target) + [target]
    for candidate in candidates:
        if source_contains(session, candidate):
            return {"ok": True, "found": True, "matched": {"kind": "pageSourceContains", "value": candidate}}
    return {"ok": False, "found": False, "failureClass": "assertion_failed", "target": target}


def execute_command(session: Any, run_action: Any, app_id: str, command: Any) -> dict[str, Any]:
    if isinstance(command, str):
        if command == "launchApp":
            return run_action(session, "app.start", {"package": app_id, "stop": True, "wait": 2})
        if command == "killApp":
            return run_action(session, "app.stop", {"package": app_id})
        return {"ok": False, "failureClass": "unsupported_command", "error": f"Unsupported string command: {command}"}

    if not isinstance(command, dict) or len(command) != 1:
        return {"ok": False, "failureClass": "unsupported_command", "error": f"Invalid command: {command!r}"}

    name, value = next(iter(command.items()))
    value = value or {}

    if name == "pressKey":
        key = str(value).lower()
        return run_action(session, "device.press", {"key": {"return": "enter"}.get(key, key)})

    if name == "performActions":
        total_pause = 0
        only_pause = True
        for source in value if isinstance(value, list) else []:
            for action in source.get("actions", []):
                if action.get("type") == "pause":
                    total_pause += int(action.get("duration", 0))
                else:
                    only_pause = False
        if only_pause:
            time.sleep(min(total_pause / 1000.0, 10.0))
            return {"ok": True, "waitedMs": total_pause}
        session.transport.perform_actions(value)
        session.transport.release_actions()
        return {"ok": True, "performedActions": True}

    if name == "swipe":
        direction = str(value.get("direction", "up")).lower()
        return viewport_swipe(session, direction, int(value.get("duration", 500)))

    if name == "inputText":
        target = str(value.get("target") or "Search box")
        result = run_action(session, "ui.type", {"selectors": selectors_for(target), "text": value.get("text", ""), "clear": True})
        if not result.get("typed"):
            return {**result, "ok": False, "failureClass": "element_not_found", "target": target}
        return result

    if name == "tapOn":
        target = str(value.get("target", value))
        low = target.lower()
        if "analyze the screenshot" in low:
            return {"ok": False, "failureClass": "unsupported_non_vision_assertion", "target": target}
        gesture = gesture_for_target(target)
        if gesture:
            return long_press_target(session, target)
        if "press enter" in low or low == "go":
            return run_action(session, "device.press", {"key": "enter"})
        if "wait" in low or "load completely" in low or "reloaded" in low:
            time.sleep(3)
            return {"ok": True, "waitedMs": 3000}
        if "scroll the page down" in low:
            return viewport_swipe(session, "up", 800)
        if "swipe within" in low or "right to left" in low:
            return viewport_swipe(session, "left", 500)
        if is_assert_like(target):
            return assert_visible(session, run_action, target)
        result = run_action(session, "ui.click", {"selectors": selectors_for(target), "timeout": 8})
        if not result.get("clicked"):
            return {**result, "ok": False, "failureClass": "element_not_found", "target": target}
        return result

    if name == "assertVisible":
        return assert_visible(session, run_action, str(value.get("target", value)))

    if name == "assertNotVisible":
        target = str(value.get("target", value))
        result = run_action(session, "ui.wait", {"selectors": selectors_for(target), "timeout": 3})
        found = bool(result.get("found"))
        return {"ok": not found, "found": found, "failureClass": "assertion_failed" if found else None}

    if name == "assert":
        url = value.get("url") if isinstance(value, dict) else None
        expected = url.get("contains") if isinstance(url, dict) else None
        if expected and source_contains(session, str(expected)):
            return {"ok": True, "matched": {"kind": "pageSourceContains", "value": expected}}
        return {"ok": False, "failureClass": "unsupported_native_url_assertion", "target": value}

    return {"ok": False, "failureClass": "unsupported_command", "error": f"Unsupported command: {name}"}


def load_case(path: Path) -> tuple[dict[str, Any], list[Any]]:
    docs = list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
    if len(docs) != 2:
        raise ValueError(f"Expected two YAML documents in {path}")
    return docs[0] or {}, docs[1] or []


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one Android FSQ case with Android_Harness direct AppiumSession")
    parser.add_argument("--case", required=True)
    parser.add_argument("--backend", default="appium-harness")
    parser.add_argument("--output", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--harness-path", default=os.environ.get("ANDROID_HARNESS_PATH", DEFAULT_HARNESS_PATH))
    parser.add_argument("--appium-server", default=os.environ.get("APPIUM_SERVER", "http://127.0.0.1:4723"))
    parser.add_argument("--udid", default=os.environ.get("ANDROID_UDID") or os.environ.get("ANDROID_SERIAL") or "145e66aa")
    args = parser.parse_args()

    AppiumSession, Platform, run_action = load_harness(args.harness_path)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    config, commands = load_case(Path(args.case))
    app_id = config.get("appId", DEFAULT_APP_ID)
    result: dict[str, Any] = {"case": args.case, "backend": args.backend, "appId": app_id, "steps": []}
    session = None

    try:
        session = AppiumSession(serial=args.udid, platform=Platform.ANDROID, appium_url=args.appium_server, package=app_id)
        for index, command in enumerate(commands, 1):
            step_start = time.monotonic()
            entry: dict[str, Any] = {"step": index, "command": command, "label": command_name(command)}
            entry["beforeXml"] = dump_tree(session, output, index, "before")
            try:
                step_result = execute_command(session, run_action, app_id, command)
            except Exception as exc:
                step_result = {"ok": False, "failureClass": "execution_error", "error": repr(exc), "traceback": traceback.format_exc()[-4000:]}
            entry["afterXml"] = dump_tree(session, output, index, "after")
            entry["result"] = step_result
            entry["status"] = "passed" if step_result.get("ok") else "failed"
            entry["durationMs"] = int((time.monotonic() - step_start) * 1000)
            result["steps"].append(entry)
            if entry["status"] == "failed":
                entry["failedXml"] = dump_tree(session, output, index, "failed")
                result.update({"status": "failed", "failureClass": step_result.get("failureClass"), "error": step_result.get("error"), "failedStep": index})
                write_json(output / "codex-android-harness-runner-result.json", result)
                print(json.dumps({"status": "failed", "case": args.case, "output": str(output), "failedStep": index, "failureClass": result.get("failureClass"), "error": result.get("error")}, ensure_ascii=False), flush=True)
                return 1

        result["status"] = "passed"
        write_json(output / "codex-android-harness-runner-result.json", result)
        print(json.dumps({"status": "passed", "case": args.case, "output": str(output)}, ensure_ascii=False), flush=True)
        return 0
    finally:
        if session:
            try:
                run_action(session, "app.stop", {"package": app_id})
            except Exception:
                pass
            try:
                session.close()
            except Exception:
                pass


if __name__ == "__main__":
    raise SystemExit(main())
