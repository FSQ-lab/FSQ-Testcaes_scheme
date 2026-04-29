# Conversion Report

Codex-produced conversion report.

## Source

- Source repo: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows`
- Source feature: `/Users/qunmi/Documents/MS_ADO/FSQ_AI_TestCases_Windows/features/core_address_bar/core_address_bar.feature`
- Feature: `core_address_bar`
- Scenario: `Navigate to HTTPS website and verify secure connection`
- Tags: `@navigation, @regression, @p0`

## Output

- Output YAML: `fsq-testcases/windows/core_address_bar/navigate_to_https_website_and_verify_secure_connection.codex.yaml`
- Platform: `windows`
- Schema target: `docs/codex-fsq-ai-test-dsl-v1.schema.json`
- Review status: `draft`

## Step Mapping

| Source step | FSQ command | Notes |
| --- | --- | --- |
| `When I input "https://www.apple.com" in address bar` | `tapOn, inputText, pressKey, waitUntil` | Conservative semantic conversion. |
| `And I press the "Enter" key` | `pressKey` | Conservative semantic conversion. |
| `Then I should navigate to "Apple" page successfully` | `tapOn, inputText, pressKey, waitUntil` | Conservative semantic conversion. |
| `And the security indicator should show a secure connection` | `assert/assertVisible/assertWithAI` | Conservative semantic conversion. |

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
