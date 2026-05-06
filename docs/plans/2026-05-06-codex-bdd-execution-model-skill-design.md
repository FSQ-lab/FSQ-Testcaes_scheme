# Codex BDD Execution Model Skill Design

Codex-produced design document.

## Goal

Upgrade the FSQ case converter skill so BDD/Behave cases are converted from the real execution semantics, not from feature prose alone. Before generating FSQ DSL, Codex must build a BDD Execution Model that combines Gherkin structure, Behave step definitions, `context.execute_steps()` expansion, and environment hook normalization.

The primary success criterion is conversion fidelity: generated `.codex.yaml` cases should preserve the setup, action order, locators, assertions, and environment assumptions that Behave would actually execute.

## Current Problem

The current conversion process is better than the first version, but still too easy to drift:

- Feature steps can be converted without fully expanding `context.execute_steps()`.
- `Background`, `Rule Background`, `Scenario Outline` examples, and step arguments can be missed or flattened incorrectly.
- Behave step files are sometimes treated as feature-adjacent, but Behave loads step definitions globally from `features/steps/**/*.py`.
- `environment.py` hooks mix two different concerns: environment setup/teardown and runtime evidence/telemetry.
- Unsupported setup can accidentally become vague prose actions such as `tapOn: clean downloads`.

## Recommended Approach

Use a semi-structured conversion flow called **BDD Execution Model + Environment Hook Normalization**.

This is more precise than manual rule-only conversion, but avoids building a full converter tool too early. The skill should require Codex to construct an intermediate model before writing YAML.

```text
Source Repo
  -> Parse Gherkin
  -> Resolve Behave runtime
  -> Build BDD Execution Model
  -> Generate FSQ DSL and conversion report
```

## Gherkin Parsing Rules

The converter must parse the effective scenario, not just scan lines.

Required Gherkin inputs:

- `Feature` name, tags, and description.
- `Rule` and `Rule Background` when present.
- `Background` steps.
- `Scenario` / `Example` steps.
- `Scenario Outline` / `Scenario Template` expanded once per `Examples` row.
- Scenario tags, inherited tags, and version/skip tags.
- Step arguments: DocString and DataTable.

Effective scenario steps are ordered as:

```text
Feature Background
+ Rule Background, when applicable
+ Scenario steps with Scenario Outline values substituted
```

Step matching should remove the leading Gherkin keyword for resolution. `Given`, `When`, `Then`, `And`, and `But` do not define the Python implementation by themselves; the trailing step text does.

## Behave Step Resolution

Behave step definitions must be treated as a global registry:

```text
features/steps/**/*.py
  @given(...)
  @when(...)
  @then(...)
  @step(...)
```

Resolution order:

1. Exact decorator text match.
2. Parameterized decorator match, including quoted parameters and `{param}`-style placeholders.
3. Regex-style matcher, when used by the source repo.
4. Low-confidence semantic fallback, only with report evidence.

Each resolved step should preserve:

- Source step text and line number.
- Decorator text and implementation file/line.
- Extracted parameters.
- Confidence level.
- Extracted operations, in source order.

## `context.execute_steps()` Expansion

`context.execute_steps()` is executable BDD, not prose. It must be recursively expanded before YAML generation.

Example source:

```python
@given('I open edge and go to the NTP page')
def step_impl(context):
    context.execute_steps('''
        Given I open edge
        And I dismiss the alert dialog
        Then I can see the new tab page
    ''')
```

The intermediate model should record:

```yaml
stepExecution:
  sourceStep: Given I open edge and go to the NTP page
  resolvedImplementation: features/steps/given_steps.py:44
  expansion:
    - Given I open edge
    - And I dismiss the alert dialog
    - Then I can see the new tab page
  operations:
    - app launch
    - optional alert dismissal
    - NTP assertion
  unresolved: []
```

This model is not final DSL. It is conversion scratch space used to avoid collapsing complex helper steps into one natural-language command.

Expansion rules:

- Preserve parent-to-child step evidence.
- Insert child operations at the parent step's position.
- Limit recursion depth, for example to 5.
- Detect repeated call chains and mark cycles unresolved.
- Preserve parameters and substitutions.

## Hook Normalization

Behave hooks must be classified before conversion.

### Convert Setup And Teardown Hooks

Convert hook logic that establishes or restores case state:

- Opening app/browser to NTP.
- Clearing state when the DSL/runner has a safe equivalent.
- Login/account setup when the scenario actually needs it.
- Switching top/bottom omnibox mode.
- Preparing tab count, profile state, or required permissions.
- Teardown that restores state or cleans temporary execution state.

These become case setup or teardown commands.

### Do Not Convert Runtime Evidence Hooks Yet

Do not put these into YAML case commands:

- Screenshot capture after scenario.
- Telemetry or Application Insights metrics.
- Retry patching.
- Session close / MCP worker shutdown.
- Log archival and screenshot naming.

Record them in the conversion report or runner policy instead.

### Android Environment Example

For Android `environment.py`:

