# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/tab_center.feature`
- Feature: `tab_center`
- Scenario: `Add new tab by clicking 'add new tab' button in bottom bar`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/ios/tab_center/add_new_tab_by_clicking_add_new_tab_button_in_bottom_bar.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I enter tab center by clicking on the tab center icon` | `tapOn` | Converted from matched step implementation. |
| `And I click "Edit" button on tab center page` | `tapOn` | Converted from matched step implementation. |
| `And I click "Close all tabs and groups" on menu` | `tapOn` | Converted from matched step implementation. |
| `And I click tab grid add button in tab center` | `tapOn` | Converted from matched step implementation. |
| `Then I should return to new tab page` | `assertVisible` | Converted from matched step implementation. |
| `When I click on the search box on NTP page` | `tapOn` | Converted from matched step implementation. |
| `And I input "https://www.microsoft.com" in search box and navigate to it` | `inputText, tapOn` | Converted from matched step implementation. |
| `Then I should see "1" on the tab center icon` | `assert` | Converted from matched step implementation. |
| `When I click on new tab button to open a new tab` | `tapOn` | Converted from matched step implementation. |
| `Then I should return to new tab page` | `assertVisible` | Converted from matched step implementation. |
| `Then I should see "2" on the tab center icon` | `assert` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I enter tab center by clicking on the tab center icon` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/tab_center.py:507` | operations=click_element; locator={"accessibilityId": "kToolbarStackButtonIdentifier"} |
| `And I click "Edit" button on tab center page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/tab_center.py:614` | operations=click_element; locator={"name": "kTabGridEditButtonIdentifier"} |
| `And I click "Close all tabs and groups" on menu` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/tab_center.py:627` | operations=click_element; locator={"name": "Close All Tabs and Groups"} |
| `And I click tab grid add button in tab center` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/tab_center.py:751` | operations=click_element; locator={"name": "Open a new tab."} |
| `Then I should return to new tab page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/tab_center.py:494` | operations=verify_element_exists; locator={"name": "NTPCollectionViewIdentifier"} |
| `When I click on the search box on NTP page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:11` | operations=click_element; locator={"name": "Search and address bar"} |
| `And I input "https://www.microsoft.com" in search box and navigate to it` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/tab_center.py:257` | operations=send_keys, click_element; locator={"name": "Address"} |
| `Then I should see "1" on the tab center icon` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/tab_center.py:806` | operations=verify_element_attribute; locator={"name": "kToolbarStackButtonIdentifier"} |
| `When I click on new tab button to open a new tab` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/tab_center.py:822` | operations=click_element; locator={"name": "kToolbarEdgeNewTabButtonIdentifier"} |
| `Then I should return to new tab page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/tab_center.py:494` | operations=verify_element_exists; locator={"name": "NTPCollectionViewIdentifier"} |
| `Then I should see "2" on the tab center icon` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/tab_center.py:835` | operations=verify_element_attribute; locator={"name": "kToolbarStackButtonIdentifier"} |

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
