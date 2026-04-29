# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/growth/db.feature`
- Feature: `db`
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
| `Implicit conversion assumption` | `launchApp` | iOS source scenarios commonly omit explicit launch step. |
| `Given I sign in to Edge with MSA` | `tapOn` | I sign in to Edge with MSA |
| `When I click the account in NTP page` | `tapOn` | I click the account in NTP page |
| `And I click the "Microsoft Rewards" option` | `tapOn` |  |
| `Then I can see the Microsoft Rewards page open normally` | `assertVisible` |  |

## Unresolved Or Low-Confidence Items

- I sign in to Edge with MSA
- I click the account in NTP page

## Conversion Rules Applied

- iOS scenarios without explicit launch steps receive an implicit `launchApp`.
- Known literal UI labels are converted to semantic `target` actions.
- Screenshot analysis steps are converted to blocking `assertWithAI` commands.
- Unknown UI targets are preserved as semantic `target` descriptions.
- No coordinates were generated.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm `appId: com.microsoft.msedge` matches the runner environment.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Add stable iOS locators from knowledge base when available.
- Confirm every assertion should remain blocking.
