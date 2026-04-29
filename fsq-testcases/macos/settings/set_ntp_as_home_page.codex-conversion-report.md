# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/settings/settings.feature`
- Feature: `settings`
- Scenario: `Set NTP as home page`
- Tags: `@settings, @smoke, @p0`

## Output

- Output YAML: `fsq-testcases/macos/settings/set_ntp_as_home_page.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `launchApp` |  |
| `And I input "edge://settings/startHomeNTP" to the address bar` | `tapOn, inputText` |  |
| `When I turn on the option "show home button on the toolbar"` | `tapOn` |  |
| `And I select the option "New tab page"` | `tapOn` |  |
| `When I click "Home" button to the left of the address bar` | `tapOn` |  |
| `Then should open a page titled "New Tab"` | `assertVisible` | should open a page titled "New Tab" |

## Unresolved Or Low-Confidence Items

- should open a page titled "New Tab"

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
