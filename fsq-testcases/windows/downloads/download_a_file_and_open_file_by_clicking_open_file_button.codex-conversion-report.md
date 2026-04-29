# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/downloads/downloads.feature`
- Feature: `downloads`
- Scenario: `Download a file and open file by clicking Open file button`
- Tags: `@downloads, @regression, @p0`

## Output

- Output YAML: `fsq-testcases/windows/downloads/download_a_file_and_open_file_by_clicking_open_file_button.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I navigate to "https://getsamplefiles.com/download/pdf/sample-1.pdf"` | `tapOn, inputText, pressKey, waitUntil` | Conservative semantic conversion. |
| `Then the Downloads page should appear` | `assert/assertVisible/assertWithAI` | Conservative semantic conversion. |
| `When I click "Open file" for "sample-1.pdf"` | `tapOn` | Conservative semantic conversion. |
| `Then the downloaded file "sample-1.pdf" should be opened in a new tab` | `assert/assertVisible/assertWithAI` | Conservative semantic conversion. |

## Unresolved Or Low-Confidence Items

- Confirm Windows accessibility names against pywinauto MCP tree during first execution.

## Conversion Rules Applied

- Windows cases use `runner.backend: pywinauto-mcp` and Edge app metadata.
- Known address bar interactions use `name: Address and search bar` with `controlType: Edit`.
- Unknown UI targets are preserved as semantic `target` descriptions for accessibility-tree locator resolution.
- Screenshot/visual validation steps are represented as blocking `assertWithAI`; no visual coordinate fallback was generated.
- No coordinates were generated.

## Manual Review Checklist

- Confirm Edge executable path matches the runner machine.
- Confirm target wording is specific enough for accessibility-tree locator resolution.
- Add stable Windows locators from knowledge base when available.
- Confirm every assertion should remain blocking.
