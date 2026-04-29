# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/search_bottom_mode.feature`
- Feature: `search_bottom_mode`
- Scenario: `Verify Bottom address bar on NTP`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/ios/search_bottom_mode/verify_bottom_address_bar_on_ntp.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | iOS source scenarios commonly omit explicit launch step. |
| `When I click + button on the bottom toolbar` | `tapOn` |  |
| `When I change the NTP page layout to Partial view` | `tapOn` | I change the NTP page layout to Partial view |
| `And I close the Page settings dialog` | `tapOn` |  |
| `And I scroll feeds up for 3 seconds` | `swipe` |  |
| `Then I should see the omnibox with Copilot icon and Copilot voice icon` | `assertVisible` |  |
| `When I scroll feeds down for 3 seconds` | `swipe` |  |
| `Then I should see the omnibox with Copilot icon and Copilot voice icon` | `assertVisible` |  |
| `When I change the NTP page layout to Headings view` | `tapOn` | I change the NTP page layout to Headings view |
| `And I close the Page settings dialog` | `tapOn` |  |
| `And I scroll feeds up for 3 seconds` | `swipe` |  |
| `Then I should see the omnibox with Copilot icon and Copilot voice icon` | `assertVisible` |  |
| `When I scroll feeds down for 3 seconds` | `swipe` |  |
| `Then I should see the omnibox with Copilot icon and Copilot voice icon` | `assertVisible` |  |

## Unresolved Or Low-Confidence Items

- I change the NTP page layout to Partial view
- I change the NTP page layout to Headings view

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
