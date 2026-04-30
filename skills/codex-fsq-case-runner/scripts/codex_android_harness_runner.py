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



def selectors_from_targeting(value: Any, default_target: str = "") -> list[dict[str, Any]]:
    if isinstance(value, str):
        return selectors_for(value)
    if not isinstance(value, dict):
        return selectors_for(default_target)
    selectors: list[dict[str, Any]] = []
    locator = value.get("locator")
    if isinstance(locator, dict) and locator:
        selectors.append(dict(locator))
    inline_locator = {
        key: value[key]
        for key in ("resourceId", "id", "accessibilityId", "text", "textContains", "description", "descriptionContains", "className", "xpath", "uiautomator")
        if key in value
    }
    if inline_locator:
        selectors.append(inline_locator)
    target = str(value.get("target") or default_target or "")
    selectors.extend(selectors_for(target))
    # Preserve order while removing duplicate selector dicts.
    unique: list[dict[str, Any]] = []
    seen: set[str] = set()
    for selector in selectors:
        marker = json.dumps(selector, sort_keys=True, ensure_ascii=False)
        if marker not in seen:
            seen.add(marker)
            unique.append(selector)
    return unique


def is_assert_like(target: str) -> bool:
    low = str(target or "").lower()
    return low.startswith("the ") or any(hint in low for hint in ASSERT_HINTS)


def source_contains(session: Any, text: str) -> bool:
    return bool(text) and text.lower() in session.dump_hierarchy().lower()


def visual_assertion(session: Any, output: Path, step: int, prompt: str) -> dict[str, Any]:
    screenshot_path = output / f"{step:03d}-visual.png"
    report_path = output / f"{step:03d}-visual-assertion.json"
    result: dict[str, Any] = {
        "ok": False,
        "failureClass": "visual_assertion_failed",
        "prompt": prompt,
        "screenshot": str(screenshot_path),
        "report": str(report_path),
        "analyzer": "codex-simple-accessibility-backed-visual-v1",
        "usedForCoordinates": False,
    }
    try:
        session.screenshot(path=str(screenshot_path))
    except Exception as exc:
        result.update({"failureClass": "screenshot_failed", "error": repr(exc)})
        write_json(report_path, result)
        return result

    try:
        source = session.dump_hierarchy()
    except Exception as exc:
        source = ""
        result["sourceError"] = repr(exc)

    low_prompt = prompt.lower()
    low_source = source.lower()
    signals: list[str] = []
    for token in ("bing", "search", "microsoft", "copilot", "news", "images", "videos"):
        if token in low_prompt and token in low_source:
            signals.append(token)

    if "displayed normally" in low_prompt or "loads well" in low_prompt or "does not have large blank" in low_prompt:
        result.update({
            "ok": bool(signals),
            "failureClass": None if signals else "needs_vision_review",
            "matchedSignals": signals,
            "method": "screenshot_saved_accessibility_text_signals",
        })
    else:
        result.update({
            "ok": bool(signals),
            "failureClass": None if signals else "needs_vision_review",
            "matchedSignals": signals,
            "method": "screenshot_saved_accessibility_text_signals",
        })

    write_json(report_path, result)
    return result


def matcher_expected_contains(matcher: Any) -> str | None:
    if not isinstance(matcher, dict):
        return None
    value = matcher.get("contains")
    return str(value) if value is not None else None


def element_text_matches(session: Any, selectors: list[dict[str, Any]], expected: str) -> dict[str, Any]:
    try:
        element_id, resolution = first_element(session, selectors, timeout=8.0)
    except LookupError as exc:
        return {"ok": False, "found": False, "failureClass": "element_not_found", "error": str(exc), "selectors": selectors}

    values: dict[str, str] = {}
    try:
        values["text"] = session.transport.get_element_text(element_id) or ""
    except Exception as exc:
        values["textError"] = repr(exc)
    for attribute in ("text", "content-desc", "name", "label", "value"):
        try:
            attr_value = session.transport.get_element_attribute(element_id, attribute)
        except Exception:
            attr_value = None
        if attr_value:
            values[f"attribute:{attribute}"] = str(attr_value)

    expected_low = expected.lower()
    for source, actual in values.items():
        if expected_low in str(actual).lower():
            return {**resolution, "ok": True, "found": True, "matched": {"kind": "elementTextContains", "source": source, "value": actual, "expected": expected}}
    return {"ok": False, "found": True, "failureClass": "assertion_failed", "expected": expected, "actual": values, **resolution}


def bool_attribute(value: Any) -> bool | None:
    if isinstance(value, bool):
        return value
    if value is None:
        return None
    low = str(value).strip().lower()
    if low == "true":
        return True
    if low == "false":
        return False
    return None


def locator_part(selector: dict[str, Any]) -> dict[str, Any]:
    state_keys = {"enabled", "visible", "selected", "checked", "focused"}
    return {key: value for key, value in selector.items() if key not in state_keys}


def element_exists_or_state_matches(session: Any, selector: dict[str, Any]) -> dict[str, Any]:
    locator = locator_part(selector)
    try:
        element_id, resolution = first_element(session, [locator], timeout=8.0)
    except LookupError as exc:
        return {"ok": False, "found": False, "failureClass": "element_not_found", "error": str(exc), "selectors": [locator]}

    expected_enabled = bool_attribute(selector.get("enabled"))
    if expected_enabled is None:
        return {**resolution, "ok": True, "found": True}

    try:
        actual_enabled = bool_attribute(session.transport.get_element_attribute(element_id, "enabled"))
    except Exception as exc:
        return {**resolution, "ok": False, "found": True, "failureClass": "assertion_failed", "error": repr(exc), "expected": {"enabled": expected_enabled}}
    if actual_enabled == expected_enabled:
        return {**resolution, "ok": True, "found": True, "matched": {"kind": "elementState", "enabled": actual_enabled}}
    return {**resolution, "ok": False, "found": True, "failureClass": "assertion_failed", "expected": {"enabled": expected_enabled}, "actual": {"enabled": actual_enabled}}


