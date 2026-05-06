import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "skills" / "codex-fsq-case-runner" / "scripts" / "codex_android_simple_runner.py"
SPEC = importlib.util.spec_from_file_location("codex_android_simple_runner", MODULE_PATH)
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class FakeElement:
    def __init__(self, resource_id, text="", content_description="", on_click=None):
        self.resource_id = resource_id
        self.text = text
        self.content_description = content_description
        self.clicked = False
        self.on_click = on_click
        self.rect = {"x": 10, "y": 20, "width": 100, "height": 40}

    def click(self):
        self.clicked = True
        if self.on_click:
            self.on_click()

    def is_displayed(self):
        return True

    def get_attribute(self, name):
        return {
            "resourceId": self.resource_id,
            "text": self.text,
            "contentDescription": self.content_description,
            "className": "android.widget.Button",
            "bounds": "[0,0][1,1]",
        }.get(name)


class FakeDriver:
    def __init__(self):
        self.calls = []
        self.executed = []
        self.keycodes = []
        self.page_source = "<hierarchy><android.widget.TextView text='Personal info' /></hierarchy>"
        self.close_button = FakeElement("com.microsoft.emmx:id/close_button")
        self.settings_title = FakeElement("", text="Settings")
        self.move_address_bar_item = FakeElement("com.microsoft.emmx:id/menu_item_text", text="Move address bar to the bottom")
        self.url_bar = FakeElement("com.microsoft.emmx:id/url_bar", text="Search or ask anything")
        self.navigate_up = FakeElement("", content_description="Navigate up")

    def find_element(self, by, value):
        self.calls.append((by, value))
        if by == runner.AppiumBy.ID and value == "com.microsoft.emmx:id/close_button":
            return self.close_button
        if by == runner.AppiumBy.ID and value == "com.microsoft.emmx:id/url_bar":
            return self.url_bar
        if by == runner.AppiumBy.ACCESSIBILITY_ID and value == "Navigate up":
            return self.navigate_up
        if "Settings" in value:
            return self.settings_title
        if "Move address bar to the bottom" in value:
            return self.move_address_bar_item
        raise runner.NoSuchElementException(value)

    def execute(self, command, params=None):
        self.executed.append((command, params or {}))
        return {"value": None}

    def press_keycode(self, keycode):
        self.keycodes.append(keycode)


def test_tap_on_prefers_explicit_locator_over_semantic_target_alias():
    driver = FakeDriver()
    command = {
        "tapOn": {
            "target": "Close Settings panel",
            "locator": {"resourceId": "com.microsoft.emmx:id/close_button"},
        }
    }

    label, resolution = runner.execute_command(driver, "com.microsoft.emmx", command)

    assert label == "tapOn:Close Settings panel"
    assert resolution["matched"] == {"kind": "id", "value": "com.microsoft.emmx:id/close_button"}
    assert driver.close_button.clicked is True
    assert driver.calls[0] == (runner.AppiumBy.ID, "com.microsoft.emmx:id/close_button")


def test_tap_on_does_not_fallback_to_semantic_target_when_explicit_locator_is_wrong():
    driver = FakeDriver()
    command = {
        "tapOn": {
            "target": "Close Settings panel",
            "locator": {"resourceId": "com.microsoft.emmx:id/missing_close_button"},
        }
    }

    try:
        runner.execute_command(driver, "com.microsoft.emmx", command)
    except runner.ResolutionError:
        pass
    else:
        raise AssertionError("Expected explicit locator miss to fail without semantic fallback")

    assert driver.settings_title.clicked is False
    assert driver.calls[0] == (runner.AppiumBy.ID, "com.microsoft.emmx:id/missing_close_button")


def test_perform_actions_executes_w3c_actions_and_releases_actions():
    driver = FakeDriver()
    command = {
        "performActions": [
            {
                "type": "pointer",
                "id": "codex-menu-page-swipe",
                "parameters": {"pointerType": "touch"},
                "actions": [
                    {"type": "pointerMove", "origin": "viewport", "x": 800, "y": 1900},
                    {"type": "pointerDown", "button": 0},
                    {"type": "pointerMove", "origin": "viewport", "x": 200, "y": 1900, "duration": 1000},
                    {"type": "pointerUp", "button": 0},
                ],
            }
        ]
    }

    label, resolution = runner.execute_command(driver, "com.microsoft.emmx", command)

    assert label == "performActions"
    assert resolution == {"matched": {"kind": "w3cActions", "value": 1}}
    assert driver.executed[0][0] == runner.Command.W3C_ACTIONS
    assert driver.executed[0][1]["actions"][0]["actions"][0]["duration"] == 0
    assert driver.executed[0][1]["actions"][0]["actions"][2]["duration"] == 1000
    assert driver.executed[1][0] == runner.Command.W3C_CLEAR_ACTIONS


def test_long_press_on_uses_element_center_w3c_actions():
    driver = FakeDriver()
    command = {
        "longPressOn": {
            "target": "Close Settings panel",
            "locator": {"resourceId": "com.microsoft.emmx:id/close_button"},
        }
    }

    label, resolution = runner.execute_command(driver, "com.microsoft.emmx", command)

    actions = driver.executed[0][1]["actions"][0]["actions"]
    assert label == "longPressOn:Close Settings panel"
    assert resolution["matched"] == {"kind": "id", "value": "com.microsoft.emmx:id/close_button"}
    assert resolution["point"] == {"x": 60, "y": 40}
    assert actions == [
        {"type": "pointerMove", "duration": 0, "origin": "viewport", "x": 60, "y": 40},
        {"type": "pointerDown", "button": 0},
        {"type": "pause", "duration": 1000},
        {"type": "pointerUp", "button": 0},
    ]
    assert driver.executed[1][0] == runner.Command.W3C_CLEAR_ACTIONS


def test_tap_on_move_address_bar_to_bottom_accepts_menu_wording_with_the():
    driver = FakeDriver()
    command = {"tapOn": {"target": "Move address bar to bottom"}}

    label, resolution = runner.execute_command(driver, "com.microsoft.emmx", command)

    assert label == "tapOn:Move address bar to bottom"
    assert resolution["matched"] == {"kind": "text_contains", "value": "Move address bar to the bottom"}
    assert driver.move_address_bar_item.clicked is True


def test_ntp_search_box_locator_falls_back_to_url_bar_in_bottom_omnibox_mode():
    driver = FakeDriver()
    command = {
        "tapOn": {
            "target": "Search box on NTP page",
            "locator": {"resourceId": "com.microsoft.emmx:id/search_box_text"},
        }
    }

    label, resolution = runner.execute_command(driver, "com.microsoft.emmx", command)

    assert label == "tapOn:Search box on NTP page"
    assert resolution["matched"] == {"kind": "id", "value": "com.microsoft.emmx:id/url_bar"}
    assert driver.url_bar.clicked is True
    assert driver.calls[0] == (runner.AppiumBy.ID, "com.microsoft.emmx:id/search_box_text")


def test_navigate_up_uses_back_key_when_click_does_not_change_page_source():
    driver = FakeDriver()
    command = {
        "tapOn": {
            "target": "Navigate up",
            "locator": {"accessibilityId": "Navigate up"},
        }
    }

    label, resolution = runner.execute_command(driver, "com.microsoft.emmx", command)

    assert label == "tapOn:Navigate up"
    assert resolution["matched"] == {"kind": "accessibility_id", "value": "Navigate up"}
    assert resolution["repair"] == {"kind": "backKeyAfterUnchangedNavigateUp"}
    assert driver.navigate_up.clicked is True
    assert driver.keycodes == [4]
