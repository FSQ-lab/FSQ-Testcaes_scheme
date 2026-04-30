# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/history/history.feature`
- Feature: `History`
- Scenario: `Click the History button on toolbar to open History pane`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/windows/history/click_the_history_button_on_toolbar_to_open_history_pane.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I click "···" button in toolbar` | `tapOn` | Converted from matched step implementation. |
| `And I right click "History" button in the menu` | `rightClickOn` | Converted from matched step implementation. |
| `And I click "Show in toolbar" in menu` | `tapOn` | Converted from matched step implementation. |
| `Then the History button should be displayed in the toolbar` | `assertVisible` | Converted from matched step implementation. |
| `When I click "History" button in the toolbar` | `tapOn` | Converted from matched step implementation. |
| `Then the "history hub" should be displayed` | `assertVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I click "···" button in toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/history/history.py:22` | operations=element_click; locator={"name": "Settings and more (Alt+F)"} |
| `And I right click "History" button in the menu` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/history/history.py:39` | operations=right_click; locator={"name": "History Ctrl+H"} |
| `And I click "Show in toolbar" in menu` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/history/history.py:56` | operations=element_click; locator={"name": "Show in toolbar"} |
| `Then the History button should be displayed in the toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/history/history.py:73` | operations=verify_element_exists; locator={"name": "History"} |
| `When I click "History" button in the toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/history/history.py:169` | operations=element_click; locator={"name": "History"} |
| `Then the "history hub" should be displayed` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/history/history.py:186` | operations=verify_element_exists; locator={"name": "History"} |

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
