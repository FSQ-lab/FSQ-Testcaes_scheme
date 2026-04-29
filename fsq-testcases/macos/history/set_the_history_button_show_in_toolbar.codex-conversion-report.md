# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/history/history.feature`
- Feature: `history`
- Scenario: `Set the History button show in toolbar`
- Tags: `@p0, @regression, @history`

## Output

- Output YAML: `fsq-testcases/macos/history/set_the_history_button_show_in_toolbar.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `launchApp` |  |
| `When I click "Settings and more" button in toolbar` | `tapOn` |  |
| `And I right click "History" button in menu` | `tapOn` |  |
| `And I click "Show in toolbar" in menu` | `tapOn` | I click "Show in toolbar" in menu |
| `Then "History" should be displayed in toolbar` | `tapOn` | "History" should be displayed in toolbar |

## Unresolved Or Low-Confidence Items

- I click "Show in toolbar" in menu
- "History" should be displayed in toolbar

## Conversion Rules Applied

- Known address bar interactions use `accessibilityId: Address and search bar`.
- Unknown UI targets are preserved as semantic `target` descriptions.
- Relation locators are used only when the source step explicitly provides context.
- No coordinates were generated.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm `appId: com.microsoft.edgemac` matches the runner environment.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Add stable locators from knowledge base when available.
- Confirm every assertion should remain blocking.
