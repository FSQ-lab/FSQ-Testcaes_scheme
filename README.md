# FSQ AI Test DSL Codex Artifacts

## 中文

### 仓库用途

这个仓库用于沉淀 **AI Agent Friendly** 的 FSQ 自动化测试资产。当前主要包含三类内容：

- **DSL 定义**：用于描述跨平台 UI 自动化测试 case，面向 AI Agent 生成、审阅、执行和修复。
- **Schema**：用于校验 DSL case 的结构和字段约束。
- **Codex Skills**：用于辅助 case 转化和 case 运行交接。

仓库也包含一批已转化的 Codex YAML case，方便团队基于真实 case 验证 DSL、Schema 和 runner 方向。

### 核心产物

| 类型 | 路径 | 说明 |
| --- | --- | --- |
| DSL 设计文档 | `docs/codex-fsq-ai-test-dsl-v1.md` | FSQ AI Test DSL v1 的主要定义 |
| JSON Schema | `docs/codex-fsq-ai-test-dsl-v1.schema.json` | DSL case 的机器可校验 schema |
| 转化工具设计 | `docs/codex-fsq-case-converter-design.md` | case 转化工具和流程说明 |
| 转化 skill | `skills/codex-fsq-case-converter/` | 将平台 case 转成 FSQ Codex YAML 的 skill |
| 运行 skill | `skills/codex-fsq-case-runner/` | 选择、校验、生成 manifest、运行 case 的 skill |
| 已转化 case | `fsq-testcases/` | Android、iOS、macOS、Windows 各 20 条 case |
| 交付说明 | `docs/codex-repository-handoff.md` | 当前仓库状态、验证命令和后续建议 |

### Case 目录

```text
fsq-testcases/
  android/
  ios/
  macos/
  windows/
```

当前 case 数量：

| 平台 | Codex YAML case | 转化报告 |
| --- | ---: | ---: |
| Android | 20 | 20 |
| iOS | 20 | 20 |
| macOS | 20 | 20 |
| Windows | 20 | 20 |
| Total | 80 | 80 |

### AI Agent Friendly 原则

这个仓库中的 DSL 和 case 设计优先服务 AI Agent：

- 使用声明式 action，减少自然语言步骤的二次解释成本。
- 保留 `steps` 结构，方便人审阅，也方便 Agent 分步执行和定位失败。
- locator 是可选增强信息，不强制 case 作者提前陷入执行细节。
- 执行失败应进入 repair 流程，不应在非 vision 模型下截图猜坐标。
- 视觉断言、账号前置条件、复杂手势和平台差异应由 runner 或 repair 层显式分类处理。

### 校验全部 Case

```bash
python3 skills/codex-fsq-case-converter/scripts/validate_fsq_cases.py \
  --schema docs/codex-fsq-ai-test-dsl-v1.schema.json \
  --cases fsq-testcases
```

期望输出：

```text
total=80 failed=0
```

### 列出 Case

```bash
python3 skills/codex-fsq-case-runner/scripts/list_fsq_cases.py \
  --cases fsq-testcases \
  --platform android
```

### 运行 Case

`codex-fsq-case-runner` skill 提供 case 选择、schema 校验、manifest 生成和 evidence 目录管理。真正执行时需要传入具体 runner command。

```bash
python3 skills/codex-fsq-case-runner/scripts/run_fsq_cases.py \
  --cases fsq-testcases/android/bottom_bar/access_settings_through_overflow_menu.codex.yaml \
  --runner-command "<runner> --case {case} --backend {backend} --output {output} --manifest {manifest}"
```

平台默认 backend：

| 平台 | Backend |
| --- | --- |
| Android | `appium-mcp` |
| iOS | `appium-mcp` |
| macOS | `appium-mcp` |
| Windows | `pywinauto-mcp` |

### Android 试跑结论

当前本地 Android 试跑验证了基础链路：Appium 3.x、UiAutomator2、设备连接、schema 校验、manifest 生成和基础 bottom bar 菜单流可以端到端工作。

已观察到的结果：

- 4 条 Android bottom bar case 通过临时 Appium runner。
- 16 条之前失败的 Android case 在系统切换为英文后仍然失败。
- 英文系统能改善部分 UI 文案匹配，但不能解决主要问题。

主要后续方向：

