# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/settings/settings.feature`
- Feature: `settings`
- Scenario: `Restore by new tab`
- Tags: `@regression, @p0, @settings`

## Output

- Output YAML: `fsq-testcases/macos/settings/restore_by_new_tab.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `launchApp` |  |
| `And I input "edge://settings/startHomeNTP" to the address bar` | `tapOn, inputText` |  |
| `When I select the option "Open the new tab page"` | `tapOn` |  |
| `And I open a new tab` | `tapOn` |  |
| `And I navigate to "https://www.bing.com"` | `tapOn, inputText, pressKey` |  |
| `And I close and restart Edge` | `killApp, launchApp` |  |
| `Then edge should open with a page titled "New Tab"` | `assertVisible` | edge should open with a page titled "New Tab" |

## Unresolved Or Low-Confidence Items

- edge should open with a page titled "New Tab"

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
