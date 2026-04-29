# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/overflow_menu.feature`
- Feature: `overflow_menu`
- Scenario: `Complete all menu workflow through overflow menu on NTP`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/android/overflow_menu/complete_all_menu_workflow_through_overflow_menu_on_ntp.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I open the browser menu by tapping on the three dots icon at the bottom right corner` | `tapOn` |  |
| `And I swipe within the scrollable area on menu from right to left to go to the second page` | `tapOn` | I swipe within the scrollable area on menu from right to left to go to the second page |
| `And I tap "All Menu" from the menu` | `tapOn` |  |
| `Then the All Menu panel should open` | `tapOn` | the All Menu panel should open |
| `When I click "Edit" on All menu panel` | `tapOn` |  |
| `Then The All menu edit mode should be opened` | `tapOn` | The All menu edit mode should be opened |
| `And The "Favorites" is disabled` | `tapOn` | The "Favorites" is disabled |
| `When I click "Drop" icon` | `tapOn` |  |
| `And I click "Done" on All menu panel` | `tapOn` |  |
| `And I click back button on All menu panel` | `pressKey` |  |
| `And I open the browser menu by tapping on the three dots icon at the bottom right corner` | `tapOn` |  |
| `And I swipe within the scrollable area on menu from right to left to go to the second page` | `tapOn` | I swipe within the scrollable area on menu from right to left to go to the second page |
| `Then I should not see "Drop" on menu` | `assertNotVisible` |  |
| `When I tap "All Menu" from the menu` | `tapOn` |  |
| `And I click "Edit" on All menu panel` | `tapOn` |  |
| `And I scroll the page up slightly` | `swipe` |  |
| `And I click "Drop" icon` | `tapOn` |  |
| `And I click "Done" on All menu panel` | `tapOn` |  |
| `And I click back button on All menu panel` | `pressKey` |  |
| `And I open the browser menu by tapping on the three dots icon at the bottom right corner` | `tapOn` |  |
| `And I swipe within the scrollable area on menu from right to left to go to the second page` | `tapOn` | I swipe within the scrollable area on menu from right to left to go to the second page |
| `Then I should see "Drop" on menu` | `assertVisible` |  |

## Unresolved Or Low-Confidence Items

- I swipe within the scrollable area on menu from right to left to go to the second page
- the All Menu panel should open
- The All menu edit mode should be opened
- The "Favorites" is disabled
- I swipe within the scrollable area on menu from right to left to go to the second page
- I swipe within the scrollable area on menu from right to left to go to the second page

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
