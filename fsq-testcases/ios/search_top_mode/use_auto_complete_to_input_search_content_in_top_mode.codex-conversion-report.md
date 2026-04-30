# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/search_top_mode.feature`
- Feature: `search_top_mode`
- Scenario: `Use auto complete to input search content in top mode`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/ios/search_top_mode/use_auto_complete_to_input_search_content_in_top_mode.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I click on the top address bar on NTP page` | `tapOn` | Converted from matched step implementation. |
| `And I input a keyword "apple" in the search box` | `inputText` | Converted from matched step implementation. |
| `And I click "Go" on keyboard` | `tapOn` | Converted from matched step implementation. |
| `When I dismiss the permission dialog from bing` | `assertVisible, tapOn, assertVisible, tapOn, assertVisible, tapOn` | Converted from matched step implementation. |
| `When I click + button on the bottom toolbar` | `tapOn` | Converted from matched step implementation. |
| `When I click on the top address bar on NTP page` | `tapOn` | Converted from matched step implementation. |
| `And I type "appl" in the search box` | `inputText` | Converted from matched step implementation. |
| `Then I should see "apple" shown in search box` | `assert` | Converted from matched step implementation. |
| `And I click "Go" on keyboard` | `tapOn` | Converted from matched step implementation. |
| `And analyze the screenshot to verify the search result is apple related` | `assertWithAI, assertVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I click on the top address bar on NTP page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_top_mode.py:48` | operations=click_element; locator={"name": "NTPHomeFakeOmniboxAccessibilityID"} |
| `And I input a keyword "apple" in the search box` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:62` | operations=send_keys; locator={"name": "Address"} |
| `And I click "Go" on keyboard` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:433` | operations=click_element; locator={"name": "Go"} |
| `When I dismiss the permission dialog from bing` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:477` | operations=verify_element_exists, click_element, verify_element_exists, click_element, verify_element_exists, click_element, Accept; locator={"name": "Allow While Using App"} |
| `When I click + button on the bottom toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:396` | operations=click_element; locator={"accessibilityId": "kToolbarEdgeNewTabButtonIdentifier"} |
| `When I click on the top address bar on NTP page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_top_mode.py:48` | operations=click_element; locator={"name": "NTPHomeFakeOmniboxAccessibilityID"} |
| `And I type "appl" in the search box` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_top_mode.py:62` | operations=send_keys; locator={"name": "Address"} |
| `Then I should see "apple" shown in search box` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:565` | operations=verify_element_attribute; locator={"accessibilityId": "Address"} |
| `And I click "Go" on keyboard` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:433` | operations=click_element; locator={"name": "Go"} |
| `And analyze the screenshot to verify the search result is apple related` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_top_mode.py:74` | operations=verify_visual_task, verify_element_exists; locator={"xpath": "//*[contains(@label, 'Apple') or contains(@value, 'apple')]"} |

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
