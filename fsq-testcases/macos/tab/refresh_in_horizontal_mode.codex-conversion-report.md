# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/tab/tab.feature`
- Feature: `tab`
- Scenario: `Refresh in horizontal mode`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/macos/tab/refresh_in_horizontal_mode.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `launchApp` |  |
| `When I navigate to "https://www.youtube.com"` | `tapOn, inputText, pressKey` |  |
| `And I right click on the tab header of "Youtube" tab` | `tapOn` | I right click on the tab header of "Youtube" tab |
| `And I click "Refresh" from the context menu` | `tapOn` | I click "Refresh" from the context menu |
| `Then the page should be refreshed` | `assertVisible` | the page should be refreshed |
| `And the address bar still displays the complete URL "https://www.youtube.com"` | `assertVisible` | the address bar still displays the complete URL "https://www.youtube.com" |

## Unresolved Or Low-Confidence Items

- I right click on the tab header of "Youtube" tab
- I click "Refresh" from the context menu
- the page should be refreshed
- the address bar still displays the complete URL "https://www.youtube.com"

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
