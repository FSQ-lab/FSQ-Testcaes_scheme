# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/tab/tab.feature`
- Feature: `tab`
- Scenario: `Refresh in horizontal mode`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/macos/tab/refresh_in_horizontal_mode.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `tapOn` | Converted from matched step implementation. |
| `When I navigate to "https://www.youtube.com"` | `tapOn, inputText, pressKey, tapOn` | Converted from matched step implementation. |
| `And I right click on the tab header of "Youtube" tab` | `tapOn` | Converted from matched step implementation. |
| `And I click "Refresh" from the context menu` | `tapOn, tapOn` | Converted from matched step implementation. |
| `Then the page should be refreshed` | `assertVisible` | Converted from matched step implementation. |
| `And the address bar still displays the complete URL "https://www.youtube.com"` | `assertVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `Given Edge is launched` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/common/common.py:154` | operations=semantic/no direct tool call detected |
| `When I navigate to "https://www.youtube.com"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/tab/tab.py:228` | operations=click_element, send_keys, press_key, click_element; locator={"accessibilityId": "Address and search bar"} |
| `And I right click on the tab header of "Youtube" tab` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/tab/tab.py:300` | operations=right_click_element; locator={"xpath": "//XCUIElementTypeTab[@label='YouTube']"} |
| `And I click "Refresh" from the context menu` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/tab/tab.py:321` | operations=click_element, click_element; locator={"xpath": "//XCUIElementTypeMenuItem[@title='Refresh']"} |
| `Then the page should be refreshed` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/tab/tab.py:359` | operations=verify_element_exists; locator={"xpath": "//XCUIElementTypeStaticText[@value='Try searching to get started']"} |
| `And the address bar still displays the complete URL "https://www.youtube.com"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/tab/tab.py:380` | operations=verify_element_exists; locator={"xpath": "//XCUIElementTypeTextField[@label='Address and search bar' and @value='https://www.youtube.com']"} |

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
