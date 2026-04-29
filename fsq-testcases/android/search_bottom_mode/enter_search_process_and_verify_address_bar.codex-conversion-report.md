# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/search_bottom_mode.feature`
- Feature: `search_bottom_mode`
- Scenario: `Enter search process and verify address bar`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/search_bottom_mode/enter_search_process_and_verify_address_bar.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I click on the search box on NTP page` | `tapOn` |  |
| `Then I should see Omnibox with Camera icon and Copilot voice icon` | `assertVisible` |  |
| `When I input a keyword "microsoft" in the search box and click "Go" on keyboard` | `tapOn` |  |
| `Then I should see the omnibox with Copilot icon and refresh icon` | `tapOn` |  |
| `When I click on the search box` | `tapOn` |  |
| `Then I should see the omnibox with "microsoft" in the search box` | `assertVisible` |  |

## Unresolved Or Low-Confidence Items

- None

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
