# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/settings/settings.feature`
- Feature: `Settings functionality`
- Scenario: `Search in settings search box`
- Tags: `@regression, @p0, @settings`

## Output

- Output YAML: `fsq-testcases/macos/settings/search_in_settings_search_box.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `tapOn` | Converted from matched step implementation. |
| `When I click "Settings and more" button on toolbar` | `tapOn` | Converted from matched step implementation. |
| `And I select "Settings" button from the dropdown menu` | `tapOn` | Converted from matched step implementation. |
| `Then the settings page should be opened` | `assertVisible` | Converted from matched step implementation. |
| `When I input "Privacy" in the settings search box` | `inputText, inputText` | Converted from matched step implementation. |
| `Then the search results should display relevant settings related to "Privacy"` | `assertVisible` | Converted from matched step implementation. |
| `When I clear the search box` | `tapOn` | Converted from matched step implementation. |
| `Then the search results should reset to show all settings` | `assertVisible` | Converted from matched step implementation. |
| `When I input "123" in the settings search box` | `inputText, inputText` | Converted from matched step implementation. |
| `Then the search results should display "No search results found"` | `tapOn` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `Given Edge is launched` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/common/common.py:154` | operations=semantic/no direct tool call detected |
| `When I click "Settings and more" button on toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:12` | operations=click_element; locator={"accessibilityId": "Settings and more"} |
| `And I select "Settings" button from the dropdown menu` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:33` | operations=click_element; locator={"accessibilityId": "Settings ⌘Comma ⌘Comma"} |
| `Then the settings page should be opened` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:54` | operations=verify_element_exists; locator={"accessibilityId": "Settings"} |
| `When I input "Privacy" in the settings search box` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:75` | operations=send_keys, send_keys; locator={"xpath": "//XCUIElementTypeTextField[@placeholderValue='Search settings']"} |
| `Then the search results should display relevant settings related to "Privacy"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:128` | operations=verify_element_exists; locator={"accessibilityId": "Privacy, search, and services"} |
| `When I clear the search box` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:149` | operations=click_element; locator={"accessibilityId": "Clear search"} |
| `Then the search results should reset to show all settings` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:170` | operations=verify_element_exists; locator={"accessibilityId": "Top settings"} |
| `When I input "123" in the settings search box` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:191` | operations=send_keys, send_keys; locator={"xpath": "//XCUIElementTypeTextField[@placeholderValue='Search settings']"} |
| `Then the search results should display "No search results found"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:240` | operations=find_element; locator={"accessibilityId": "No search results found"} |

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
