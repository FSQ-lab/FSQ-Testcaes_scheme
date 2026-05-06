# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/settings/settings.feature`
- Feature: `Settings functionality`
- Scenario: `Set custom site as home page`
- Tags: `@settings, @smoke, @p0`

## Output

- Output YAML: `fsq-testcases/macos/settings/set_custom_site_as_home_page.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `launchApp` | Converted from launch helper; temp profile setup remains runner-owned. |
| `And I input "edge://settings/startHomeNTP" to the address bar` | `tapOn, inputText, pressKey` | Converted from matched step implementation. |
| `When I turn on the option "show home button on the toolbar"` | `tapOn` | Converted from matched step implementation. |
| `And I select the option "Set custom site"` | `tapOn` | Converted from matched step implementation. |
| `Then the input box under "Set custom site" can be clicked` | `tapOn` | Converted from matched step implementation. |
| `When I input "https://www.apple.com" to the input box` | `inputText` | Converted from matched step implementation. |
| `And I select the option "Set custom site"` | `tapOn` | Converted from matched step implementation. |
| `And I click "Home" button to the left of the address bar` | `tapOn` | Converted from matched step implementation. |
| `Then should open "https://www.apple.com" site` | `assert` | Converted from matched step implementation. |

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
| `And I input "edge://settings/startHomeNTP" to the address bar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:321` | operations=click_element, send_keys, press_key; locator={"accessibilityId": "Address and search bar"} |
| `When I turn on the option "show home button on the toolbar"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:1262` | operations=click_element; locator={"accessibilityId": "Show home button on the toolbar"} |
| `And I select the option "Set custom site"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:1283` | operations=click_element; locator={"accessibilityId": "Set custom site"} |
| `Then the input box under "Set custom site" can be clicked` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:1371` | operations=click_element; locator={"accessibilityId": "Enter URL"} |
| `When I input "https://www.apple.com" to the input box` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:1304` | operations=send_keys; locator={"accessibilityId": "Enter URL"} |
| `And I select the option "Set custom site"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:1283` | operations=click_element; locator={"accessibilityId": "Set custom site"} |
| `And I click "Home" button to the left of the address bar` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:1326` | operations=click_element; locator={"accessibilityId": "Home"} |
| `Then should open "https://www.apple.com" site` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/settings/settings.py:1347` | operations=verify_element_attribute; locator={"accessibilityId": "Address and search bar"} |

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
