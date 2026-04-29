# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/tab_center.feature`
- Feature: `tab_center`
- Scenario: `Add new tab by clicking 'add new tab' button in bottom bar`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/ios/tab_center/add_new_tab_by_clicking_add_new_tab_button_in_bottom_bar.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | iOS source scenarios commonly omit explicit launch step. |
| `When I enter tab center by clicking on the tab center icon` | `tapOn` | I enter tab center by clicking on the tab center icon |
| `And I click "Edit" button on tab center page` | `tapOn` |  |
| `And I click "Close all tabs and groups" on menu` | `tapOn` |  |
| `And I click tab grid add button in tab center` | `tapOn` | I click tab grid add button in tab center |
| `Then I should return to new tab page` | `tapOn` | I should return to new tab page |
| `When I click on the search box on NTP page` | `tapOn` |  |
| `And I input "https://www.microsoft.com" in search box and navigate to it` | `inputText` |  |
| `Then I should see "1" on the tab center icon` | `assertVisible` |  |
| `When I click on new tab button to open a new tab` | `tapOn` | I click on new tab button to open a new tab |
| `Then I should return to new tab page` | `tapOn` | I should return to new tab page |
| `Then I should see "2" on the tab center icon` | `assertVisible` |  |

## Unresolved Or Low-Confidence Items

- I enter tab center by clicking on the tab center icon
- I click tab grid add button in tab center
- I should return to new tab page
- I click on new tab button to open a new tab
- I should return to new tab page

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
