# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/settings/settings.feature`
- Feature: `Settings functionality`
- Scenario: `Cancel add custom site`
- Tags: `@regression, @p0, @settings`

## Output

- Output YAML: `fsq-testcases/macos/settings/cancel_add_custom_site.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `tapOn` | Converted from matched step implementation. |
| `And I input "edge://settings/startHomeNTP" to the address bar` | `tapOn, inputText, pressKey` | Converted from matched step implementation. |
| `When I select the option "Open custom sites"` | `tapOn` | Converted from matched step implementation. |
| `And I click the "Add site" button` | `tapOn` | Converted from matched step implementation. |
| `Then the "Add site" dialog should be opened` | `assertVisible` | Converted from matched step implementation. |
| `When I input "https://www.bing.com" in the URL field on the "Add site" dialog` | `tapOn, tapOn, inputText, inputText` | Converted from matched step implementation. |
| `And I click the "Cancel" button on the "Add site" dialog` | `tapOn` | Converted from matched step implementation. |
| `Then the "Add site" dialog should be closed` | `assertNotVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `Given Edge is launched` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/common/common.py:154` | operations=semantic/no direct tool call detected |
| `And I input "edge://settings/startHomeNTP" to the address bar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:321` | operations=click_element, send_keys, press_key; locator={"accessibilityId": "Address and search bar"} |
| `When I select the option "Open custom sites"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:697` | operations=find_element, click_element; locator={"name": "Open custom sites"} |
| `And I click the "Add site" button` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:453` | operations=click_element; locator={"accessibilityId": "Add site"} |
| `Then the "Add site" dialog should be opened` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:474` | operations=verify_element_exists; locator={"accessibilityId": "Website"} |
| `When I input "https://www.bing.com" in the URL field on the "Add site" dialog` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:537` | operations=click_element, click_element, send_keys, send_keys; locator={"xpath": "(//XCUIElementTypeGroup[@label=\"Website\"])"} |
| `And I click the "Cancel" button on the "Add site" dialog` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:676` | operations=click_element; locator={"name": "Cancel"} |
| `Then the "Add site" dialog should be closed` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:634` | operations=verify_element_not_exists; locator={"xpath": "//XCUIElementTypeTextField[@title=\"Website\"]"} |

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
