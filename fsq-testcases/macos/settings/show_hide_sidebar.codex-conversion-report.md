# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/settings/settings.feature`
- Feature: `settings`
- Scenario: `Show/hide sidebar`
- Tags: `@regression, @p0, @settings`

## Output

- Output YAML: `fsq-testcases/macos/settings/show_hide_sidebar.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `launchApp` |  |
| `And I input "edge://settings/appearance/copilotAndSidebar" to the address bar` | `tapOn, inputText` |  |
| `When I select "Always on" option in Settings page` | `tapOn` | I select "Always on" option in Settings page |
| `Then the sidebar should be visible` | `assertVisible` |  |
| `When I select "Off" option in Settings page` | `tapOn` | I select "Off" option in Settings page |
| `Then the sidebar should be hidden` | `assertNotVisible` |  |

## Unresolved Or Low-Confidence Items

- I select "Always on" option in Settings page
- I select "Off" option in Settings page

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
