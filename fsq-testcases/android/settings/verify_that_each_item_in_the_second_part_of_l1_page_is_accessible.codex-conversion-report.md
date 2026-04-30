# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/settings.feature`
- Feature: `settings`
- Scenario: `Verify that each item in the second part of L1 page is accessible`
- Tags: `@P0`

## Output

- Output YAML: `fsq-testcases/android/settings/verify_that_each_item_in_the_second_part_of_l1_page_is_accessible.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I open browser menu` | `tapOn` |  |
| `And I click on "Settings" button` | `tapOn` |  |
| `And I navigate to the "Set as Default Browser" section` | `tapOn` |  |
| `Then I should see "Set edge as your default browser app?" dialog` | `assertVisible` |  |
| `When I click on "Cancel" button on dialog` | `tapOn` |  |
| `Then the dialog should close` | `assertNotVisible` |  |
| `When I navigate to the "Search" section` | `tapOn` |  |
| `Then I should see the page title "Search"` | `assertVisible` |  |
| `When I click back button on L2 page` | `pressKey` |  |
| `And  I click on "Appearance and layout" button` | `tapOn` |  |
| `Then I should see the page title "Appearance and Layout"` | `assertVisible` |  |
| `When I click back button on L2 page` | `pressKey` |  |
| `And I scroll the page up slightly` | `swipe` |  |
| `And I navigate to the "New Tab Page" section` | `tapOn` |  |
| `Then I should see the page title "New Tab Page"` | `tapOn` |  |
| `When I click back button on L2 page` | `pressKey` |  |
| `And I scroll up the page for 2 second` | `swipe` |  |
| `And I navigate to the "Tabs" section` | `tapOn` |  |
| `Then I should see the page title "Tabs"` | `assertVisible` |  |
| `When I click back button on L2 page` | `pressKey` |  |
| `And I navigate to the "Accessibility" section` | `tapOn` |  |
| `Then I should see the page title "Accessibility"` | `assertVisible` |  |
| `When I click back button on L2 page` | `pressKey` |  |
| `And I click back button on setting page` | `pressKey` |  |
| `Then I can see the new tab page` | `tapOn` |  |

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
- Replaced final Add New Tab action with the source NTP assertion on `Account menu`.
- Remaining execution risk: this scenario can vary by device because `Set as default browser` may open Android system Default apps instead of the Edge dialog.