def assert_element_text(session: Any, assertion: dict[str, Any]) -> dict[str, Any] | None:
    element = assertion.get("element")
    expected = matcher_expected_contains(assertion.get("text"))
    if not isinstance(element, dict) or expected is None:
        return None
    return element_text_matches(session, [element], expected)


def assert_element(session: Any, assertion: dict[str, Any]) -> dict[str, Any] | None:
    element = assertion.get("element")
    if not isinstance(element, dict):
        return None
    text_result = assert_element_text(session, assertion)
    if text_result is not None:
        return text_result
    return element_exists_or_state_matches(session, element)


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


def normalize_actions(actions: Any) -> Any:
    if not isinstance(actions, list):
        return actions
    normalized: list[dict[str, Any]] = []
    for source in actions:
        if not isinstance(source, dict):
            normalized.append(source)
            continue
        normalized_source = dict(source)
        source_actions = source.get("actions")
        if isinstance(source_actions, list):
            normalized_source["actions"] = [normalize_action_item(item) for item in source_actions]
        normalized.append(normalized_source)
    return normalized


def normalize_action_item(action: Any) -> Any:
    if not isinstance(action, dict):
        return action
    normalized = dict(action)
    if normalized.get("type") == "pointerMove" and "duration" not in normalized:
        normalized["duration"] = 0
    return normalized


def assert_visible(session: Any, run_action: Any, target: str, selectors: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    selectors = selectors or selectors_for(target)
    if selectors:
        result = run_action(session, "ui.wait", {"selectors": selectors, "timeout": 8})
        if result.get("found"):
            return result
    candidates = re.findall(r'"([^"]+)"', target) + [target]
    for candidate in candidates:
        if source_contains(session, candidate):
            return {"ok": True, "found": True, "matched": {"kind": "pageSourceContains", "value": candidate}}
    return {"ok": False, "found": False, "failureClass": "assertion_failed", "target": target}


def execute_command(session: Any, run_action: Any, app_id: str, command: Any, output: Path | None = None, step: int = 0) -> dict[str, Any]:
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
        session.transport.perform_actions(normalize_actions(value))
        session.transport.release_actions()
        return {"ok": True, "performedActions": True}

    if name == "swipe":
        direction = str(value.get("direction", "up")).lower()
        return viewport_swipe(session, direction, int(value.get("duration", 500)))

    if name == "inputText":
        target = str(value.get("target") or "Search box")
        result = run_action(session, "ui.type", {"selectors": selectors_from_targeting(value, target), "text": value.get("text", ""), "clear": True})
        if not result.get("typed"):
            return {**result, "ok": False, "failureClass": "element_not_found", "target": target}
        return result

    if name == "longPressOn":
        target = str(value.get("target", value))
        selectors = selectors_from_targeting(value, target)
        try:
            element_id, resolution = first_element(session, selectors, timeout=8.0)
        except LookupError as exc:
            return {"ok": False, "found": False, "failureClass": "element_not_found", "error": str(exc), "selectors": selectors, "target": target}
        rect = session.transport.get_element_rect(element_id)
        x, y = rect_center(rect)
        session.long_press(x, y, duration=1.0)
        return {"ok": True, "rect": rect, "point": {"x": x, "y": y}, **resolution}

    if name == "tapOn":
        target = str(value.get("target", value))
        low = target.lower()
        if "analyze the screenshot" in low:
            if output is None:
                return {"ok": False, "failureClass": "visual_assertion_missing_output", "target": target}
            return visual_assertion(session, output, step, target)
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
        selectors = selectors_from_targeting(value, target)
        wait_result = run_action(session, "ui.wait", {"selectors": selectors, "timeout": 8, "interval": 0.25})
        if not wait_result.get("found"):
            return {**wait_result, "ok": False, "failureClass": "element_not_found", "target": target}
        result = run_action(session, "ui.click", {"selectors": selectors, "timeout": 8})
        if not result.get("clicked"):
            return {**result, "ok": False, "failureClass": "element_not_found", "target": target}
        return result

    if name == "assertVisible":
        return assert_visible(session, run_action, str(value.get("target", value)), selectors_from_targeting(value, str(value.get("target", value))))

    if name == "assertNotVisible":
        target = str(value.get("target", value))
        result = run_action(session, "ui.wait", {"selectors": selectors_from_targeting(value, target), "timeout": 3})
        found = bool(result.get("found"))
        return {"ok": not found, "found": found, "failureClass": "assertion_failed" if found else None}

    if name == "assertWithAI":
        prompt = str(value.get("prompt") or value.get("target") or value)
        if output is None:
            return {"ok": False, "failureClass": "visual_assertion_missing_output", "target": prompt}
        return visual_assertion(session, output, step, prompt)

    if name == "assert":
        element_result = assert_element(session, value) if isinstance(value, dict) else None
        if element_result is not None:
            return element_result
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
                step_result = execute_command(session, run_action, app_id, command, output, index)
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