- `before_all` starts MCP/session and loads env: runner/environment requirement, not case commands.
- `before_scenario` version/skip checks become environment constraints or skip/unresolved metadata.
- `before_scenario` `context.execute_steps("Given I open edge and go to the NTP page")` becomes executable setup and must be expanded.
- `after_scenario` screenshot is runtime evidence and is not converted to YAML.
- `after_step` telemetry is runtime evidence and is not converted to YAML.
- `after_all` session close is runner lifecycle and is not converted to YAML.

## Environment Variables

Handle common Android environment variables as assumptions and requirements, not plaintext YAML values.

### `TEST_ACCOUNT_EMAIL`

- Required only for login, account, sync, profile, rewards, or MSA scenarios.
- If login setup is not skipped, assume the provided account can log in successfully.
- Do not write the actual email into YAML.
- If a source step inputs the email, use `${TEST_ACCOUNT_EMAIL}` or record an unresolved secret-handling item if the DSL cannot express env placeholders safely.

### `TEST_ACCOUNT_PASSWORD`

- Required only for login, account, sync, profile, rewards, or MSA scenarios.
- If login setup is not skipped, assume login succeeds with the supplied password.
- Never write the password into YAML.
- Use `${TEST_ACCOUNT_PASSWORD}` only if the DSL and runner support env placeholders safely.

### `PACKAGE`

- Used as Android app identity and resource-id prefix.
- If install/uninstall setup is not present or is skipped, assume the target package is already installed and launchable.
- Use `appId: ${PACKAGE}` when runner support is expected, or record the default source value in the report.
- If source setup performs install, uninstall, or clear app data and no safe DSL equivalent exists, mark it unresolved or as a runner requirement.

## YAML Generation

Generated YAML should follow this order:

```text
setup commands
scenario body commands
teardown commands
```

Rules:

- Every case still starts with `launchApp` and ends with `killApp` unless an approved runner convention replaces that.
- Background and executable setup hooks are part of setup.
- Scenario steps are body commands.
- State-restoring `after_scenario` operations are teardown commands.
- Runtime evidence hooks are excluded from YAML.
- Unsupported setup must not become a prose `tapOn`.
- Secrets must not be written as literal YAML values.

Example shape:

```yaml
schemaVersion: fsq.ai-test/v1
name: Example Android case
platform: android
appId: ${PACKAGE}
tags:
  - p0
  - codex-converted
---
- launchApp
- tapOn:
    target: Dismiss alert dialog
    optional: true
- assertVisible:
    target: New tab page
    optional: false
- tapOn:
    target: Search box
    locator:
      resourceId: ${PACKAGE}:id/url_bar
- killApp
```

## Conversion Report Upgrade

Reports should explain how the YAML was derived.

Add these sections:

```markdown
## BDD Execution Model

## Hook Normalization

| Hook | Classification | Converted? | Notes |
| --- | --- | --- | --- |

## Environment Requirements

## Step Expansion Evidence

| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |
```

Unresolved items should be classified:

- Unsupported environment setup.
- Missing step implementation.
- Unsafe secret handling.
- Runtime evidence intentionally not converted.
- Low-confidence semantic fallback.
- Scenario skipped by source tags or version gates.

## Skill Packaging Design

Keep `SKILL.md` concise and move detailed BDD rules into references.

Proposed structure:

```text
skills/codex-fsq-case-converter/
  SKILL.md
  references/
    codex-fsq-conversion-rules.md
    codex-bdd-execution-model.md
    codex-behave-hook-normalization.md
```

`SKILL.md` should state the hard rule:

```text
Before converting BDD/Behave cases, build a BDD Execution Model.
Do not generate YAML directly from feature prose.
```

`codex-bdd-execution-model.md` should contain:

- Gherkin grammar subset.
- Effective scenario construction.
- Scenario Outline expansion.
- Behave global step registry matching.
- `context.execute_steps()` recursion.
- Step Execution Model structure.
- YAML generation order.

`codex-behave-hook-normalization.md` should contain:

- Hook classification.
- Setup/teardown conversion rules.
- Runtime evidence exclusion rules.
- Android `environment.py` example.
- Environment variable policy.
- Hook report template.

`codex-fsq-conversion-rules.md` should continue to answer a narrower question: once the source operation is known, how should it map to FSQ commands?

## Validation Plan

After updating the skill:

1. Re-run schema validation for existing 80 `.codex.yaml` files.
2. Use one Android case with `before_scenario` setup to verify the new report format.
3. Verify no source repository files are modified.
4. Confirm installed skill under `/Users/qunmi/.agents/skills/codex-fsq-case-converter` matches the repo copy.

## Open Decisions

- Whether `${PACKAGE}` placeholders are accepted directly by every runner, or whether generated YAML should use the current source default while reports record the env relationship.
- Whether optional setup actions need a dedicated DSL field beyond current `optional: true` behavior.
- Whether hook-derived setup should be visibly commented in YAML or only traced in the conversion report.
