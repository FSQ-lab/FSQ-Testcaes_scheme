# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/search_bottom_mode.feature`
- Feature: `search_bottom_mode`
- Scenario: `Input complete keyword in search box`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/search_bottom_mode/input_complete_keyword_in_search_box.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I click on the search box on NTP page` | `tapOn` |  |
| `And I input a keyword "machine learning tutorials" in the search box and click "Go" on keyboard` | `tapOn` |  |
| `And I wait for 3 seconds` | `performActions` |  |
| `And I dismiss the permission dialog from bing` | `tapOn` | I dismiss the permission dialog from bing |
| `And I wait for 3 seconds` | `performActions` |  |
| `Then I should navigate to bing.com with "machine learning tutorials" in search box` | `assert` |  |
| `And I should see search results for "machine learning tutorials"` | `assertVisible` |  |
| `And I scroll the page up for 2 seconds` | `swipe` |  |
| `And I scroll the page down for 2 seconds` | `tapOn` | I scroll the page down for 2 seconds |
| `Then I should navigate to bing.com with "machine learning tutorials" in search box` | `assert` |  |

## Unresolved Or Low-Confidence Items

- I dismiss the permission dialog from bing
- I scroll the page down for 2 seconds

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
