# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/overflow_menu.feature`
- Feature: `overflow_menu`
- Scenario: `Complete all menu workflow through overflow menu on NTP`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/overflow_menu/complete_all_menu_workflow_through_overflow_menu_on_ntp.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `before_scenario: Given I open edge and go to the NTP page` | `launchApp, assertVisible` | Expanded from Behave `environment.py` and `features/steps/given_steps.py`. Optional dialog/new-tab helper clicks are documented as runner repair policy because repository validation rejects `optional: true` in case YAML. |
| `When I open the browser menu by tapping on the three dots icon at the bottom right corner` | `tapOn` | Preserved Appium ID: `com.microsoft.emmx:id/overflow_button_bottom`. |
| `And I swipe within the scrollable area on menu from right to left to go to the second page` | `swipe` | Preserved action semantics as a left swipe. |
| `And I tap "All Menu" from the menu` | `tapOn` | Preserved source XPath: `//android.widget.TextView[@text='All menu']`. |
| `Then the All Menu panel should open` | `assertVisible` | Preserved source XPath: `//android.widget.TextView[@text='All Menu']`. |
| `When I click "Edit" on All menu panel` | `tapOn` | Preserved Appium ID: `com.microsoft.emmx:id/toolbar_button_edit_done`. |
| `Then The All menu edit mode should be opened` | `assertVisible` | Preserved source XPath: `//android.widget.TextView[@text='Edit Menu']`. |
| `And The "Favorites" is disabled` | `assert` | Preserved source XPath and enabled=false assertion. |
| `When I click "Drop" icon` | `tapOn` | Preserved source XPath: `//android.widget.TextView[@text='Drop']/..`. |
| `And I click "Done" on All menu panel` | `tapOn` | Preserved source XPath: `//android.widget.Button[@text='Done']`. |
| `And I click back button on All menu panel` | `tapOn` | Preserved Appium ID: `com.microsoft.emmx:id/back_button`. |
| `And I open the browser menu by tapping on the three dots icon at the bottom right corner` | `tapOn` | Preserved Appium ID: `com.microsoft.emmx:id/overflow_button_bottom`. |
| `And I swipe within the scrollable area on menu from right to left to go to the second page` | `swipe` | Preserved action semantics as a left swipe. |
| `Then I should not see "Drop" on menu` | `assertNotVisible` | Preserved source XPath: `//android.widget.TextView[@text='Drop']`. |
| `When I tap "All Menu" from the menu` | `tapOn` | Preserved source XPath: `//android.widget.TextView[@text='All menu']`. |
| `And I click "Edit" on All menu panel` | `tapOn` | Preserved Appium ID: `com.microsoft.emmx:id/toolbar_button_edit_done`. |
| `And I scroll the page up slightly` | `swipe` | Preserved action semantics as an upward swipe. |
| `And I click "Drop" icon` | `tapOn` | Preserved source XPath: `//android.widget.TextView[@text='Drop']/..`. |
| `And I click "Done" on All menu panel` | `tapOn` | Preserved source XPath: `//android.widget.Button[@text='Done']`. |
| `And I click back button on All menu panel` | `tapOn` | Preserved Appium ID: `com.microsoft.emmx:id/back_button`. |
| `And I open the browser menu by tapping on the three dots icon at the bottom right corner` | `tapOn` | Preserved Appium ID: `com.microsoft.emmx:id/overflow_button_bottom`. |
| `And I swipe within the scrollable area on menu from right to left to go to the second page` | `swipe` | Preserved action semantics as a left swipe. |
| `Then I should see "Drop" on menu` | `assertVisible` | Preserved source XPath: `//android.widget.TextView[@text='Drop']`. |

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

- None for locator preservation. Runner still needs device validation for exact gesture distance and current app build locators.

## Conversion Rules Applied

- Optional startup dialog dismissal and optional new-tab click are preserved as report evidence/runner repair policy instead of `optional: true` YAML commands.

- Runtime screenshot, telemetry, and autoretry hooks are documented in the report but not converted into YAML commands.

- Android Behave `before_scenario` setup is expanded before scenario body commands.

- Android Behave `before_scenario` setup contributes `launchApp`; converted YAML keeps each case isolated with final `killApp`.
- Known literal UI labels are converted to semantic `target` actions.
- Appium locators found in Behave step definitions are preserved as dual-layer `target` + `locator` or locator-backed assertions.
- Swipe steps are kept as direct action commands instead of prose `tapOn` steps.
- No coordinates were invented; gesture coordinates are preserved only when they come from source step implementations.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm `appId: com.microsoft.emmx` matches the runner environment.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Confirm preserved Appium locators still match the current Android app build.
- Confirm the left swipe reaches the second overflow-menu page on the test device size.
- Confirm every assertion should remain blocking.

## Post-run Corrections

- Preserved source horizontal menu swipe as W3C pointer actions with exact coordinates `(800,1900)->(200,1900)` and `duration=1000`.
- Avoided generic `swipe: left` because menu paging depends on the original gesture target and path.

