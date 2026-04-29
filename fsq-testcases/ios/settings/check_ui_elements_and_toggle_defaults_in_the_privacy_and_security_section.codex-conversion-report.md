# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_iOS/features/core/settings.feature`
- Feature: `settings`
- Scenario: `Check UI elements and toggle defaults in the "Privacy and Security" section`
- Tags: `@settings, @P0`

## Output

- Output YAML: `fsq-testcases/ios/settings/check_ui_elements_and_toggle_defaults_in_the_privacy_and_security_section.codex.yaml`
- Platform: `ios`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Implicit conversion assumption` | `launchApp` | iOS source scenarios commonly omit explicit launch step. |
| `When I navigate to the Settings page` | `tapOn, tapOn` |  |
| `And I navigate to the "Privacy and Security" section` | `tapOn` |  |
| `And I should see the element "Diagnostic Data"` | `assertVisible` |  |
| `And the toggle "Tracking Prevention" should be on by default` | `assertVisible` |  |
| `And the toggle "Protect InPrivate Tabs by Passcode" should be off by default` | `assertVisible` |  |
| `And the toggle "Microsoft Defender SmartScreen" should be on by default` | `assertVisible` |  |
| `And the toggle "Website Typo Protection" should be on by default` | `assertVisible` |  |
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
