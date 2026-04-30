# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/tab/tab.feature`
- Feature: `tab`
- Scenario: `Close a tab in horizontal mode`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/macos/tab/close_a_tab_in_horizontal_mode.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `tapOn` | Converted from matched step implementation. |
| `When I new a tab and navigate to "https://www.apple.com"` | `tapOn, tapOn, inputText, pressKey` | Converted from matched step implementation. |
| `And I click the "Close Tab" button on tab header` | `tapOn` | Converted from matched step implementation. |
| `Then the "Apple" tab should be closed` | `assertNotVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `Given Edge is launched` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/common/common.py:154` | operations=semantic/no direct tool call detected |
| `When I new a tab and navigate to "https://www.apple.com"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/tab/tab.py:8` | operations=click_element, click_element, send_keys, press_key, app_state, find_element; locator={"xpath": "//XCUIElementTypeButton[@label='New Tab']"} |
| `And I click the "Close Tab" button on tab header` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/tab/tab.py:114` | operations=click_element, app_state; locator={"xpath": "//XCUIElementTypeTab[@label='Apple' and @selected='true']//XCUIElementTypeButton[@label='Close tab']"} |
| `Then the "Apple" tab should be closed` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/tab/tab.py:152` | operations=verify_element_not_exists; locator={"xpath": "//XCUIElementTypeTab[@label='Apple']"} |

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
