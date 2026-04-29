# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/settings.feature`
- Feature: `settings`
- Scenario: `Verify that each item in the third part is accessible and exitable`
- Tags: `@settings, @P0`

## Output

- Output YAML: `fsq-testcases/ios/settings/verify_that_each_item_in_the_third_part_is_accessible_and_exitable.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | iOS source scenarios commonly omit explicit launch step. |
| `When I navigate to the Settings page` | `tapOn, tapOn` |  |
| `And I swipe up to bottom of the page` | `swipe` |  |
| `Then analyze the screenshot to verify that settings page contains the following items3` | `assertWithAI` |  |
| `And I navigate to the "Languages" section` | `tapOn` |  |
| `Then I should see the page title "Languages"` | `assertVisible` |  |
| `And I click back button on the upper left corner` | `pressKey` |  |
| `And I navigate to the "Site Settings" section` | `tapOn` |  |
| `Then I should see the page title "Site Settings"` | `assertVisible` |  |
| `And I click back button on the upper left corner` | `pressKey` |  |
| `And I navigate to the "Notifications" section` | `tapOn` |  |
| `Then I should see the page title "Notifications"` | `assertVisible` |  |
| `And I click back button on the upper left corner` | `pressKey` |  |
| `And I navigate to the "About Microsoft Edge" section` | `tapOn` |  |
| `Then I should see the page title "About Microsoft Edge"` | `assertVisible` |  |
| `When I click on "Done" button on the top right corner` | `tapOn` |  |
| `Then I am landing on new tab page` | `assertVisible` |  |

## Unresolved Or Low-Confidence Items

- None

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
