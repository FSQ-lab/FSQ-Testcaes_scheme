# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/settings/settings.feature`
- Feature: `Settings functionality`
- Scenario: `Show/hide Split screen button`
- Tags: `@regression, @p0, @settings`

## Output

- Output YAML: `fsq-testcases/macos/settings/show_hide_split_screen_button.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `launchApp` | Converted from launch helper; temp profile setup remains runner-owned. |
| `And I input "edge://settings/appearance/toolbar" to the address bar` | `tapOn, inputText, pressKey` | Converted from matched step implementation. |
| `When I click on "Split screen" button switch in Toolbar Settings page` | `tapOn` | Converted from matched step implementation. |
| `Then the Split screen button should be visible on the toolbar` | `assertVisible` | Converted from matched step implementation. |
| `When I click on "Split screen" button switch in Toolbar Settings page` | `tapOn` | Converted from matched step implementation. |
| `Then the Split screen button should be hidden on the toolbar` | `assertNotVisible` | Converted from matched step implementation. |

## BDD Execution Model

- Converted using the latest Codex FSQ Case Converter rule: feature scenario supplies intent and order; Behave step implementations supply executable operations, locators, assertions, waits, and helper behavior.
- Effective steps include Gherkin Background plus scenario steps when present.
- `features/steps/**/*.py` is treated as the global Behave step registry; matching is by exact or parameterized decorator before semantic fallback.

## Hook Normalization
| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |
| `Edge is launched` helper | setup/state guarantee | Partial | Converted to `launchApp`; temp profile arguments and system-dialog handling remain runner setup requirements. |
| environment/MCP startup | runner lifecycle | No | Appium/MCP session creation belongs to runner. |
| screenshot/log/report hooks | runtime evidence | No | Evidence collection is not encoded in case YAML. |

## Environment Requirements

- macOS Edge app installed and launchable with the Appium 3.x MCP runner.
- Source temp-profile setup and macOS system dialog handling are runner setup requirements.
- External downloads, account state, or filesystem cleanup are unresolved unless a safe runner command exists.

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
| Scenario steps | none or already reflected in Step Implementation Evidence | No unresolved `context.execute_steps()` expansion was identified during this report upgrade; any material setup/precondition is documented in Hook Normalization or Unresolved items. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `Given Edge is launched` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/common/common.py:154` | operations=app_launch via launch_edge_implementation; temp profile setup runner-owned |
| `And I input "edge://settings/appearance/toolbar" to the address bar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:376` | operations=click_element, send_keys, press_key; locator={"xpath": "//XCUIElementTypeTextField[@label=\"Address and search bar\"]"} |
| `When I click on "Split screen" button switch in Toolbar Settings page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:912` | operations=find_element, click_element; locator={"xpath": "//XCUIElementTypeSwitch[@label='Split screen']"} |
| `Then the Split screen button should be visible on the toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:950` | operations=verify_element_exists; locator={"xpath": "//XCUIElementTypeButton[@label='Split screen']"} |
| `When I click on "Split screen" button switch in Toolbar Settings page` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:912` | operations=find_element, click_element; locator={"xpath": "//XCUIElementTypeSwitch[@label='Split screen']"} |
| `Then the Split screen button should be hidden on the toolbar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:971` | operations=verify_element_not_exists; locator={"xpath": "//XCUIElementTypeButton[@label='Split screen']"} |

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
