# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/search_bottom_mode.feature`
- Feature: `search_bottom_mode`
- Scenario: `Select URL suggestion from auto suggestion list`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/search_bottom_mode/select_url_suggestion_from_auto_suggestion_list.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I click on the search box on NTP page` | `tapOn` |  |
| `And I input a keyword "developer.wikimedia.org" in the search box and click "Go" on keyboard` | `tapOn` |  |
| `And I input a keyword "developer.wikimedia.org" in the search box` | `inputText` |  |
| `And I select "Discover and build Wikimedia technology" from the auto suggestion list` | `tapOn` | I select "Discover and build Wikimedia technology" from the auto suggestion list |
| `Then I should navigate to "developer.wikimedia.org"` | `assert` |  |
| `When I click the first link on page to navigate to other pages` | `tapOn` |  |
| `And I scroll the page up for 2 seconds` | `swipe` |  |
| `And I scroll the page down for 2 seconds` | `tapOn` | I scroll the page down for 2 seconds |
| `And I click the back button on bottom toolbar` | `pressKey` |  |
| `Then I should navigate to "developer.wikimedia.org"` | `assert` |  |

## Unresolved Or Low-Confidence Items

- I select "Discover and build Wikimedia technology" from the auto suggestion list
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
