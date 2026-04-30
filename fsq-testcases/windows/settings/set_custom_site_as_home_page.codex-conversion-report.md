# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/settings/settings.feature`
- Feature: `Settings`
- Scenario: `Set custom site as home page`
- Tags: `@settings, @smoke, @p0`

## Output

- Output YAML: `fsq-testcases/windows/settings/set_custom_site_as_home_page.codex.yaml`
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
| `When I turn on the option "show home button on the toolbar"` | `tapOn` | Converted from matched step implementation. |
| `And I select the option "Set custom site"` | `tapOn` | Converted from matched step implementation. |
| `Then the input box under "Set custom site" can be clicked` | `assertVisible` | Converted from matched step implementation. |
| `When I input "https://www.apple.com" to the input box` | `tapOn` | Converted from matched step implementation. |
| `And I select the option "Set custom site"` | `tapOn` | Converted from matched step implementation. |
| `And I click "Home" button to the left of the address bar` | `tapOn` | Converted from matched step implementation. |
| `Then should open "https://www.apple.com" site` | `assert` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I click "Settings and more" button on toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:10` | operations=element_click; locator={"name": "Settings and more"} |
| `And I select "Settings" button from the dropdown menu` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:27` | operations=select_item; locator={"name": "Settings"} |
| `Then the settings page should be opened` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:44` | operations=verify_element_exists; locator={"name": "Settings"} |
| `And I click "Start, home, and new tab page"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:196` | operations=select_item; locator={"name": "Start, home, and new tab page"} |
| `When I turn on the option "show home button on the toolbar"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:275` | operations=element_click; locator={"name": "Show home button on the toolbar"} |
| `And I select the option "Set custom site"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:292` | operations=select_item; locator={"name": "Set custom site"} |
| `Then the input box under "Set custom site" can be clicked` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:309` | operations=verify_element_exists; locator={"name": "￼"} |
| `When I input "https://www.apple.com" to the input box` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:330` | operations=enter_text; locator={"name": "control"} |
| `And I select the option "Set custom site"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:292` | operations=select_item; locator={"name": "Set custom site"} |
| `And I click "Home" button to the left of the address bar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:348` | operations=element_click; locator={"name": "Home"} |
| `Then should open "https://www.apple.com" site` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:365` | operations=verify_element_value; locator={"name": "https://www.apple.com"} |

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
