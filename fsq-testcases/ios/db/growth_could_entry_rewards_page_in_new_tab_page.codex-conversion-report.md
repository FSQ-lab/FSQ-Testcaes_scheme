# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/growth/db.feature`
- Feature: `Edge db`
- Scenario: `Growth Could entry rewards page in New Tab page`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/ios/db/growth_could_entry_rewards_page_in_new_tab_page.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given I sign in to Edge with MSA` | `tapOn` | Converted from matched step implementation. |
| `When I click the account in NTP page` | `tapOn` | Converted from matched step implementation. |
| `And I click the "Microsoft Rewards" option` | `tapOn` | Converted from matched step implementation. |
| `Then I can see the Microsoft Rewards page open normally` | `assertVisible` | Converted from matched step implementation. |

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
| `Given I sign in to Edge with MSA` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/given_steps.py:253` | operations=find_element, Sign in to sync; locator={"xpath": "//XCUIElementTypeButton[@name='Sign in to sync' and @x='32']"} |
| `When I click the account in NTP page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/growth/db.py:102` | operations=click_element; locator={"name": "kEdgeNTPViewAvatarViewIdentifier"} |
| `And I click the "Microsoft Rewards" option` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/growth/db.py:115` | operations=click_element; locator={"name": "Microsoft Rewards"} |
| `Then I can see the Microsoft Rewards page open normally` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/steps/growth/db.py:128` | operations=verify_element_exists; locator={"name": "Microsoft Rewards"} |

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
