# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android/features/core/settings.feature`
- Feature: `settings`
- Scenario: `Verify that each item in the first part of L1 page is accessible`
- Tags: `@P0`

## Output

- Output YAML: `fsq-testcases/android/settings/verify_that_each_item_in_the_first_part_of_l1_page_is_accessible.codex.yaml`
- Platform: `android`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | Android source scenarios commonly omit explicit launch step. |
| `When I open browser menu` | `tapOn` |  |
| `And I click on "Settings" button` | `tapOn` |  |
| `And I navigate to the "Password Manager" section` | `tapOn` |  |
| `Then I should see the page title "Microsoft Password Manager"` | `assertVisible` |  |
| `When I close the "Microsoft Password Manager" page` | `pressKey` |  |
| `And I navigate to the "Payment Methods" section` | `tapOn` |  |
| `Then I should see the page title "Payment Methods"` | `assertVisible` |  |
| `When I click back button on L2 page` | `pressKey` |  |
| `And I navigate to the "Personal Info" section` | `tapOn` |  |
| `Then I should see the page title "Personal Info"` | `assertVisible` |  |
| `When I click back button on L2 page` | `pressKey` |  |
| `And I navigate to the "Privacy and Security" section` | `tapOn` |  |
| `Then I should see the page title "Privacy and Security"` | `assertVisible` |  |
| `When I click back button on L2 page` | `pressKey` |  |
| `And I navigate to the "Microsoft Services" section` | `tapOn` |  |
| `Then I should see the page title "Microsoft Services"` | `assertVisible` |  |
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
- Replaced final Add New Tab action with the source NTP assertion on `Account menu`.
- Kept all settings section/page title assertions locator-backed from source step definitions.

