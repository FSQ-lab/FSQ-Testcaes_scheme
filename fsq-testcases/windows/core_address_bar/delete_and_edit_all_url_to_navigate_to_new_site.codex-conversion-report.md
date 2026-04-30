# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/core_address_bar/core_address_bar.feature`
- Feature: `Core Address Bar`
- Scenario: `Delete and edit all URL to navigate to new site`
- Tags: `@navigation, @regression, @p0`

## Output

- Output YAML: `fsq-testcases/windows/core_address_bar/delete_and_edit_all_url_to_navigate_to_new_site.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given I navigate to "https://www.apple.com"` | `tapOn` | Converted from matched step implementation. |
| `And the address bar should display the complete URL "https://www.apple.com"` | `assert` | Converted from matched step implementation. |
| `When I select all text in address bar` | `tapOn, pressKey` | Converted from matched step implementation. |
| `And I press the "Backspace" key` | `pressKey` | Converted from matched step implementation. |
| `And I input "www.bbc.com" in address bar` | `tapOn` | Converted from matched step implementation. |
| `And I press the "Enter" key` | `pressKey` | Converted from matched step implementation. |
| `Then I should navigate to "BBC" page successfully` | `assertVisible` | Converted from matched step implementation. |
| `And the address bar should display the complete URL "https://www.bbc.com"` | `assert` | Converted from matched step implementation. |
| `And the "BBC" page should load completely` | `assertVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `Given I navigate to "https://www.apple.com"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/common.py:48` | operations=native_navigate |
| `And the address bar should display the complete URL "https://www.apple.com"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/core_address_bar/core_address_bar.py:104` | operations=verify_element_value; locator={"name": "https://www.apple.com"} |
| `When I select all text in address bar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/core_address_bar/core_address_bar.py:272` | operations=element_click, send_keystrokes |
| `And I press the "Backspace" key` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/core_address_bar/core_address_bar.py:205` | operations=send_keystrokes |
| `And I input "www.bbc.com" in address bar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/common.py:79` | operations=enter_text |
| `And I press the "Enter" key` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/core_address_bar/core_address_bar.py:9` | operations=send_keystrokes |
| `Then I should navigate to "BBC" page successfully` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/core_address_bar/core_address_bar.py:218` | operations=verify_element_exists; locator={"name": "BBC Home"} |
| `And the address bar should display the complete URL "https://www.bbc.com"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/core_address_bar/core_address_bar.py:235` | operations=verify_element_value; locator={"name": "https://www.bbc.com"} |
| `And the "BBC" page should load completely` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/core_address_bar/core_address_bar.py:255` | operations=verify_element_exists; locator={"name": "BBC Home"} |

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
