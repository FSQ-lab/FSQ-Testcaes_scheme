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
| 已转化 case | `fsq-testcases/` | Android、iOS、macOS、Windows 的 Codex YAML case |
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
| Android | 26 | 26 |
| iOS | 24 | 24 |
| macOS | 24 | 24 |
| Windows | 24 | 24 |
| Total | 98 | 98 |

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
total=98 failed=0
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

当前本地 Android 试跑验证了基础链路：Appium 3.x、UiAutomator2、设备连接、schema 校验、manifest 生成、evidence 采集和一批真实 Edge Android case 可以端到端工作。

最新试跑结论：

- Android 目前有 26 条 Codex YAML case，其中 `rewards` 和 `default browser` 两条临时标记为 `codex-skip`，因为依赖账号或设备默认浏览器状态。
- 最近一轮批跑使用 `--exclude-tag codex-skip` 选择 18 条 case；runner 修复后结果为 **14 passed / 4 failed**。
- 已验证的 runner 修复包括：NTP bottom omnibox 模式下 `search_box_text` 缺失时按目标语义回退到 `url_bar`；`Navigate up` 点击后页面未变化时回退 Android Back。
- 剩余 4 个失败已分类：`assertWithAI` 暂未实现；一个 Web 结果文本与 case 预期不一致；一个 Tab Center 菜单状态需要继续看 evidence；一个 NTP 搜索 target 文案不够明确，未触发 bottom omnibox fallback。

当前建议：

- 团队验证时优先运行非 `codex-skip` 的 Android case，并保留每步 page source / screenshot evidence。
- 继续补齐简单版 `assertWithAI` 或 screenshot visual assertion runner 能力。
- 保持 accessibility-first：定位失败进入 resolver/repair，不在非 vision 模型下截图猜坐标。
- 后续再回看 rewards/default-browser 这类需要账号或系统状态的 case。

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
| Converted cases | `fsq-testcases/` | Codex YAML cases for Android, iOS, macOS, and Windows |
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
| Android | 26 | 26 |
| iOS | 24 | 24 |
| macOS | 24 | 24 |
| Windows | 24 | 24 |
| Total | 98 | 98 |

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
total=98 failed=0
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

The local Android runs validated the basic execution path: Appium 3.x, UiAutomator2, device connectivity, schema validation, manifest generation, evidence capture, and a batch of real Edge Android cases can work end to end.

Latest findings:

- Android now has 26 Codex YAML cases. The `rewards` and `default browser` cases are temporarily tagged `codex-skip` because they depend on account state or device default-browser state.
- The latest batch selected 18 cases with `--exclude-tag codex-skip`; after runner fixes, the result was **14 passed / 4 failed**.
- Verified runner fixes include: falling back from missing NTP `search_box_text` to `url_bar` in bottom omnibox mode when target semantics match, and falling back to Android Back when `Navigate up` does not change the page.
- The remaining 4 failures are classified as: missing `assertWithAI` support, one web result text mismatch against case expectation, one Tab Center menu state/evidence issue, and one NTP search target wording issue that did not trigger the bottom-omnibox fallback.

Recommended next steps:

- For team validation, run Android cases excluding `codex-skip` and keep per-step page source / screenshot evidence.
- Add the lightweight `assertWithAI` or screenshot visual assertion path to the runner.
- Keep the accessibility-first rule: failed location should enter resolver/repair, not screenshot coordinate guessing under non-vision models.
- Revisit rewards/default-browser after account and system-state preconditions are explicitly controlled.
