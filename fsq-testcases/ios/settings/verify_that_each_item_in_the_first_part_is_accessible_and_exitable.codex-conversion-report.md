# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/settings.feature`
- Feature: `L2 Settings Page`
- Scenario: `Verify that each item in the first part is accessible and exitable`
- Tags: `@settings, @P0`

## Output

- Output YAML: `fsq-testcases/ios/settings/verify_that_each_item_in_the_first_part_is_accessible_and_exitable.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I navigate to the Settings page` | `tapOn, tapOn` | Converted from matched step implementation. |
| `Then analyze the screenshot to verify that settings page contains the following items1` | `assertWithAI` | Converted from matched step implementation. |
| `And I navigate to the "Payment Methods" section` | `tapOn` | Converted from matched step implementation. |
| `Then I should see the page title "Payment Methods"` | `assertVisible` | Converted from matched step implementation. |
| `And I click back button on the upper left corner` | `tapOn` | Converted from matched step implementation. |
| `And I navigate to the "Personal Info" section` | `tapOn` | Converted from matched step implementation. |
| `Then I should see the page title "Personal Info"` | `assertVisible` | Converted from matched step implementation. |
| `And I click back button on the upper left corner` | `tapOn` | Converted from matched step implementation. |
| `And I navigate to the "Privacy and Security" section` | `tapOn, tapOn` | Converted from matched step implementation. |
| `Then I should see the page title "Privacy and Security"` | `assertVisible` | Converted from matched step implementation. |
| `And I click back button on the upper left corner` | `tapOn` | Converted from matched step implementation. |
| `And I navigate to the "Microsoft Services" section` | `tapOn, tapOn` | Converted from matched step implementation. |
| `Then I should see the page title "Microsoft Services"` | `assertVisible` | Converted from matched step implementation. |
| `When I click on "Done" button on the top right corner` | `tapOn` | Converted from matched step implementation. |
| `Then I am landing on new tab page` | `assertVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I navigate to the Settings page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:9` | operations=click_element, click_element, Settings; locator={"name": "kLegacyToolbarToolsMenuButtonIdentifier"} |
| `Then analyze the screenshot to verify that settings page contains the following items1` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:879` | operations=verify_visual_task |
| `And I navigate to the "Payment Methods" section` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:762` | operations=click_element; locator={"name": "Payment Methods"} |
| `Then I should see the page title "Payment Methods"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:775` | operations=verify_element_exists; locator={"accessibilityId": "Payment Methods"} |
| `And I click back button on the upper left corner` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:647` | operations=click_element; locator={"name": "Settings"} |
| `And I navigate to the "Personal Info" section` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:788` | operations=click_element; locator={"name": "Personal Info"} |
| `Then I should see the page title "Personal Info"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:801` | operations=verify_element_exists; locator={"accessibilityId": "Personal Info"} |
| `And I click back button on the upper left corner` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:647` | operations=click_element; locator={"name": "Settings"} |
| `And I navigate to the "Privacy and Security" section` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:48` | operations=click_element, click_element; locator={"name": "Privacy and Security"} |
| `Then I should see the page title "Privacy and Security"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:814` | operations=verify_element_exists; locator={"accessibilityId": "Privacy and Security"} |
| `And I click back button on the upper left corner` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:647` | operations=click_element; locator={"name": "Settings"} |
| `And I navigate to the "Microsoft Services" section` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:83` | operations=click_element, click_element; locator={"name": "Microsoft Services"} |
| `Then I should see the page title "Microsoft Services"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:827` | operations=verify_element_exists; locator={"accessibilityId": "Microsoft Services"} |
| `When I click on "Done" button on the top right corner` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:424` | operations=click_element; locator={"name": "kSettingsDoneButtonId"} |
| `Then I am landing on new tab page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/default_bottom_omnibox.py:270` | operations=verify_element_exists; locator={"name": "NTPCollectionViewIdentifier"} |

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
