# Codex BDD Execution Model

Use this reference before converting BDD/Gherkin/Behave cases into FSQ DSL. The goal is to model what Behave would execute, then generate YAML from that model.

## Model Shape

Build scratch evidence like this before writing the final `.codex.yaml`:

```yaml
bddExecutionModel:
  sourceFeature: features/example.feature
  feature: Example feature name
  rule: Optional rule name
  scenario: Example scenario name
  expandedFromScenarioOutline: false
  tags: [p0, smoke]
  effectiveSteps:
    - keyword: Given
      text: I open edge and go to the NTP page
      source: features/example.feature:12
      resolvedImplementation: features/steps/given_steps.py:44
      expansion: []
      operations:
        - launch_app
        - optional dismiss alert
        - verify NTP
      unresolved: []
```

This model is report evidence and conversion scratch space. It is not the final FSQ DSL.

## Gherkin Effective Scenario

Parse Gherkin by structure, not by line scanning.

Required inputs:

- `Feature` name, description, and tags.
- `Rule`, `Rule Background`, and rule tags when present.
- `Background` steps.
- `Scenario` / `Example` steps.
- `Scenario Outline` / `Scenario Template` expanded once per `Examples` row.
- Scenario tags and inherited tags.
- Step arguments: DocString and DataTable.

Effective step order:

```text
Feature Background
+ Rule Background, when applicable
+ Scenario steps with Scenario Outline values substituted
```

Step keywords are execution order markers, not implementation selectors. Resolve a step using the text after `Given`, `When`, `Then`, `And`, or `But`.

## Behave Step Registry

Behave loads step definitions globally from:

```text
features/steps/**/*.py
```

Collect decorators:

- `@given(...)`
- `@when(...)`
- `@then(...)`
- `@step(...)`

Resolution order:

1. Exact decorator text match.
2. Parameterized decorator match, including quoted parameters and `{param}` placeholders.
3. Regex-style matcher when the source repo uses one.
4. Low-confidence semantic fallback, only with explicit report evidence.

Preserve for each resolved step:

- Feature source file and line.
- Decorator text.
- Implementation file and line.
- Extracted parameters.
- Confidence level.
- Extracted operations in source order.

## `context.execute_steps()` Expansion

Treat `context.execute_steps()` as executable nested BDD.

Rules:

- Parse the string passed to `context.execute_steps()` as Gherkin steps.
- Resolve each nested step through the same global Behave step registry.
- Insert child operations at the parent step position.
- Preserve parent and child evidence in the conversion report.
- Preserve parameter substitutions.
- Limit recursion depth, normally 5.
- Detect repeated call chains and mark cycles unresolved.

Example:

```python
@given('I open edge and go to the NTP page')
def step_impl(context):
    context.execute_steps('''
        Given I open edge
        And I dismiss the alert dialog
        Then I can see the new tab page
    ''')
```

Model it as:

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

## Operation Extraction

Extract executable facts from implementation code, not only from the feature sentence.

Look for:

- App lifecycle: launch, stop, foreground, background.
- Element actions: click, tap, long press, hover, right click.
- Text actions: input, clear, key press, shortcuts.
- Assertions: exists, not exists, text/value/attribute, visual task.
- Navigation: native navigation, address bar operations, current URL reads.
- Gestures: swipe, drag, exact Appium pointer actions.
- Waits: explicit waits, material sleeps, wait-until visible/clickable.
- Helper flows: login, dismiss dialogs, setup state, cleanup state.

Do not convert unsupported setup into vague prose actions. Mark it unresolved with source evidence.

## Report Sections

Add these report sections for BDD/Behave conversions:

```markdown
## BDD Execution Model

## Step Expansion Evidence
| Source step | Expanded steps | Implementation evidence |
| --- | --- | --- |

## Step Implementation Evidence
| Source step | Implementation file:line | Extracted operations |
| --- | --- | --- |
```
