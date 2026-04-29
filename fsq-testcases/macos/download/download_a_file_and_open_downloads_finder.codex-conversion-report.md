# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac/features/download/download.feature`
- Feature: `download`
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
| `Given Edge is launched` | `launchApp` |  |
| `And I clean Edge downloads file "sample-1.pdf"` | `tapOn` | I clean Edge downloads file "sample-1.pdf" |
| `When I navigate to "https://getsamplefiles.com/download/pdf/sample-1.pdf"` | `tapOn, inputText, pressKey` |  |
| `Then the Downloads panel should appear` | `assertVisible` | the Downloads panel should appear |
| `When I click "Search downloads" in Downloads panel` | `tapOn` | I click "Search downloads" in Downloads panel |
| `And I hover over the file name containing "sample-1" in the Downloads panel` | `tapOn` | I hover over the file name containing "sample-1" in the Downloads panel |
| `And I click the "Show in Finder" button` | `tapOn` | I click the "Show in Finder" button |
| `Then Analyze the screenshot to verify the Finder window should appear` | `tapOn` | Analyze the screenshot to verify the Finder window should appear |
| `And Analyze the screenshot to verify that the file "sample-1.pdf" is present in the Finder window` | `tapOn` | Analyze the screenshot to verify that the file "sample-1.pdf" is present in the Finder window |

## Unresolved Or Low-Confidence Items

- I clean Edge downloads file "sample-1.pdf"
- the Downloads panel should appear
- I click "Search downloads" in Downloads panel
- I hover over the file name containing "sample-1" in the Downloads panel
- I click the "Show in Finder" button
- Analyze the screenshot to verify the Finder window should appear
- Analyze the screenshot to verify that the file "sample-1.pdf" is present in the Finder window

## Conversion Rules Applied

- Known address bar interactions use `accessibilityId: Address and search bar`.
- Unknown UI targets are preserved as semantic `target` descriptions.
- Relation locators are used only when the source step explicitly provides context.
- No coordinates were generated.
- No screenshot-based coordinate guessing was used.

## Manual Review Checklist

- Confirm `appId: com.microsoft.edgemac` matches the runner environment.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Add stable locators from knowledge base when available.
- Confirm every assertion should remain blocking.
