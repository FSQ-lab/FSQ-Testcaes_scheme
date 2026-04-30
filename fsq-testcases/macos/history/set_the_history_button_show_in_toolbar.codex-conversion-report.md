# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/history/history.feature`
- Feature: `History functionality in Microsoft Edge`
- Scenario: `Set the History button show in toolbar`
- Tags: `@p0, @regression, @history`

## Output

- Output YAML: `fsq-testcases/macos/history/set_the_history_button_show_in_toolbar.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `tapOn` | Converted from matched step implementation. |
| `When I click "Settings and more" button in toolbar` | `tapOn` | Converted from matched step implementation. |
| `And I right click "History" button in menu` | `tapOn` | Converted from matched step implementation. |
| `And I click "Show in toolbar" in menu` | `tapOn` | Converted from matched step implementation. |
| `Then "History" should be displayed in toolbar` | `assertVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `Given Edge is launched` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/common/common.py:154` | operations=semantic/no direct tool call detected |
| `When I click "Settings and more" button in toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/history/history.py:67` | operations=click_element; locator={"accessibilityId": "Settings and more"} |
| `And I right click "History" button in menu` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/history/history.py:186` | operations=right_click_element; locator={"accessibilityId": "History ⌘Y ⌘Y"} |
| `And I click "Show in toolbar" in menu` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/history/history.py:207` | operations=click_element; locator={"accessibilityId": "Show in Toolbar"} |
| `Then "History" should be displayed in toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/history/history.py:228` | operations=verify_element_exists; locator={"accessibilityId": "History"} |

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
