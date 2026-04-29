# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/fundamental/rendering.feature`
- Feature: `rendering`
- Scenario: `Fundamental Test bing website`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/ios/rendering/fundamental_test_bing_website.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | iOS source scenarios commonly omit explicit launch step. |
| `When I click the search box in NTP page` | `tapOn` | I click the search box in NTP page |
| `And I type "www.bing.com" in the search box` | `inputText` |  |
| `And I press go button to search` | `tapOn` | I press go button to search |
| `Then I should see the Microsoft bing logo` | `assertVisible` |  |

## Unresolved Or Low-Confidence Items

- I click the search box in NTP page
- I press go button to search

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
