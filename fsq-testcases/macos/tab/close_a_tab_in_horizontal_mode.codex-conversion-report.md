# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/tab/tab.feature`
- Feature: `tab`
- Scenario: `Close a tab in horizontal mode`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/macos/tab/close_a_tab_in_horizontal_mode.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `launchApp` |  |
| `When I new a tab and navigate to "https://www.apple.com"` | `tapOn, inputText, pressKey` |  |
| `And I click the "Close Tab" button on tab header` | `tapOn` | I click the "Close Tab" button on tab header |
| `Then the "Apple" tab should be closed` | `assertVisible` | the "Apple" tab should be closed |

## Unresolved Or Low-Confidence Items

- I click the "Close Tab" button on tab header
- the "Apple" tab should be closed

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
