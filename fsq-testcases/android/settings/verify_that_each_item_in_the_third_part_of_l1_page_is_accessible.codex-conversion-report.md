# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/settings.feature`
- Feature: `settings`
- Scenario: `Verify that each item in the third part of L1 page is accessible`
- Tags: `@P0`

## Output

- Output YAML: `fsq-testcases/android/settings/verify_that_each_item_in_the_third_part_of_l1_page_is_accessible.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I open browser menu` | `tapOn` |  |
| `And I click on "Settings" button` | `tapOn` |  |
| `And I scroll up the page for 2 second` | `swipe` |  |
| `And I navigate to the "Languages" section` | `tapOn` |  |
| `Then I should see the page title "Languages"` | `assertVisible` |  |
| `When I click back button on the upper left corner` | `pressKey` |  |
| `And I navigate to the "Site Settings" section` | `tapOn` |  |
| `Then I should see the page title "Site Settings"` | `assertVisible` |  |
| `When I click back button on the upper left corner` | `pressKey` |  |
| `And I navigate to the "Notifications" section` | `tapOn` |  |
| `Then I should see the page title "Notifications"` | `assertVisible` |  |
| `When I click back button on the upper left corner` | `pressKey` |  |
| `And I scroll the page up slightly` | `swipe` |  |
| `And I navigate to the "About Microsoft Edge" section` | `tapOn` |  |
| `Then I should see the page title "About Microsoft Edge"` | `assertVisible` |  |

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

## Codex Whole-pass Reconciliation

- Preserved browser menu locator and source `Navigate up` accessibility id instead of generic Back.
- Converted settings scroll helper steps to W3C pointer actions.
- Kept all lower settings section/page title assertions locator-backed from source step definitions.

