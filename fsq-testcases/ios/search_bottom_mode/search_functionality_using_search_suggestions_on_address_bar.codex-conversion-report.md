# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/search_bottom_mode.feature`
- Feature: `search`
- Scenario: `Search functionality using search suggestions on address bar`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/ios/search_bottom_mode/search_functionality_using_search_suggestions_on_address_bar.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I click on the search box on NTP page` | `tapOn` | Converted from matched step implementation. |
| `And I input a keyword "apple" in the search box` | `inputText` | Converted from matched step implementation. |
| `And I select the first search suggestion from the Search suggestion list` | `tapOn` | Converted from matched step implementation. |
| `When I dismiss the permission dialog from bing` | `assertVisible, tapOn, assertVisible, tapOn, assertVisible, tapOn` | Converted from matched step implementation. |
| `And I should see search results for "apple"` | `assertVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I click on the search box on NTP page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:11` | operations=click_element; locator={"name": "Search and address bar"} |
| `And I input a keyword "apple" in the search box` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:62` | operations=send_keys; locator={"name": "Address"} |
| `And I select the first search suggestion from the Search suggestion list` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:729` | operations=click_element; locator={"name": "omnibox suggestion 0 7"} |
| `When I dismiss the permission dialog from bing` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:477` | operations=verify_element_exists, click_element, verify_element_exists, click_element, verify_element_exists, click_element, Accept; locator={"name": "Allow While Using App"} |
| `And I should see search results for "apple"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:581` | operations=verify_element_exists; locator={"xpath": "//*[contains(@label, 'Apple')]"} |

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
