# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/downloads/downloads.feature`
- Feature: `Downloads`
- Scenario: `Download a file and open file by clicking Open file button`
- Tags: `@downloads, @regression, @P0`

## Output

- Output YAML: `fsq-testcases/windows/downloads/download_a_file_and_open_file_by_clicking_open_file_button.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given I launch Edge with empty user data directory` | `tapOn` | Converted from matched step implementation. |
| `When I navigate to "https://getsamplefiles.com/download/pdf/sample-1.pdf"` | `executeMethod: native_navigate` | Preserves Windows pywinauto MCP `native_navigate` source operation. |
| `Then the Downloads page should appear` | `assertWithAI` | Converted from matched step implementation. |
| `When I click "Open file" for "sample-1.pdf"` | `tapOn` | Converted from matched step implementation. |
| `Then the downloaded file "sample-1.pdf" should be opened in a new tab` | `assertVisible` | Converted from matched step implementation. |

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
| `Given I launch Edge with empty user data directory` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/common.py:27` | operations=app_launch |
| `When I navigate to "https://getsamplefiles.com/download/pdf/sample-1.pdf"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/common.py:48` | operations=native_navigate |
| `Then the Downloads page should appear` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/downloads/downloads.py:314` | operations=verify_visual_task |
| `When I click "Open file" for "sample-1.pdf"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/downloads/downloads.py:1154` | operations=element_click; locator={"name": "sample-1.pdf"} |
| `Then the downloaded file "sample-1.pdf" should be opened in a new tab` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/downloads/downloads.py:1132` | operations=verify_element_exists; locator={"name": "sample-1.pdf"} |

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
