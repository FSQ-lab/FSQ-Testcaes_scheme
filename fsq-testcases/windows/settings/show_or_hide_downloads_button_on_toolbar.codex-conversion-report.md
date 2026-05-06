# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/settings/settings.feature`
- Feature: `Settings`
- Scenario: `Show or hide Downloads button on toolbar`
- Tags: `@regression, @p0, @settings`

## Output

- Output YAML: `fsq-testcases/windows/settings/show_or_hide_downloads_button_on_toolbar.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I click "Settings and more" button on toolbar` | `tapOn` | Converted from matched step implementation. |
| `And I select "Settings" button from the dropdown menu` | `tapOn` | Converted from matched step implementation. |
| `Then the settings page should be opened` | `assertVisible` | Converted from matched step implementation. |
| `When I click "Appearance"` | `tapOn` | Converted from matched step implementation. |
| `And I click the option "Page zoom" button under "Appearance"` | `tapOn` | Converted from matched step implementation. |
| `And I click "Toolbar" in the webpage` | `tapOn` | Converted from matched step implementation. |
| `And I click on "Downloads" button on the settings page to turn it on` | `tapOn` | Converted from matched step implementation. |
| `Then the Downloads button should be visible on the toolbar` | `assertVisible` | Converted from matched step implementation. |
| `When I click on "Downloads" button on the settings page to turn it off` | `tapOn` | Converted from matched step implementation. |
| `Then the Downloads button should be hidden on the toolbar` | `assertNotVisible` | Converted from matched step implementation. |

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
| `When I click "Settings and more" button on toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:10` | operations=element_click; locator={"name": "Settings and more"} |
| `And I select "Settings" button from the dropdown menu` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:27` | operations=select_item; locator={"name": "Settings"} |
| `Then the settings page should be opened` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:44` | operations=verify_element_exists; locator={"name": "Settings"} |
| `When I click "Appearance"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:784` | operations=element_click; locator={"name": "Appearance"} |
| `And I click the option "Page zoom" button under "Appearance"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:1408` | operations=element_click; locator={"name": "Page zoom"} |
| `And I click "Toolbar" in the webpage` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:1425` | operations=element_click; locator={"name": "Toolbar"} |
| `And I click on "Downloads" button on the settings page to turn it on` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:1300` | operations=element_click; locator={"name": "Downloads"} |
| `Then the Downloads button should be visible on the toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:1279` | operations=verify_element_exists; locator={"name": "Downloads"} |
| `When I click on "Downloads" button on the settings page to turn it off` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:1317` | operations=element_click; locator={"name": "Downloads"} |
| `Then the Downloads button should be hidden on the toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/steps/settings/settings.py:1334` | operations=verify_element_not_exist; locator={"name": "Downloads"} |

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
