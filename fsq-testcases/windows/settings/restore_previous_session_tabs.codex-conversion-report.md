# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/settings/settings.feature`
- Feature: `Settings`
- Scenario: `Restore previous session tabs`
- Tags: `@settings, @smoke, @p0`

## Output

- Output YAML: `fsq-testcases/windows/settings/restore_previous_session_tabs.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I click "Settings and more" button on toolbar` | `tapOn` | Converted from matched step implementation. |
| `And I select "Settings" button from the dropdown menu` | `tapOn` | Converted from matched step implementation. |
| `Then the settings page should be opened` | `assertVisible` | Converted from matched step implementation. |
| `And I click "Start, home, and new tab page"` | `tapOn` | Converted from matched step implementation. |
| `When I select the option "Open tabs from the previous session"` | `tapOn` | Converted from matched step implementation. |
| `Then the option "Open tabs from the previous session" should be selected successfully` | `assertVisible` | Converted from matched step implementation. |
| `When I open a new tab` | `tapOn` | Converted from matched step implementation. |
| `And I navigate to "https://www.bbc.com"` | `tapOn` | Converted from matched step implementation. |
| `And I open a new tab` | `tapOn` | Converted from matched step implementation. |
| `And I navigate to "https://www.apple.com"` | `tapOn` | Converted from matched step implementation. |
| `And I close and restart Edge` | `tapOn` | Converted from matched step implementation. |
| `Then previously "https://www.bbc.com" and "https://www.apple.com" tabs should be opened` | `assertVisible, assertVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I click "Settings and more" button on toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:10` | operations=element_click; locator={"name": "Settings and more"} |
| `And I select "Settings" button from the dropdown menu` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:27` | operations=select_item; locator={"name": "Settings"} |
| `Then the settings page should be opened` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:44` | operations=verify_element_exists; locator={"name": "Settings"} |
| `And I click "Start, home, and new tab page"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:196` | operations=select_item; locator={"name": "Start, home, and new tab page"} |
| `When I select the option "Open tabs from the previous session"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:213` | operations=element_click; locator={"name": "Open tabs from the previous session"} |
| `Then the option "Open tabs from the previous session" should be selected successfully` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:230` | operations=verify_checkbox_state; locator={"name": "Open tabs from the previous session"} |
| `When I open a new tab` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/common.py:63` | operations=element_click; locator={"name": "New Tab"} |
| `And I navigate to "https://www.bbc.com"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/common.py:48` | operations=native_navigate |
| `And I open a new tab` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/common.py:63` | operations=element_click; locator={"name": "New Tab"} |
| `And I navigate to "https://www.apple.com"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/common.py:48` | operations=native_navigate |
| `And I close and restart Edge` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:248` | operations=select_item, app_launch; locator={"name": "Close"} |
| `Then previously "https://www.bbc.com" and "https://www.apple.com" tabs should be opened` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:510` | operations=verify_element_exists, verify_element_exists; locator={"name": "BBC Home"} |

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
