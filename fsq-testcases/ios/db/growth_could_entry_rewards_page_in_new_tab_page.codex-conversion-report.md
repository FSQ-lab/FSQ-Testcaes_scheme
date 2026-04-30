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
