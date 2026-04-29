# backround

2025年和团队一起做了FSQ1.0版本，当时的主要核心思路是AI 不是很靠谱，所以需要人来监控运行效果。设计了一套 E2E的 regression Test 的AI 自动化测试框架。

2026年了，发现AI飞速发展。 应该从围绕AI 能力的角度重新设计一下FSQ2.0版本了。FSQ2.0 版本的核心

Goal (自然语言目标)
    ↓
Plan IR (结构化计划)
    ↓
Appium 3.x MCP or Cli (执行)
    ↓
Evidence (执行结果)
    ↓
Repair (自动修复)

## 参考资料：

- Maestro： /Users/qunmi/Documents/github/Maestro
- Appium:  /Users/qunmi/Documents/github/Appium
- Edge Mac Testcase： /Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Mac
- Edge Android Testcase: /Users/qunmi/Documents/MS_ADO/FSQ_AI_Testcases_Android

资料的使用方式： 
- Maestro，重点看 声明式 YAML DSL 这个对我们的目标有非常大帮助。
- Appium， 重点看 appium 3.x 部分的Action 部分，需要支持 MacOS， Android 和 iOS。
- Edge Mac Testcase 和 Edge Android Testcase: 主要是我们现在的case格式，需要这些case 可以被转化。

## Scope: 

本项目只产出一个 AI Agent Firendly 的 Testcase 的 YAML 文件。 其中包括三个部分：
- 本身YAML 文件的格式
- YAML 文件格式的Scheme 定义
- 现有的case BDD 格式 转成 YAML 文件的工具。

目标：
-  AI Agent Firendly 的 Testcase 的 YAML 文件定义特别重要。主要服务于 Plan IR。 
- Plan IR 会从知识库中，结合用户的测试目的来 生成 测试用例的YAML文件。
- YAML 文件 “测试意图”，不是底层执行细节。
- 不要让 AI 直接自由调用 findElement、click、sendKeys。更好的方式是让 AI 生成 YAML文件，然后由执行器翻译成 Appium 命令
- AI 不直接控制 Appium，AI 生成/修复 YAML