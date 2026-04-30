# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/search_bottom_mode.feature`
- Feature: `search`
- Scenario: `Verify Bottom address bar on NTP`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/ios/search_bottom_mode/verify_bottom_address_bar_on_ntp.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I click + button on the bottom toolbar` | `tapOn` | Converted from matched step implementation. |
| `When I change the NTP page layout to Partial view` | `tapOn, tapOn` | Converted from matched step implementation. |
| `And I close the Page settings dialog` | `tapOn` | Converted from matched step implementation. |
| `And I scroll feeds up for 3 seconds` | `performActions` | Converted from matched step implementation. |
| `Then I should see the omnibox with Copilot icon and Copilot voice icon` | `assertVisible, assertVisible` | Converted from matched step implementation. |
| `When I scroll feeds down for 3 seconds` | `performActions` | Converted from matched step implementation. |
| `Then I should see the omnibox with Copilot icon and Copilot voice icon` | `assertVisible, assertVisible` | Converted from matched step implementation. |
| `When I change the NTP page layout to Headings view` | `tapOn, tapOn` | Converted from matched step implementation. |
| `And I close the Page settings dialog` | `tapOn` | Converted from matched step implementation. |
| `And I scroll feeds up for 3 seconds` | `performActions` | Converted from matched step implementation. |
| `Then I should see the omnibox with Copilot icon and Copilot voice icon` | `assertVisible, assertVisible` | Converted from matched step implementation. |
| `When I scroll feeds down for 3 seconds` | `performActions` | Converted from matched step implementation. |
| `Then I should see the omnibox with Copilot icon and Copilot voice icon` | `assertVisible, assertVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I click + button on the bottom toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:396` | operations=click_element; locator={"accessibilityId": "kToolbarEdgeNewTabButtonIdentifier"} |
| `When I change the NTP page layout to Partial view` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:295` | operations=click_element, click_element; locator={"name": "New tab page layout settings"} |
| `And I close the Page settings dialog` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:634` | operations=tap_coordinates |
| `And I scroll feeds up for 3 seconds` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:318` | operations=swipe |
| `Then I should see the omnibox with Copilot icon and Copilot voice icon` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:334` | operations=verify_element_exists, verify_element_exists; locator={"name": "Copilot"} |
| `When I scroll feeds down for 3 seconds` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:357` | operations=swipe |
| `Then I should see the omnibox with Copilot icon and Copilot voice icon` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:334` | operations=verify_element_exists, verify_element_exists; locator={"name": "Copilot"} |
| `When I change the NTP page layout to Headings view` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:373` | operations=click_element, click_element; locator={"name": "New tab page layout settings"} |
| `And I close the Page settings dialog` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:634` | operations=tap_coordinates |
| `And I scroll feeds up for 3 seconds` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:318` | operations=swipe |
| `Then I should see the omnibox with Copilot icon and Copilot voice icon` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:334` | operations=verify_element_exists, verify_element_exists; locator={"name": "Copilot"} |
| `When I scroll feeds down for 3 seconds` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:357` | operations=swipe |
| `Then I should see the omnibox with Copilot icon and Copilot voice icon` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/search_bottom_mode.py:334` | operations=verify_element_exists, verify_element_exists; locator={"name": "Copilot"} |

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
