# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/search_bottom_mode.feature`
- Feature: `search_bottom_mode`
- Scenario: `Complete search process with bottom omnibox`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/search_bottom_mode/complete_search_process_with_bottom_omnibox.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `before_scenario: Given I open edge and go to the NTP page` | `launchApp, assertVisible` | Expanded from Behave `environment.py` and `features/steps/given_steps.py`. Optional dialog/new-tab helper clicks are documented as runner repair policy because repository validation rejects `optional: true` in case YAML. |
| `When I click on the address bar on NTP page` | `tapOn` |  |
| `Then I should see the topsites shown on ZIP` | `assertVisible` | Preserved Appium ID from step definition: `com.microsoft.emmx:id/suggestion_top_sites_list`. |
| `And I should see the camera search icon on omnibox` | `assertVisible` | Preserved Appium ID from step definition: `com.microsoft.emmx:id/attachment_right_camera_button`. |
| `And I should see the Copilot voice icon on omnibox` | `assertVisible` | Preserved Appium ID from step definition: `com.microsoft.emmx:id/attachment_right_mic_button`. |
| `When I input a keyword "chinatravel.com"` | `inputText` |  |
| `Then I should see the suggestion list shown next to Omnibox` | `assertVisible` | Preserved Appium ID from step definition: `com.microsoft.emmx:id/omnibox_suggestions_dropdown`. |
| `When I click "Go" on keyboard` | `tapOn` |  |
| `Then the address bar is fully expanded and show "chinatravel.com"` | `tapOn` | the address bar is fully expanded and show "chinatravel.com" |

## BDD Execution Model

- Effective scenario steps are built from the feature scenario plus Behave `before_scenario` setup.
- `before_scenario` executes `Given I open edge and go to the NTP page` before each non-skipped scenario.
- The setup step expands through `context.execute_steps()` into `Given I open edge`, `And I dismiss the alert dialog`, `And I click new tab button to open a new tab`, and `Then I can see the new tab page`; YAML keeps the deterministic launch and NTP assertion, while optional helpers remain report evidence.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| `before_all` | runner lifecycle / environment requirements | No | Loads `.env`, starts MCP session, initializes telemetry, reads `PACKAGE`, `TEST_ACCOUNT_EMAIL`, and `TEST_ACCOUNT_PASSWORD`. |
| `before_scenario` version and tag checks | environment constraints | Report only | `@wip`, `@fre`, `@v*`, and `@vmax*` affect case eligibility, not YAML commands. |
| `before_scenario` NTP setup | setup/state guarantee | Partial | YAML keeps launch plus blocking NTP assertion. Optional dialog dismissal and optional new-tab click are documented for runner repair instead of case commands. |
| `after_scenario` screenshot | runtime evidence | No | Runner/evidence policy, not case behavior. |
| `before_feature` autoretry patch | runner policy | No | Retry policy is outside case DSL. |
| `after_step` telemetry | runtime evidence | No | Telemetry is not converted to YAML. |

## Environment Requirements

- `PACKAGE`: Android app id and resource-id prefix. Converted YAML keeps `appId: com.microsoft.emmx`; source default is `com.microsoft.emmx.canary` when env is absent.
- `TEST_ACCOUNT_EMAIL`: Required only for account/MSA scenarios; no plaintext value is written to YAML.
- `TEST_ACCOUNT_PASSWORD`: Required only for account/MSA scenarios; no plaintext value is written to YAML.
- The app is assumed to be installed and launchable; install/uninstall setup is not represented in these cases.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| `Given I open edge and go to the NTP page` | `Given I open edge`; `And I dismiss the alert dialog`; `And I click new tab button to open a new tab`; `Then I can see the new tab page` | `features/steps/given_steps.py:44`; child implementations at `given_steps.py:6`, `given_steps.py:12`, `given_steps.py:31`, `given_steps.py:37` |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `before_scenario: Given I open edge and go to the NTP page` | `features/environment.py:326`; `features/steps/given_steps.py:44` | `app_launch`; optional permission/popup dismiss clicks; optional `Add New tab` click; `verify_element_exists` for `Account menu` |

## Unresolved Or Low-Confidence Items

- the address bar is fully expanded and show "chinatravel.com"

## Conversion Rules Applied

- Optional startup dialog dismissal and optional new-tab click are preserved as report evidence/runner repair policy instead of `optional: true` YAML commands.

- Runtime screenshot, telemetry, and autoretry hooks are documented in the report but not converted into YAML commands.

- Android Behave `before_scenario` setup is expanded before scenario body commands.

- Android Behave `before_scenario` setup contributes `launchApp`; converted YAML keeps each case isolated with final `killApp`.
- Known literal UI labels are converted to semantic `target` actions.
- Unknown UI targets are preserved as semantic `target` descriptions.
- Appium locators found in Behave step definitions are preserved as dual-layer `target` + `locator` fields.
- No coordinates were invented; gesture coordinates are preserved only when they come from source step implementations.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm `appId: com.microsoft.emmx` matches the runner environment.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Confirm preserved Appium resource IDs still match the current Android app build.
- Confirm every assertion should remain blocking.

## Post-run Corrections

- Preserved source locators for top sites, camera icon, Copilot voice icon, suggestion dropdown, and address bar text assertion.
- Kept icon assertions accessibility-backed rather than screenshot-backed because the source step uses Appium ids.

## Codex Whole-pass Reconciliation

- Preserved `url_bar` locator for focusing/input and source locators for top sites, camera, mic, and suggestion dropdown.
- Fixed submit action to `pressKey: Enter` instead of semantic `tapOn: Go`.
- Converted final address-bar state to a locator-backed structured assertion.

