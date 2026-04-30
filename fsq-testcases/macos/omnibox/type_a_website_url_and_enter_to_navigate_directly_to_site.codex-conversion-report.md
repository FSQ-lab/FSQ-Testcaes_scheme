# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/ominibox/ominibox.feature`
- Feature: `ominibox`
- Scenario: `Type a website URL and enter to navigate directly to site`
- Tags: `@p0, @ominibox`

## Output

- Output YAML: `fsq-testcases/macos/omnibox/type_a_website_url_and_enter_to_navigate_directly_to_site.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `tapOn` | Converted from matched step implementation. |
| `When I input "www.163.com" in address bar` | `tapOn, inputText` | Converted from matched step implementation. |
| `And I press the "Enter" key` | `pressKey` | Converted from matched step implementation. |
| `Then "163" website should be opened` | `assertVisible` | Converted from matched step implementation. |
| `And the address bar should display the complete URL "https://www.163.com"` | `assertVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `Given Edge is launched` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/common/common.py:154` | operations=semantic/no direct tool call detected |
| `When I input "www.163.com" in address bar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/ominibox/ominibox.py:16` | operations=click_element, send_keys; locator={"accessibilityId": "Address and search bar"} |
| `And I press the "Enter" key` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/ominibox/ominibox.py:805` | operations=press_key |
| `Then "163" website should be opened` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/ominibox/ominibox.py:55` | operations=verify_element_exists; locator={"name": "网易"} |
| `And the address bar should display the complete URL "https://www.163.com"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/ominibox/ominibox.py:76` | operations=verify_element_exists; locator={"accessibilityId": "Address and search bar"} |

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
