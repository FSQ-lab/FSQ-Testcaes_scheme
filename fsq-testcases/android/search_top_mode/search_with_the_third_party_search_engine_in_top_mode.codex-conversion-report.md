# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/search_top_mode.feature`
- Feature: `search_top_mode`
- Scenario: `Search with the third party search engine in top mode`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/search_top_mode/search_with_the_third_party_search_engine_in_top_mode.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I open browser menu` | `tapOn` |  |
| `And I click on "Settings" button` | `tapOn` |  |
| `And I click on "Search" button in settings` | `tapOn` |  |
| `And I click on "Search engine" button in Search settings` | `tapOn` |  |
| `And I select "Google" radio button` | `tapOn` | I select "Google" radio button |
| `And I click back button on L3 page` | `pressKey` |  |
| `Then I see "Google" shown on "Search engine" section` | `tapOn` | I see "Google" shown on "Search engine" section |
| `When I click back button on L2 page` | `pressKey` |  |
| `And I click back button on setting page` | `pressKey` |  |
| `And I click on the top address bar on NTP page` | `tapOn` |  |
| `And I input a keyword "microsoft" in the search box and click "Go" on keyboard` | `tapOn` |  |
| `Then I should see the omnibox with "google.com" in the search box` | `assertVisible` |  |
| `When I perform a long press gesture on address bar` | `tapOn` | I perform a long press gesture on address bar |
| `And I click on "Move address bar to bottom" option` | `tapOn` |  |
| `Then I should see address bar on the bottom of screen` | `assertVisible` |  |
| `When I open browser menu` | `tapOn` |  |
| `And I click on "Settings" button` | `tapOn` |  |
| `And I click on "Search" button in settings` | `tapOn` |  |
| `And I click on "Search engine" button in Search settings` | `tapOn` |  |
| `And I select "Bing" radio button` | `tapOn` | I select "Bing" radio button |
| `And I click back button on L3 page` | `pressKey` |  |
| `Then I see "Bing" shown on "Search engine" section` | `tapOn` | I see "Bing" shown on "Search engine" section |

## Unresolved Or Low-Confidence Items

- I select "Google" radio button
- I see "Google" shown on "Search engine" section
- I perform a long press gesture on address bar
- I select "Bing" radio button
- I see "Bing" shown on "Search engine" section

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

## Post-run Corrections

- Preserved source settings/search/search-engine XPath locators and Google/Bing summary assertions.
- Fixed keyword submission to `inputText` followed by `pressKey: Enter`.
- Preserved source `google.com` address-bar assertion, top address-bar locator, bottom omnibox assertion, and browser menu resource id.

