from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile


def load_runner():
    path = Path(__file__).resolve().parents[1] / "skills" / "codex-fsq-case-runner" / "scripts" / "codex_android_harness_runner.py"
    spec = importlib.util.spec_from_file_location("codex_android_harness_runner", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_long_press_target_is_detected():
    runner = load_runner()

    gesture = runner.gesture_for_target("I perform a long press gesture on address bar")

    assert gesture == {"type": "long_press", "target": "address bar"}


def test_rect_center_uses_element_bounds():
    runner = load_runner()

    assert runner.rect_center({"x": 10, "y": 20, "width": 100, "height": 40}) == (60, 40)


def test_selectors_prefer_explicit_locator():
    runner = load_runner()

    selectors = runner.selectors_from_targeting({
        "target": "the camera search icon on omnibox",
        "locator": {"resourceId": "com.microsoft.emmx:id/attachment_right_camera_button"},
    })

    assert selectors[0] == {"resourceId": "com.microsoft.emmx:id/attachment_right_camera_button"}


class FakeTransport:
    def get_element_text(self, element_id):
        assert element_id == "element-1"
        return "https://www.chinatravel.com"

    def get_element_attribute(self, element_id, name):
        if name == "enabled":
            return "false"
        return None


class FakeSession:
    transport = FakeTransport()

    def _find_element(self, selector):
        if selector == {"resourceId": "com.microsoft.emmx:id/url_bar"}:
            return "element-1"
        return None

    def screenshot(self, path):
        Path(path).write_bytes(b"fake-png")
        return path

    def dump_hierarchy(self):
        return '<node text="Bing Search Microsoft" />'


def test_assert_element_text_contains_uses_locator():
    runner = load_runner()

    result = runner.assert_element_text(FakeSession(), {
        "element": {"resourceId": "com.microsoft.emmx:id/url_bar"},
        "text": {"contains": "chinatravel.com"},
    })

    assert result["ok"] is True
    assert result["matched"]["kind"] == "elementTextContains"


def test_assert_element_enabled_state_uses_locator():
    runner = load_runner()

    result = runner.assert_element(FakeSession(), {
        "element": {
            "resourceId": "com.microsoft.emmx:id/url_bar",
            "enabled": False,
        },
    })

    assert result["ok"] is True
    assert result["matched"] == {"kind": "elementState", "enabled": False}


def test_visual_assertion_saves_screenshot_and_report():
    runner = load_runner()

    with tempfile.TemporaryDirectory() as tmp:
        result = runner.visual_assertion(
            FakeSession(),
            Path(tmp),
            7,
            "Analyze the screenshot to verify bing webpage displayed normally",
        )

        assert result["ok"] is True
        assert Path(result["screenshot"]).exists()
        assert Path(result["report"]).exists()
        assert result["usedForCoordinates"] is False


def test_execute_long_press_on_uses_explicit_locator():
    runner = load_runner()

    class Transport(FakeTransport):
        def get_element_rect(self, element_id):
            assert element_id == "element-1"
            return {"x": 10, "y": 20, "width": 100, "height": 40}

    class Session(FakeSession):
        transport = Transport()

        def __init__(self):
            self.long_pressed = None

        def long_press(self, x, y, duration=1.0):
            self.long_pressed = (x, y, duration)

    session = Session()

    result = runner.execute_command(
        session,
        lambda *args, **kwargs: {"ok": False},
        "com.microsoft.emmx",
        {"longPressOn": {"target": "Address bar", "locator": {"resourceId": "com.microsoft.emmx:id/url_bar"}}},
    )

    assert result["ok"] is True
    assert session.long_pressed == (60, 40, 1.0)
