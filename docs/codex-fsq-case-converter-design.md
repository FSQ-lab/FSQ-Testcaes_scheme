# FSQ Case Converter Codex Design

> Codex-produced artifact. This document defines the scope and contract for a manual or semi-automated tool that converts existing test cases into FSQ AI Test DSL v1.

## 1. Goal

The converter helps a human or AI agent transform existing case descriptions into FSQ v1 YAML drafts. It is not part of the core testcase DSL, and it must not write conversion metadata into the final testcase YAML.

The converter should produce reviewable drafts, not silently finalized test cases.

## 2. Non-Goals

- Do not convert BDD/Gherkin as a special first-class format in v1.
- Do not infer coordinates from screenshots in non-vision mode.
- Do not weaken assertions to make conversion pass.
- Do not embed evidence, repair, or conversion reports in testcase YAML.
- Do not generate executor-specific code such as Appium Python, JavaScript, or pywinauto calls.

## 3. Inputs

The v1 converter accepts one source case at a time.

Recommended input types:

```text
plain text steps
markdown case description
legacy YAML-like action lists
Maestro-like YAML flows
JSON case descriptions
```

Optional context inputs:

```text
target platform
app identity
known stable locators
accessibility tree snapshot
project env defaults
conversion policy
```

The converter should work without an accessibility tree, but it must then avoid pretending uncertain locator data is known.

## 4. Outputs

The converter produces two separate artifacts.

### FSQ YAML Draft

The main output is an FSQ v1 testcase draft.

```yaml
schemaVersion: fsq.ai-test/v1
name: Converted login case
platform: windows
app:
  name: edge
---
- launchApp
- tapOn:
    target: "Username input field"
- inputText:
    text: "alice@example.com"
    target: "Username input field"
- inputText:
    text: "123456"
    target: "Password input field"
    locator:
      text: "Password"
      below:
        text: "Username"
- tapOn:
    target: "Sign in button"
- assertVisible:
    target: "Home page"
```

### Conversion Report

The report is separate from the testcase YAML.

Recommended filename pattern:

```text
<case-name>.codex-conversion-report.md
```

The report should include:

- source file path or source label
- conversion timestamp
- assumptions
- unresolved targets
- locator confidence notes
- validation result
- manual review checklist

## 5. Conversion Pipeline

```text
Load source case
  -> parse into source steps
  -> classify each step as lifecycle / action / assertion / wait / flow
  -> normalize to FSQ command draft
  -> attach target / locator / relation constraints when justified
  -> validate normalized model with codex-fsq-ai-test-dsl-v1.schema.json
  -> emit YAML draft and conversion report
```

The converter should fail loudly when it cannot preserve intent. It should not silently drop steps.

## 6. Locator Conversion Rules

Locator certainty determines the output shape.

### Known Stable Locator

When a source case or knowledge base provides a stable locator, emit `locator`.

```yaml
- tapOn:
    target: "Settings button"
    locator:
      accessibilityId: SettingsButton
```

### Semantic Target Only

When the source describes intent but no stable locator is known, emit `target` only.

```yaml
- tapOn:
    target: "Settings and more button on toolbar"
```

The executor may later resolve this through accessibility tree based locator resolution.

### Relation Disambiguation

When the source gives contextual position, put relation constraints inside `locator`.

```yaml
- inputText:
    text: "123456"
    target: "Password input field"
    locator:
      text: "Password"
      below:
        text: "Username"
```

### Coordinates

Coordinates may be emitted only when they are explicit in the source case or derived from trusted backend element bounds. Non-vision screenshot coordinate guessing is forbidden.

```yaml
- tapOn:
    target: "Canvas point selected by legacy case"
    locator:
      point:
        x: 120
        y: 240
```

## 7. Validation Rules

The converter validates the parser-normalized model against:

```text
docs/codex-fsq-ai-test-dsl-v1.schema.json
```

Validation failure should block final output unless the user explicitly requests a best-effort draft. Best-effort drafts must still include a conversion report that lists every schema violation.

## 8. CLI Shape

Recommended tool name:

```text
tools/codex_fsq_convert.py
```

Recommended command shape:

```bash
python3 tools/codex_fsq_convert.py \
  --input path/to/source-case.md \
  --output path/to/codex-converted-case.yaml \
  --report path/to/codex-converted-case.codex-conversion-report.md \
  --platform windows \
  --app-name edge \
  --schema docs/codex-fsq-ai-test-dsl-v1.schema.json
```

Recommended options:

```text
--input
--output
--report
--schema
--platform
--app-id
--app-name
--app-exe
--window-title-regex
--known-locators
--accessibility-tree
--best-effort
```

## 9. Review Checklist

Every converted case should be reviewed for:

- command names use FSQ camelCase
- every source step is represented or explicitly reported as unresolved
- assertions remain blocking unless `optional: true` is intentional
- uncertain locators are represented as `target`, not fake `locator`
- relation constraints are nested inside `locator`
- no evidence, repair, or conversion metadata is embedded in the testcase YAML
- non-vision screenshot coordinate guessing did not occur

## 10. Recommended Implementation Milestones

1. Implement schema fix verification and converter design review.
2. Implement a minimal converter for plain text and markdown step lists.
3. Add optional Maestro-like YAML input support.
4. Add known locator mapping support.
5. Add accessibility tree assisted locator suggestion as a later executor-adjacent feature.
