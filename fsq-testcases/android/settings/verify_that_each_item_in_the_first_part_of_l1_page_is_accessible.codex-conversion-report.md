# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/settings.feature`
- Feature: `settings`
- Scenario: `Verify that each item in the first part of L1 page is accessible`
- Tags: `@P0`

## Output

- Output YAML: `fsq-testcases/android/settings/verify_that_each_item_in_the_first_part_of_l1_page_is_accessible.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `before_scenario: Given I open edge and go to the NTP page` | `launchApp, assertVisible` | Expanded from Behave `environment.py` and `features/steps/given_steps.py`. Optional dialog/new-tab helper clicks are documented as runner repair policy because repository validation rejects `optional: true` in case YAML. |
| `When I open browser menu` | `tapOn` |  |
| `And I click on "Settings" button` | `tapOn` |  |
| `And I navigate to the "Password Manager" section` | `tapOn` |  |
| `Then I should see the page title "Microsoft Password Manager"` | `assertVisible` |  |
| `When I close the "Microsoft Password Manager" page` | `pressKey` |  |
| `And I navigate to the "Payment Methods" section` | `tapOn` |  |
| `Then I should see the page title "Payment Methods"` | `assertVisible` |  |
| `When I click back button on L2 page` | `pressKey` |  |
| `And I navigate to the "Personal Info" section` | `tapOn` |  |
| `Then I should see the page title "Personal Info"` | `assertVisible` |  |
| `When I click back button on L2 page` | `pressKey` |  |
| `And I navigate to the "Privacy and Security" section` | `tapOn` |  |
| `Then I should see the page title "Privacy and Security"` | `assertVisible` |  |
| `When I click back button on L2 page` | `pressKey` |  |
| `And I navigate to the "Microsoft Services" section` | `tapOn` |  |
| `Then I should see the page title "Microsoft Services"` | `assertVisible` |  |
| `When I click back button on L2 page` | `pressKey` |  |
| `And I click back button on setting page` | `pressKey` |  |
| `Then I can see the new tab page` | `tapOn` |  |

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

- None

## Conversion Rules Applied

- Optional startup dialog dismissal and optional new-tab click are preserved as report evidence/runner repair policy instead of `optional: true` YAML commands.

- Runtime screenshot, telemetry, and autoretry hooks are documented in the report but not converted into YAML commands.

- Android Behave `before_scenario` setup is expanded before scenario body commands.

- Android Behave `before_scenario` setup contributes `launchApp`; converted YAML keeps each case isolated with final `killApp`.
- Known literal UI labels are converted to semantic `target` actions.
- Unknown UI targets are preserved as semantic `target` descriptions.
- No coordinates were invented; gesture coordinates are preserved only when they come from source step implementations.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm `appId: com.microsoft.emmx` matches the runner environment.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Add stable Android locators from knowledge base when available.
- Confirm every assertion should remain blocking.

## Codex Whole-pass Reconciliation

- Preserved browser menu locator and source `Navigate up` accessibility id instead of generic Back.
- Replaced final Add New Tab action with the source NTP assertion on `Account menu`.
- Kept all settings section/page title assertions locator-backed from source step definitions.

