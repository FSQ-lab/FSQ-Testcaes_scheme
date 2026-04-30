# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/download/download.feature`
- Feature: `Download functionality in Microsoft Edge`
- Scenario: `Download a file and open downloads finder`
- Tags: `@p0, @regression, @download`

## Output

- Output YAML: `fsq-testcases/macos/download/download_a_file_and_open_downloads_finder.codex.yaml`
- Platform: `macos`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `Given Edge is launched` | `tapOn` | Converted from matched step implementation. |
| `And I clean Edge downloads file "sample-1.pdf"` | `tapOn` | Converted from matched step implementation. |
| `When I navigate to "https://getsamplefiles.com/download/pdf/sample-1.pdf"` | `tapOn, inputText, pressKey` | Converted from matched step implementation. |
| `Then the Downloads panel should appear` | `assertVisible` | Converted from matched step implementation. |
| `When I click "Search downloads" in Downloads panel` | `tapOn` | Converted from matched step implementation. |
| `And I hover over the file name containing "sample-1" in the Downloads panel` | `tapOn` | Converted from matched step implementation. |
| `And I click the "Show in Finder" button` | `tapOn` | Converted from matched step implementation. |
| `Then Analyze the screenshot to verify the Finder window should appear` | `assertWithAI` | Converted from matched step implementation. |
| `And Analyze the screenshot to verify that the file "sample-1.pdf" is present in the Finder window` | `assertWithAI` | Converted from matched step implementation. |

## Step Implementation Evidence

| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
| `Given Edge is launched` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/common/common.py:154` | operations=semantic/no direct tool call detected |
| `And I clean Edge downloads file "sample-1.pdf"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/common/common.py:289` | operations=semantic/no direct tool call detected |
| `When I navigate to "https://getsamplefiles.com/download/pdf/sample-1.pdf"` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/download/download.py:9` | operations=click_element, send_keys, press_key; locator={"accessibilityId": "Address and search bar"} |
| `Then the Downloads panel should appear` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/download/download.py:64` | operations=verify_element_exists; locator={"accessibilityId": "Downloads"} |
| `When I click "Search downloads" in Downloads panel` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/download/download.py:85` | operations=click_element; locator={"accessibilityId": "Search downloads"} |
| `And I hover over the file name containing "sample-1" in the Downloads panel` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/download/download.py:106` | operations=mouse_hover; locator={"xpath": "//XCUIElementTypeStaticText[contains(@value, 'sample-1')]"} |
| `And I click the "Show in Finder" button` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/download/download.py:923` | operations=click_element; locator={"accessibilityId": "Show in Finder"} |
| `Then Analyze the screenshot to verify the Finder window should appear` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/download/download.py:1007` | operations=verify_visual_task |
| `And Analyze the screenshot to verify that the file "sample-1.pdf" is present in the Finder window` | `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/steps/download/download.py:1020` | operations=verify_visual_task |

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