- runner 需要获取当前 accessibility tree。
- runner 需要 semantic target resolver，把 `target` 描述解析为稳定定位方式。
- runner 需要 repair 分类，包括元素找不到、页面未就绪、状态不对、缺少前置条件、不支持视觉断言、转化缺口等。
- 非 vision 模型下禁止截图猜坐标。

## English

### Repository Purpose

This repository stores **AI Agent Friendly** FSQ automated testing artifacts. It currently focuses on three deliverables:

- **DSL definition**: a cross-platform UI automation test case format designed for AI Agent generation, review, execution, and repair.
- **Schema**: a machine-checkable JSON Schema for validating DSL cases.
- **Codex Skills**: local skills for case conversion and case execution handoff.

The repository also includes converted Codex YAML cases so the team can validate the DSL, schema, and runner direction against real test cases.

### Primary Artifacts

| Type | Path | Description |
| --- | --- | --- |
| DSL design | `docs/codex-fsq-ai-test-dsl-v1.md` | Main FSQ AI Test DSL v1 definition |
| JSON Schema | `docs/codex-fsq-ai-test-dsl-v1.schema.json` | Machine-checkable schema for DSL cases |
| Converter design | `docs/codex-fsq-case-converter-design.md` | Case conversion tool and workflow notes |
| Converter skill | `skills/codex-fsq-case-converter/` | Skill for converting platform cases into FSQ Codex YAML |
| Runner skill | `skills/codex-fsq-case-runner/` | Skill for selecting, validating, manifesting, and running cases |
| Converted cases | `fsq-testcases/` | 20 cases each for Android, iOS, macOS, and Windows |
| Handoff notes | `docs/codex-repository-handoff.md` | Current repository state, validation commands, and next steps |

### Case Layout

```text
fsq-testcases/
  android/
  ios/
  macos/
  windows/
```

Current inventory:

| Platform | Codex YAML cases | Conversion reports |
| --- | ---: | ---: |
| Android | 20 | 20 |
| iOS | 20 | 20 |
| macOS | 20 | 20 |
| Windows | 20 | 20 |
| Total | 80 | 80 |

### AI Agent Friendly Principles

The DSL and cases in this repository are optimized for AI Agents:

- Use declarative actions to reduce secondary interpretation of free-form natural-language steps.
- Keep the `steps` structure for human review, step-by-step execution, and failure localization.
- Treat locators as optional enhancement data, not mandatory authoring burden.
- Route execution failures into repair instead of screenshot coordinate guessing under non-vision models.
- Classify visual assertions, account preconditions, complex gestures, and platform differences explicitly in the runner or repair layer.

### Validate All Cases

```bash
python3 skills/codex-fsq-case-converter/scripts/validate_fsq_cases.py \
  --schema docs/codex-fsq-ai-test-dsl-v1.schema.json \
  --cases fsq-testcases
```

Expected output:

```text
total=80 failed=0
```

### List Cases

```bash
python3 skills/codex-fsq-case-runner/scripts/list_fsq_cases.py \
  --cases fsq-testcases \
  --platform android
```

### Run Cases

The `codex-fsq-case-runner` skill handles case selection, schema validation, manifest generation, and evidence directory management. Actual execution requires a concrete runner command.

```bash
python3 skills/codex-fsq-case-runner/scripts/run_fsq_cases.py \
  --cases fsq-testcases/android/bottom_bar/access_settings_through_overflow_menu.codex.yaml \
  --runner-command "<runner> --case {case} --backend {backend} --output {output} --manifest {manifest}"
```

Default platform backends:

| Platform | Backend |
| --- | --- |
| Android | `appium-mcp` |
| iOS | `appium-mcp` |
| macOS | `appium-mcp` |
| Windows | `pywinauto-mcp` |

### Android Test Findings

The local Android smoke run validated the basic execution path: Appium 3.x, UiAutomator2, device connectivity, schema validation, manifest generation, and basic bottom-bar menu flows can work end to end.

Observed results:

- 4 Android bottom-bar cases passed with a temporary Appium runner.
- 16 previously failing Android cases still failed after switching the device UI to English.
- English UI text helps some matching, but it does not solve the main issue.

Recommended next steps:

- The runner should capture the current accessibility tree.
- The runner needs a semantic target resolver that maps `target` descriptions to stable locator strategies.
- The runner needs repair classification for missing elements, page-not-ready states, wrong states, missing preconditions, unsupported visual assertions, and conversion gaps.
- Non-vision models must not fall back to screenshot coordinate guessing.

