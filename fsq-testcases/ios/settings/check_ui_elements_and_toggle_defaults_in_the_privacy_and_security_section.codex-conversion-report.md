# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/settings.feature`
- Feature: `L2 Settings Page`
- Scenario: `Check UI elements and toggle defaults in the "Privacy and Security" section`
- Tags: `@settings, @P0`

## Output

- Output YAML: `fsq-testcases/ios/settings/check_ui_elements_and_toggle_defaults_in_the_privacy_and_security_section.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I navigate to the Settings page` | `tapOn, tapOn` | Converted from matched step implementation. |
| `And I navigate to the "Privacy and Security" section` | `tapOn, tapOn` | Converted from matched step implementation. |
| `And I should see the element "Diagnostic Data"` | `assertVisible` | Converted from matched step implementation. |
| `And the toggle "Tracking Prevention" should be on by default` | `assert` | Converted from matched step implementation. |
| `And the toggle "Protect InPrivate Tabs by Passcode" should be off by default` | `assert` | Converted from matched step implementation. |
| `And the toggle "Microsoft Defender SmartScreen" should be on by default` | `assert` | Converted from matched step implementation. |
| `And the toggle "Website Typo Protection" should be on by default` | `assert` | Converted from matched step implementation. |
| `When I click on "Done" button on the top right corner` | `tapOn` | Converted from matched step implementation. |
| `Then I am landing on new tab page` | `assertVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I navigate to the Settings page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:9` | operations=click_element, click_element, Settings; locator={"name": "kLegacyToolbarToolsMenuButtonIdentifier"} |
| `And I navigate to the "Privacy and Security" section` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:48` | operations=click_element, click_element; locator={"name": "Privacy and Security"} |
| `And I should see the element "Diagnostic Data"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:70` | operations=verify_element_exists; locator={"name": "Diagnostic Data"} |
| `And the toggle "Tracking Prevention" should be on by default` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:172` | operations=verify_element_attribute; locator={"name": "kEdgeSettingsPrivacyTrackingPreventionCellId"} |
| `And the toggle "Protect InPrivate Tabs by Passcode" should be off by default` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:188` | operations=verify_element_attribute; locator={"name": "Protect InPrivate Tabs by Passcode, Switch button"} |
| `And the toggle "Microsoft Defender SmartScreen" should be on by default` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:204` | operations=verify_element_attribute; locator={"name": "kEdgeSettingsPrivacySmartScreenCellId"} |
| `And the toggle "Website Typo Protection" should be on by default` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:220` | operations=verify_element_attribute; locator={"name": "kEdgeSettingsPrivacyTyposquattingCellId"} |
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
