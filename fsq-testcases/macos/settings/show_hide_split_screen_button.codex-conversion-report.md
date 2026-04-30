# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/settings/settings.feature`
- Feature: `Settings functionality`
- Scenario: `Show/hide Split screen button`
- Tags: `@regression, @p0, @settings`

## Output

- Output YAML: `fsq-testcases/macos/settings/show_hide_split_screen_button.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `tapOn` | Converted from matched step implementation. |
| `And I input "edge://settings/appearance/toolbar" to the address bar` | `tapOn, inputText, pressKey` | Converted from matched step implementation. |
| `When I click on "Split screen" button switch in Toolbar Settings page` | `tapOn` | Converted from matched step implementation. |
| `Then the Split screen button should be visible on the toolbar` | `assertVisible` | Converted from matched step implementation. |
| `When I click on "Split screen" button switch in Toolbar Settings page` | `tapOn` | Converted from matched step implementation. |
| `Then the Split screen button should be hidden on the toolbar` | `assertNotVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `Given Edge is launched` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/common/common.py:154` | operations=semantic/no direct tool call detected |
| `And I input "edge://settings/appearance/toolbar" to the address bar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:376` | operations=click_element, send_keys, press_key; locator={"xpath": "//XCUIElementTypeTextField[@label=\"Address and search bar\"]"} |
| `When I click on "Split screen" button switch in Toolbar Settings page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:912` | operations=find_element, click_element; locator={"xpath": "//XCUIElementTypeSwitch[@label='Split screen']"} |
| `Then the Split screen button should be visible on the toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:950` | operations=verify_element_exists; locator={"xpath": "//XCUIElementTypeButton[@label='Split screen']"} |
| `When I click on "Split screen" button switch in Toolbar Settings page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:912` | operations=find_element, click_element; locator={"xpath": "//XCUIElementTypeSwitch[@label='Split screen']"} |
| `Then the Split screen button should be hidden on the toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:971` | operations=verify_element_not_exists; locator={"xpath": "//XCUIElementTypeButton[@label='Split screen']"} |

## Unresolved Or Low-Confidence Items

- None

## Conversion Rules Applied

- Applied Codex dual-source conversion: feature scenario for intent/order and Behave step implementation for executable operations.
- Preserved source locators from Appium/pywinauto step definitions where available.
- Preserved URL/current-page checks as locator-backed element assertions when source code verifies UI state.
- Converted screenshot/visual checks to blocking `assertWithAI` assertions instead of coordinate fallback.
- Every case starts with `launchApp` and ends with `killApp` for isolated runs.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm app identity and runner backend match the target execution environment.
- Confirm semantic targets remain specific enough for accessibility-tree locator resolution.
- Confirm any unresolved source steps before using this case for gating.
- Confirm visual assertions are run with a vision-capable analysis path.
