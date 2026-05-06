# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/history/history.feature`
- Feature: `History`
- Scenario: `Search in new tab to add browsing history`
- Tags: `@p0`

## Output

- Output YAML: `fsq-testcases/windows/history/search_in_new_tab_to_add_browsing_history.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I input "https://www.cgtn.com" in address bar` | `tapOn` | Converted from matched step implementation. |
| `And I press "Enter" key` | `pressKey` | Converted from matched step implementation. |
| `Then the "cgtn" website should be opnened` | `assertVisible` | Converted from matched step implementation. |
| `When I press "Ctrl+H" to open history hub` | `pressKey` | Converted from matched step implementation. |
| `And I search "cgtn" in history hub` | `tapOn` | Converted from matched step implementation. |
| `Then the "cgtn" website should be displayed in the history hub` | `assertVisible` | Converted from matched step implementation. |

## BDD Execution Model

- Converted using the latest Codex FSQ Case Converter rule: feature scenario supplies intent and order; Behave step implementations supply executable operations, locators, assertions, waits, and helper behavior.
- Effective steps include Gherkin Background plus scenario steps when present.
- `features/steps/**/*.py` is treated as the global Behave step registry; matching is by exact or parameterized decorator before semantic fallback.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| `before_all` MCP startup | runner lifecycle / environment requirements | No | Starts pywinauto MCP and telemetry; keep out of case YAML. |
| Background `I launch Edge with empty user data directory` | setup/state guarantee | Partial | Represented by `launchApp`; temp user-data-dir creation is runner responsibility unless a dedicated command exists. |
| screenshot/telemetry hooks | runtime evidence | No | Failure screenshots, logs, and telemetry remain runner/evidence behavior. |

## Environment Requirements

- Windows Edge app available through the pywinauto MCP backend.
- Temporary user data directory setup from the Behave source is runner setup unless a dedicated DSL/runner method is provided.
- `native_navigate` source steps must be executed through the Windows runner contract, represented as `executeMethod: native_navigate`.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| Scenario steps | none or already reflected in Step Implementation Evidence | No unresolved `context.execute_steps()` expansion was identified during this report upgrade; any material setup/precondition is documented in Hook Normalization or Unresolved items. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `When I input "https://www.cgtn.com" in address bar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/common.py:79` | operations=enter_text |
| `And I press "Enter" key` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/history/history.py:91` | operations=send_keystrokes |
| `Then the "cgtn" website should be opnened` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/history/history.py:104` | operations=verify_element_exists; locator={"name": "CGTN"} |
| `When I press "Ctrl+H" to open history hub` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/history/history.py:121` | operations=send_keystrokes |
| `And I search "cgtn" in history hub` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/history/history.py:134` | operations=enter_text; locator={"name": "control"} |
| `Then the "cgtn" website should be displayed in the history hub` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/history/history.py:152` | operations=verify_element_exists; locator={"name": "CGTN"} |

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
