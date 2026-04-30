# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/core_address_bar/core_address_bar.feature`
- Feature: `Core Address Bar`
- Scenario: `Select website URL in dropdown list to navigate directly to site`
- Tags: `@navigation, @smoke, @p0`

## Output

- Output YAML: `fsq-testcases/windows/core_address_bar/select_website_url_in_dropdown_list_to_navigate_directly_to_site.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I input "www.apple.com" in address bar` | `tapOn` | Converted from matched step implementation. |
| `Then a dropdown list should appear with URL suggestions` | `assertVisible` | Converted from matched step implementation. |
| `When I click the top item "www.apple.com" in the dropdown list` | `tapOn` | Converted from matched step implementation. |
| `Then I should navigate to "Apple" page successfully` | `assertVisible` | Converted from matched step implementation. |
| `And the address bar should display the complete URL "https://www.apple.com"` | `assert` | Converted from matched step implementation. |
| `And the "Apple" page should load completely` | `assertVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I input "www.apple.com" in address bar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/common.py:79` | operations=enter_text |
| `Then a dropdown list should appear with URL suggestions` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/core_address_bar/core_address_bar.py:22` | operations=verify_element_exists; locator={"name": "Suggestions"} |
| `When I click the top item "www.apple.com" in the dropdown list` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/core_address_bar/core_address_bar.py:38` | operations=element_click; locator={"name": "www.apple.com"} |
| `Then I should navigate to "Apple" page successfully` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/core_address_bar/core_address_bar.py:87` | operations=verify_element_exists; locator={"name": "Apple"} |
| `And the address bar should display the complete URL "https://www.apple.com"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/core_address_bar/core_address_bar.py:104` | operations=verify_element_value; locator={"name": "https://www.apple.com"} |
| `And the "Apple" page should load completely` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/core_address_bar/core_address_bar.py:124` | operations=verify_element_exists; locator={"name": "Apple"} |

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
