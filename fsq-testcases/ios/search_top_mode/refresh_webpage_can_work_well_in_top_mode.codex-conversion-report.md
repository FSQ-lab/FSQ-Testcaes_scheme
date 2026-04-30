# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/search_top_mode.feature`
- Feature: `search_top_mode`
- Scenario: `Refresh webpage can work well in top mode`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/ios/search_top_mode/refresh_webpage_can_work_well_in_top_mode.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I click on the search box on NTP page` | `tapOn` | Converted from matched step implementation. |
| `When I input a keyword "microsoft" in the search box` | `inputText` | Converted from matched step implementation. |
| `When I dismiss the permission dialog from bing` | `assertVisible, tapOn, assertVisible, tapOn, assertVisible, tapOn` | Converted from matched step implementation. |
| `And I click "Go" on keyboard` | `tapOn` | Converted from matched step implementation. |
| `When I perform a long press gesture on address bar` | `tapOn` | Converted from matched step implementation. |
| `Then I click on "Move address bar to top" option` | `tapOn` | Converted from matched step implementation. |
| `And I see the refresh button shown on omnibox` | `assertVisible` | Converted from matched step implementation. |
| `When I click on the refresh button` | `tapOn` | Converted from matched step implementation. |
| `Then analyze the screenshot to verify the web page does not have large blank spaces, and the content loads well` | `assertWithAI` | Converted from matched step implementation. |
| `And I scroll the page down for 2 seconds` | `performActions` | Converted from matched step implementation. |
| `Then analyze the screenshot to verify the web page does not have large blank spaces, and the content loads well` | `assertWithAI` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I click on the search box on NTP page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:11` | operations=click_element; locator={"name": "Search and address bar"} |
| `When I input a keyword "microsoft" in the search box` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:69` | operations=send_keys; locator={"name": "Address"} |
| `When I dismiss the permission dialog from bing` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:477` | operations=verify_element_exists, click_element, verify_element_exists, click_element, verify_element_exists, click_element, Accept; locator={"name": "Allow While Using App"} |
| `And I click "Go" on keyboard` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:433` | operations=click_element; locator={"name": "Go"} |
| `When I perform a long press gesture on address bar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/default_bottom_omnibox.py:309` | operations=long_press_element; locator={"name": "Search and address bar"} |
| `Then I click on "Move address bar to top" option` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/default_bottom_omnibox.py:322` | operations=click_element; locator={"name": "Move address bar to top"} |
| `And I see the refresh button shown on omnibox` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_top_mode.py:9` | operations=verify_element_exists; locator={"name": "kEdgeOmniboxReloadButtonIdentifier"} |
| `When I click on the refresh button` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_top_mode.py:22` | operations=click_element; locator={"name": "kEdgeOmniboxReloadButtonIdentifier"} |
| `Then analyze the screenshot to verify the web page does not have large blank spaces, and the content loads well` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_top_mode.py:35` | operations=verify_visual_task |
| `And I scroll the page down for 2 seconds` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:146` | operations=swipe |
| `Then analyze the screenshot to verify the web page does not have large blank spaces, and the content loads well` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_top_mode.py:35` | operations=verify_visual_task |

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
