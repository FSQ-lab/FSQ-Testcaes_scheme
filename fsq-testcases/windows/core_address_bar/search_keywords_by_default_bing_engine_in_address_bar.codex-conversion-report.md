# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/core_address_bar/core_address_bar.feature`
- Feature: `Core Address Bar`
- Scenario: `Search keywords by default Bing engine in address bar`
- Tags: `@search, @smoke, @p0`

## Output

- Output YAML: `fsq-testcases/windows/core_address_bar/search_keywords_by_default_bing_engine_in_address_bar.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I input "cat" in address bar` | `tapOn` | Converted from matched step implementation. |
| `And I press the "Enter" key` | `pressKey` | Converted from matched step implementation. |
| `Then the tab should jump to the search results page related to "cat"` | `assertVisible` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I input "cat" in address bar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/common.py:79` | operations=enter_text |
| `And I press the "Enter" key` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/core_address_bar/core_address_bar.py:9` | operations=send_keystrokes |
| `Then the tab should jump to the search results page related to "cat"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/core_address_bar/core_address_bar.py:71` | operations=verify_element_exists; locator={"name": "cat - Search"} |

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
