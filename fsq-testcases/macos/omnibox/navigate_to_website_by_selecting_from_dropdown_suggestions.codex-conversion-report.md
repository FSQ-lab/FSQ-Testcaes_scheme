# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/ominibox/ominibox.feature`
- Feature: `ominibox`
- Scenario: `Navigate to website by selecting from dropdown suggestions`
- Tags: `@p0, @ominibox`

## Output

- Output YAML: `fsq-testcases/macos/omnibox/navigate_to_website_by_selecting_from_dropdown_suggestions.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `tapOn` | Converted from matched step implementation. |
| `And I open a new tab` | `tapOn` | Converted from matched step implementation. |
| `When I type "www.apple.com" in the address bar` | `tapOn, inputText` | Converted from matched step implementation. |
| `Then a dropdown list should appear with URL suggestions` | `assertVisible` | Converted from matched step implementation. |
| `When I click the top item "www.apple.com" in the dropdown list` | `tapOn` | Converted from matched step implementation. |
| `Then I should navigate to "https://www.apple.com" successfully` | `assertVisible` | Converted from matched step implementation. |
| `And the address bar should display the complete URL "https://www.apple.com"` | `assertVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `Given Edge is launched` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/common/common.py:154` | operations=semantic/no direct tool call detected |
| `And I open a new tab` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/ominibox/ominibox.py:97` | operations=click_element; locator={"accessibilityId": "New Tab"} |
| `When I type "www.apple.com" in the address bar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/ominibox/ominibox.py:378` | operations=click_element, send_keys; locator={"accessibilityId": "Address and search bar"} |
| `Then a dropdown list should appear with URL suggestions` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/ominibox/ominibox.py:417` | operations=verify_element_exists; locator={"accessibilityId": "Suggestions"} |
| `When I click the top item "www.apple.com" in the dropdown list` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/ominibox/ominibox.py:767` | operations=click_element; locator={"xpath": "//XCUIElementTypeStaticText[@value=\"www.apple.com\" and "} |
| `Then I should navigate to "https://www.apple.com" successfully` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/ominibox/ominibox.py:217` | operations=verify_element_exists; locator={"accessibilityId": "Address and search bar"} |
| `And the address bar should display the complete URL "https://www.apple.com"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/ominibox/ominibox.py:357` | operations=verify_element_exists; locator={"xpath": "//XCUIElementTypeTextField[@label='Address and search bar' and @value='https://www.apple.com']"} |

## Unresolved Or Low-Confidence Items

- None

## Conversion Rules Applied

- Applied Codex dual-source conversion: feature scenario for intent/order and Behave step implementation for executable operations.
- Preserved source locators from Appium/pywinauto step definitions where available.
- Preserved URL/current-page checks as locator-backed element assertions when source code verifies UI state.
- Converted screenshot/visual checks to blocking `assertWithAI` assertions instead of coordinate fallback.
- Every case starts with `launchApp` and ends with `killApp` for isolated runs.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm app identity and runner backend match the target execution environment.
- Confirm semantic targets remain specific enough for accessibility-tree locator resolution.
- Confirm any unresolved source steps before using this case for gating.
- Confirm visual assertions are run with a vision-capable analysis path.
