# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/fundamental/rendering.feature`
- Feature: `rendering`
- Scenario: `Fundamental Test bing.com website`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/rendering/fundamental_test_bing_com_website.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I click the search box in NTP page` | `tapOn` |  |
| `And I input "bing.com" in the search box` | `inputText` |  |
| `And I press enter to navigate to the page` | `tapOn` | I press enter to navigate to the page |
| `And I wait for the page to load completely` | `tapOn` | I wait for the page to load completely |
| `Then I should see the tab with the title "bing.com"` | `assertVisible` |  |
| `And Analyze the screenshot to verify bing webpage displayed normally` | `tapOn` | Analyze the screenshot to verify bing webpage displayed normally |

## Unresolved Or Low-Confidence Items

- I press enter to navigate to the page
- I wait for the page to load completely
- Analyze the screenshot to verify bing webpage displayed normally

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

## Codex Whole-pass Reconciliation

- Replaced prose `tapOn` commands for Enter and wait with `pressKey: Enter` and a pause action.
- Preserved source `url_bar` locator for input and the `bing.com` address-bar assertion.
- Converted source `verify_visual_task` into blocking `assertWithAI` with the original visual task intent.

