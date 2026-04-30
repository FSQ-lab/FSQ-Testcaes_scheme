# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/growth/db.feature`
- Feature: `db`
- Scenario: `Growth Could entry rewards page in New Tab page`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/db/growth_could_entry_rewards_page_in_new_tab_page.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `Given I login to edge with MSA` | `tapOn` | I login to edge with MSA |
| `When I click the account in NTP page` | `tapOn` | I click the account in NTP page |
| `And I click the "Microsoft Rewards" option` | `tapOn` | I click the "Microsoft Rewards" option |
| `Then I can see the Microsoft Rewards page open normally` | `assertVisible` |  |

## Unresolved Or Low-Confidence Items

- I login to edge with MSA
- I click the account in NTP page
- I click the "Microsoft Rewards" option

## Conversion Rules Applied

- Android scenarios without explicit launch steps receive an implicit `launchApp`.
- Known literal UI labels are converted to semantic `target` actions.
- Unknown UI targets are preserved as semantic `target` descriptions.
- No coordinates were generated.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm `appId: com.microsoft.emmx` matches the runner environment.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Add stable Android locators from knowledge base when available.
- Confirm every assertion should remain blocking.

## Post-run Corrections

- Reclassified `Given I login to edge with MSA` as a precondition/helper flow, not a single `tapOn` action.
- The pilot DSL now assumes the device is already signed in and asserts the NTP account entry before opening Rewards.
- Full conditional login expansion remains out of scope for this pilot conversion because it requires account credentials and multiple helper steps.

