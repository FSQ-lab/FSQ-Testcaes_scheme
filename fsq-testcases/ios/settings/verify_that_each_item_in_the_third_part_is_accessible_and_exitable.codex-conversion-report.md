# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/settings.feature`
- Feature: `L2 Settings Page`
- Scenario: `Verify that each item in the third part is accessible and exitable`
- Tags: `@settings, @P0`

## Output

- Output YAML: `fsq-testcases/ios/settings/verify_that_each_item_in_the_third_part_is_accessible_and_exitable.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I navigate to the Settings page` | `tapOn, tapOn` | Converted from matched step implementation. |
| `And I swipe up to bottom of the page` | `performActions` | Converted from matched step implementation. |
| `Then analyze the screenshot to verify that settings page contains the following items3` | `assertWithAI` | Converted from matched step implementation. |
| `And I navigate to the "Languages" section` | `tapOn` | Converted from matched step implementation. |
| `Then I should see the page title "Languages"` | `assertVisible` | Converted from matched step implementation. |
| `And I click back button on the upper left corner` | `tapOn` | Converted from matched step implementation. |
| `And I navigate to the "Site Settings" section` | `tapOn` | Converted from matched step implementation. |
| `Then I should see the page title "Site Settings"` | `assertVisible` | Converted from matched step implementation. |
| `And I click back button on the upper left corner` | `tapOn` | Converted from matched step implementation. |
| `And I navigate to the "Notifications" section` | `tapOn` | Converted from matched step implementation. |
| `Then I should see the page title "Notifications"` | `assertVisible` | Converted from matched step implementation. |
| `And I click back button on the upper left corner` | `tapOn` | Converted from matched step implementation. |
| `And I navigate to the "About Microsoft Edge" section` | `tapOn` | Converted from matched step implementation. |
| `Then I should see the page title "About Microsoft Edge"` | `assertVisible` | Converted from matched step implementation. |
| `When I click on "Done" button on the top right corner` | `tapOn` | Converted from matched step implementation. |
| `Then I am landing on new tab page` | `assertVisible` | Converted from matched step implementation. |

## BDD Execution Model

- Converted using the latest Codex FSQ Case Converter rule: feature scenario supplies intent and order; Behave step implementations supply executable operations, locators, assertions, waits, and helper behavior.
- Effective steps include Gherkin Background plus scenario steps when present.
- `features/steps/**/*.py` is treated as the global Behave step registry; matching is by exact or parameterized decorator before semantic fallback.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| `before_all` / Appium session setup | runner lifecycle / environment requirements | No | Keep Appium/MCP session creation and telemetry out of case YAML. |
| `before_scenario` / setup helpers | setup/state guarantee | Partial | Material app launch/NTP assumptions are represented by `launchApp`; optional dialogs remain runner repair/evidence unless safely expressible. |
| `after_scenario` / result capture | runtime evidence | No | Screenshots, reports, and logs are not converted into case commands. |

## Environment Requirements

- iOS Edge app installed and launchable with Appium 3.x MCP.
- Account credentials are required only for account/MSA/rewards flows and are not written into YAML.
- Source runtime screenshots/logs are runner evidence, not case commands.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| Scenario steps | none or already reflected in Step Implementation Evidence | No unresolved `context.execute_steps()` expansion was identified during this report upgrade; any material setup/precondition is documented in Hook Normalization or Unresolved items. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I navigate to the Settings page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:9` | operations=click_element, click_element, Settings; locator={"name": "kLegacyToolbarToolsMenuButtonIdentifier"} |
| `And I swipe up to bottom of the page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:32` | operations=swipe |
| `Then analyze the screenshot to verify that settings page contains the following items3` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:905` | operations=verify_visual_task |
| `And I navigate to the "Languages" section` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:634` | operations=click_element; locator={"name": "kEdgeSettingsLanguagesCellId"} |
| `Then I should see the page title "Languages"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:699` | operations=verify_element_exists; locator={"name": "Languages"} |
| `And I click back button on the upper left corner` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:647` | operations=click_element; locator={"name": "Settings"} |
| `And I navigate to the "Site Settings" section` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:660` | operations=click_element; locator={"name": "kEdgeSettingsSiteSettingsCellId"} |
| `Then I should see the page title "Site Settings"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:712` | operations=verify_element_exists; locator={"name": "Site Settings"} |
| `And I click back button on the upper left corner` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:647` | operations=click_element; locator={"name": "Settings"} |
| `And I navigate to the "Notifications" section` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:673` | operations=click_element; locator={"name": "kEdgeSettingsNotificationCellId"} |
| `Then I should see the page title "Notifications"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:725` | operations=verify_element_exists; locator={"name": "Notifications"} |
| `And I click back button on the upper left corner` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:647` | operations=click_element; locator={"name": "Settings"} |
| `And I navigate to the "About Microsoft Edge" section` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:686` | operations=click_element; locator={"name": "kEdgeSettingsAboutEdgeCellId"} |
| `Then I should see the page title "About Microsoft Edge"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/core/settings.py:738` | operations=verify_element_exists; locator={"name": "About Microsoft Edge"} |
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
