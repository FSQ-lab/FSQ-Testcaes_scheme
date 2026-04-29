# FSQ 2.0 — AI Agent Friendly Test Case DSL 设计文档

> AI 生成为主，人类审查确认。YAML 描述测试意图，执行器翻译为 Appium/W3C 命令。

---

## 目录

1. [设计目标](#1-设计目标)
2. [文件格式](#2-文件格式)
3. [命令集设计](#3-命令集设计)
4. [元素选择器设计](#4-元素选择器设计)
5. [流程控制设计](#5-流程控制设计)
6. [W3C 协议映射](#6-w3c-协议映射)
7. [AI 提示词配套](#7-ai-提示词配套)
8. [示例与最佳实践](#8-示例与最佳实践)

---

## 1. 设计目标

### 1.1 核心原则

| 原则 | 说明 | 设计体现 |
|------|------|---------|
| **AI 生成友好** | 命令集小、语义明确，AI 容易掌握 | 扁平命令 + 字符串/对象双态 |
| **意图级抽象** | 描述"做什么"，不涉及底层细节 | 高阶命令是 W3C Actions 的语法糖 |
| **Maestro-like 格式** | 头部元数据 + `---` + 命令列表 | 与 Maestro 生态习惯对齐 |
| **camelCase 命名** | 命令名 camelCase，与 Maestro/JS 生态一致 | tapOn / inputText / assertVisible |
| **渐进复杂** | 简单场景一行搞定，复杂场景用原语 | 高阶命令 + performActions/executeMethod 原语 |
| **稳定简写** | 字符串简写落到 text locator，不落 target | `tapOn: "Login"` → `{ text: "Login" }` |
| **AI 断言** | 对齐 Maestro assertWithAI，但 optional 默认 false | assertAi + assertVisible/assertText 等 |
| **平台独立** | macOS/Android/iOS/Windows 各自独立仓库 | 一个平台一个仓库 |

### 1.2 与 Maestro 的对比定位

```
Maestro: 人类编写为主，AI 辅助生成
   ↓
FSQ 2.0: AI 生成为主，人类审查确认
   ↓
关键差异:
- 更严格的 Schema 约束（减少 AI 生成错误）
- 双层元素定位（text locator + 可选 target 自然语言补充）
- W3C 原语命令（performActions/releaseActions/executeMethod）
- 完整的断言体系（AI 断言 + 传统精确断言并存）
- assertAi optional 默认 false，由 case/policy 显式声明
- AI 专用的恢复策略（Repair 流程）
```

### 1.3 核心流程

```
Goal (自然语言目标)
    ↓
Plan IR (结构化计划)  ← 从知识库生成 YAML
    ↓
YAML (本 DSL)          ← 本文档定义的格式
    ↓
Appium 3.x (执行)     ← 执行器翻译为 W3C 协议调用
    ↓
Evidence (执行结果)
    ↓
Repair (AI 修复 YAML)
```

---

## 2. 文件格式

### 2.1 Maestro-like 结构

文件分为两部分：**头部元数据** 和 **命令列表**，用 YAML 文档分隔符 `---` 隔开。

```yaml
# ═══════════════════════════════════════════════════════════════
# 头部元数据
# ═══════════════════════════════════════════════════════════════
appId: ${APP_ID}                       # 包名 / Bundle ID，支持变量
name: "Search in settings"             # 流程名称 (必须)
description: "验证设置页面搜索功能"      # 流程描述 (可选)
priority: p0                           # p0 / p1 / p2 (可选)
tags: [regression, settings]           # 分类标签 (可选)
env:                                   # 局部环境变量，覆盖全局 env (可选)
  USERNAME: "test@example.com"

# 全局环境变量由执行器命令行传入:
#   executor run --env APP_ID=com.microsoft.edgemac --env TIMEOUT=30000

---
# ═══════════════════════════════════════════════════════════════
# 命令列表
# ═══════════════════════════════════════════════════════════════
- launchApp
- tapOn: "Settings and more"
- tapOn: "Settings"
- assertVisible: "Settings page"
```

### 2.2 仓库目录结构

每个平台一个独立仓库：

```
fsq-testcases-mac/
  settings/
    open_settings.yaml
    search_settings.yaml
  omnibox/
    navigate_url.yaml
  shared/                              # 可复用子流程
    launch_edge.yaml
  env.yaml                             # 可选：仓库级默认 env
```

### 2.3 preconditions (前置条件)

前置条件作为头部字段声明，引用子流程：

```yaml
appId: ${APP_ID}
name: "Search in settings"
tags: [regression, settings]
preconditions:
  - runFlow: shared/launch_edge.yaml
---
- tapOn: "Settings and more"
```

---

## 3. 命令集设计

### 3.1 命令分类总览

命令分为两层：**高阶命令**（语法糖）和 **W3C 原语命令**。

```
┌──────────────────────────────────────────────────────────────┐
│                   高阶命令 (语法糖)                            │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  应用控制 (3)      交互操作 (9)       断言验证 (6)          │
│  ─────────────     ─────────────      ─────────────         │
│  launchApp         tapOn              assertVisible          │
│  killApp           longPress          assertNotVisible       │
│  clearData         doubleTap          assertText             │
│                    rightClick         assertEnabled          │
│                    inputText          assertChecked          │
│                    clearText          assertAi               │
│                    swipe                                     │
│                    scroll                                    │
│                    drag                                      │
│                                                              │
│  等待命令 (4)      导航命令 (4)       设备控制 (4)          │
│  ─────────────     ─────────────      ─────────────         │
│  waitVisible       back               setOrientation         │
│  waitGone          home               setLocation            │
│  waitText          openUrl            screenshot             │
│  waitSeconds       pressKey           startRecording         │
│                                                              │
│  流程控制 (3+1)    数据操作 (2)                             │
│  ─────────────     ─────────────                             │
│  if                setVariable                               │
│  retry             extractText                               │
│  repeat                                                      │
│  runFlow                                                     │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                   W3C 原语命令 (3)                            │
├──────────────────────────────────────────────────────────────┤
│  performActions    releaseActions     executeMethod           │
└──────────────────────────────────────────────────────────────┘
```

高阶命令是 W3C 原语的语法糖，等价关系见[第 6 节](#6-w3c-协议映射)。

### 3.2 W3C 原语命令

这三个命令直接映射到 Appium 3.x / W3C WebDriver 协议端点，可表达任何高阶命令无法覆盖的操作。

```yaml
# ─────────────────────────────────────────────────────────────────
# performActions — 构造 W3C Actions 序列
# 直接对应 POST /session/{id}/actions
# ─────────────────────────────────────────────────────────────────
- performActions:
    actions:
      - type: pointer                     # pointer / key / wheel
        id: finger1
        parameters:
          pointerType: touch              # touch / mouse / pen
        actions:
          - type: pointerMove
            duration: 0
            x: 100
            y: 200
          - type: pointerDown
            button: 0
          - type: pause
            duration: 500
          - type: pointerUp
            button: 0

# 多输入源示例: 双指缩放
- performActions:
    actions:
      - type: pointer
        id: finger1
        parameters: { pointerType: touch }
        actions:
          - { type: pointerMove, x: 200, y: 400 }
          - { type: pointerDown, button: 0 }
          - { type: pointerMove, x: 100, y: 300, duration: 500 }
          - { type: pointerUp, button: 0 }
      - type: pointer
        id: finger2
        parameters: { pointerType: touch }
        actions:
          - { type: pointerMove, x: 200, y: 400 }
          - { type: pointerDown, button: 0 }
          - { type: pointerMove, x: 300, y: 500, duration: 500 }
          - { type: pointerUp, button: 0 }

# ─────────────────────────────────────────────────────────────────
# releaseActions — 释放所有输入源
# 直接对应 DELETE /session/{id}/actions
# ─────────────────────────────────────────────────────────────────
- releaseActions

# ─────────────────────────────────────────────────────────────────
# executeMethod — 调用 Appium execute methods
# 直接对应 POST /session/{id}/execute
# ─────────────────────────────────────────────────────────────────
# 示例: 移动端滚动
- executeMethod:
    method: "mobile: scroll"
    args:
      direction: "down"
      percent: 0.75

# 示例: 处理系统弹窗
- executeMethod:
    method: "mobile: alert"
    args:
      action: "accept"

# 示例: 获取剪贴板
- executeMethod:
    method: "mobile: getClipboard"
    args:
      contentType: "plaintext"
```

### 3.3 高阶命令详细定义

#### 3.3.1 应用控制命令

```yaml
# ─────────────────────────────────────────────────────────────────
# launchApp — 启动应用
# ─────────────────────────────────────────────────────────────────
# 简写: 使用头部 appId
- launchApp

# 完整形式
- launchApp:
    appId: "com.microsoft.edgemac"      # 包名 / Bundle ID (与 path 二选一)
    path: "C:\\Program Files\\Edge\\msedge.exe"  # 可执行文件路径 (Windows/macOS)
    clearData: false                     # 启动前清除数据
    waitForReady: true                   # 等待应用就绪
    timeout: 10000                       # 启动超时 (ms)
    arguments:                           # 启动参数
      debug: true

# ─────────────────────────────────────────────────────────────────
# killApp — 强制关闭应用
# ─────────────────────────────────────────────────────────────────
- killApp
- killApp:
    appId: "com.microsoft.edgemac"

# ─────────────────────────────────────────────────────────────────
# clearData — 清除应用数据
# ─────────────────────────────────────────────────────────────────
- clearData
- clearData:
    appId: "com.microsoft.edgemac"
```

#### 3.3.2 交互操作命令

```yaml
# ─────────────────────────────────────────────────────────────────
# tapOn — 点击元素
# ─────────────────────────────────────────────────────────────────
# 简写 → { text: "Login" }
- tapOn: "Login"

# 完整形式
- tapOn:
    text: "Login"                        # text locator (稳定，推荐)
    locator:                             # 精确定位 (优先级最高)
      accessibilityId: "btn_login"
    target: "Login button on sign-in page"  # 自然语言补充 (locator 不确定时)
    index: 0                             # 多个匹配时取第几个
    below: "Username"                    # 关系定位：位于某元素下方
    above: "Forgot password"             # 关系定位：位于某元素上方
    near: "icon"                         # 关系定位：靠近某元素
    timeout: 5000                        # 等待元素出现
    retry: 3                             # 失败重试次数
    optional: false                      # 失败是否中断流程

# ─────────────────────────────────────────────────────────────────
# longPress — 长按
# ─────────────────────────────────────────────────────────────────
- longPress: "Delete"
- longPress:
    text: "Delete"
    locator:
      accessibilityId: "btn_delete"
    duration: 1000                       # 长按时长 (ms)

# ─────────────────────────────────────────────────────────────────
# doubleTap — 双击
# ─────────────────────────────────────────────────────────────────
- doubleTap: "Like"
- doubleTap:
    text: "Like"
    interval: 100                        # 两次点击间隔 (ms)

# ─────────────────────────────────────────────────────────────────
# rightClick — 右键点击 (桌面端)
# ─────────────────────────────────────────────────────────────────
- rightClick: "Google tab header"
- rightClick:
    text: "Google tab header"
    locator:
      accessibilityId: "tabHeader_Google"

# ─────────────────────────────────────────────────────────────────
# inputText — 输入文本
# ─────────────────────────────────────────────────────────────────
# 简写: 输入到当前焦点
- inputText: "hello world"

# 完整形式
- inputText:
    text: "${USERNAME}"                  # 输入内容，支持变量
    element: "Email input"               # 目标元素 (text locator)
    locator:
      accessibilityId: "searchField"
    clearFirst: true                     # 输入前清空
    hideKeyboard: true                   # 输入后隐藏键盘

# ─────────────────────────────────────────────────────────────────
# clearText — 清除文本
# ─────────────────────────────────────────────────────────────────
- clearText                              # 清除当前焦点
- clearText:
    element: "Search box"
    locator:
      accessibilityId: "searchField"
    characters: 10                       # 或指定删除字符数

# ─────────────────────────────────────────────────────────────────
# swipe — 滑动
# ─────────────────────────────────────────────────────────────────
- swipe: "up"                            # up / down / left / right

- swipe:
    direction: "up"
    distance: "medium"                   # short / medium / long
    duration: 500                        # 滑动时长 (ms)
    element: "List area"                 # 在指定元素上滑动
    # 或使用坐标
    from: [200, 800]
    to: [200, 200]

# ─────────────────────────────────────────────────────────────────
# scroll — 滚动到元素可见
# ─────────────────────────────────────────────────────────────────
- scroll:
    to: "Item 20"                        # 滚动直到该元素可见
    direction: "down"                    # up / down
    maxScrolls: 10                       # 最大滚动次数
    timeout: 30000

# ─────────────────────────────────────────────────────────────────
# drag — 拖拽
# ─────────────────────────────────────────────────────────────────
- drag:
    from: "Task A"                       # 起始元素
    to: "Done"                           # 目标元素
    duration: 1000
```

#### 3.3.3 断言验证命令

断言分两类：**传统精确断言**（基于元素属性）和 **AI 断言**（基于截图 + LLM）。

```yaml
# ─────────────────────────────────────────────────────────────────
# assertVisible — 断言元素可见
# ─────────────────────────────────────────────────────────────────
- assertVisible: "Welcome"

- assertVisible:
    text: "Welcome"
    locator:
      text: "Welcome.*"                  # 正则匹配
    timeout: 5000
    optional: false

# ─────────────────────────────────────────────────────────────────
# assertNotVisible — 断言元素不可见
# ─────────────────────────────────────────────────────────────────
- assertNotVisible: "Loading"

- assertNotVisible:
    text: "Loading"
    locator:
      id: "loading_spinner"
    timeout: 10000

# ─────────────────────────────────────────────────────────────────
# assertText — 断言元素文本内容
# ─────────────────────────────────────────────────────────────────
- assertText:
    element: "Price label"
    locator:
      id: "price_label"
    equals: "¥99.00"                     # 精确匹配
    # 或
    contains: "99"                       # 包含
    # 或
    matches: "¥\\d+\\.\\d{2}"           # 正则匹配

# ─────────────────────────────────────────────────────────────────
# assertEnabled — 断言元素可用状态
# ─────────────────────────────────────────────────────────────────
- assertEnabled:
    element: "Submit button"
    locator:
      id: "submit_button"
    enabled: true                        # true = 可用, false = 禁用

# ─────────────────────────────────────────────────────────────────
# assertChecked — 断言勾选状态
# ─────────────────────────────────────────────────────────────────
- assertChecked:
    element: "Remember me"
    locator:
      text: "Remember me"
    checked: true

# ─────────────────────────────────────────────────────────────────
# assertAi — AI 视觉断言 (对齐 Maestro assertWithAI)
# ─────────────────────────────────────────────────────────────────
# 简写
- assertAi: "page shows login success with welcome message and avatar"

# 完整形式
- assertAi:
    assertion: "the browser theme is dark, title bar and toolbar are dark colored"
    optional: false                      # 默认 false，失败即阻断
    label: "Check dark theme"            # 可读标签
    confidence: 0.8                      # AI 置信度阈值
```

#### 3.3.4 等待命令

```yaml
# ─────────────────────────────────────────────────────────────────
# waitVisible — 等待元素出现
# ─────────────────────────────────────────────────────────────────
- waitVisible: "Done"

- waitVisible:
    text: "Done"
    locator:
      text: "Done"
    timeout: 30000
    pollInterval: 500                    # 轮询间隔

# ─────────────────────────────────────────────────────────────────
# waitGone — 等待元素消失
# ─────────────────────────────────────────────────────────────────
- waitGone: "Loading..."

- waitGone:
    text: "Loading..."
    locator:
      id: "loading_spinner"
    timeout: 30000

# ─────────────────────────────────────────────────────────────────
# waitText — 等待文本内容变化
# ─────────────────────────────────────────────────────────────────
- waitText:
    element: "Status label"
    locator:
      id: "status_label"
    contains: "Done"
    timeout: 60000

# ─────────────────────────────────────────────────────────────────
# waitSeconds — 固定等待 (尽量少用)
# ─────────────────────────────────────────────────────────────────
- waitSeconds: 2
```

#### 3.3.5 导航命令

```yaml
# ─────────────────────────────────────────────────────────────────
# back — 返回
# ─────────────────────────────────────────────────────────────────
- back

# ─────────────────────────────────────────────────────────────────
# home — 回到主屏幕
# ─────────────────────────────────────────────────────────────────
- home

# ─────────────────────────────────────────────────────────────────
# openUrl — 打开链接
# ─────────────────────────────────────────────────────────────────
- openUrl: "https://example.com"

- openUrl:
    url: "myapp://product/123"           # Deep Link
    inApp: true                          # 是否在应用内打开

# ─────────────────────────────────────────────────────────────────
# pressKey — 按键 / 快捷键
# ─────────────────────────────────────────────────────────────────
- pressKey: "enter"

- pressKey:
    key: "cmd+w"                         # 支持组合键
    times: 3                             # 重复次数
```

#### 3.3.6 设备控制命令

```yaml
# ─────────────────────────────────────────────────────────────────
# setOrientation — 设置屏幕方向
# ─────────────────────────────────────────────────────────────────
- setOrientation: "landscape"            # portrait / landscape

# ─────────────────────────────────────────────────────────────────
# setLocation — 模拟 GPS 位置
# ─────────────────────────────────────────────────────────────────
- setLocation:
    latitude: 39.9042
    longitude: 116.4074
    altitude: 50

# ─────────────────────────────────────────────────────────────────
# screenshot — 截图
# ─────────────────────────────────────────────────────────────────
- screenshot: "login_page"

- screenshot:
    name: "login_page"
    crop:                                # 裁剪到指定元素
      id: "form_container"

# ─────────────────────────────────────────────────────────────────
# startRecording / stopRecording — 录屏
# ─────────────────────────────────────────────────────────────────
- startRecording: "test_video"
- stopRecording
```

#### 3.3.7 流程控制命令

```yaml
# ─────────────────────────────────────────────────────────────────
# if — 条件执行
# ─────────────────────────────────────────────────────────────────
- if:
    condition:
      visible: "Login button"
    then:
      - tapOn: "Login button"
      - waitVisible: "Home"
    else:
      - assertVisible: "Logged in"

# 平台条件
- if:
    condition:
      platform: "android"
    then:
      - pressKey: "back"

# 表达式条件
- if:
    condition:
      expression: "${retryCount < 3}"
    then:
      - tapOn: "Retry"

# ─────────────────────────────────────────────────────────────────
# retry — 重试
# ─────────────────────────────────────────────────────────────────
- retry:
    maxRetries: 3
    steps:
      - tapOn: "Settings"
      - assertAi: "settings page is visible"

# ─────────────────────────────────────────────────────────────────
# repeat — 循环
# ─────────────────────────────────────────────────────────────────
# 固定次数
- repeat:
    times: 3
    steps:
      - tapOn: "Next page"
      - waitSeconds: 1

# 条件循环
- repeat:
    while:
      visible: "Load more"
    maxTimes: 10
    steps:
      - tapOn: "Load more"
      - waitSeconds: 2

# ─────────────────────────────────────────────────────────────────
# runFlow — 调用子流程
# ─────────────────────────────────────────────────────────────────
- runFlow: "shared/login.yaml"

- runFlow:
    file: "shared/login.yaml"
    condition:
      notVisible: "Logged in"
    env:
      USERNAME: "test@example.com"
      PASSWORD: "secret123"

# 内联子流程
- runFlow:
    steps:
      - tapOn: "Settings"
      - tapOn: "Sign out"
    condition:
      visible: "Logged in"
```

#### 3.3.8 数据操作命令

```yaml
# ─────────────────────────────────────────────────────────────────
# setVariable — 设置变量
# ─────────────────────────────────────────────────────────────────
- setVariable:
    name: "retryCount"
    value: 0

- setVariable:
    name: "retryCount"
    expression: "${retryCount + 1}"

# ─────────────────────────────────────────────────────────────────
# extractText — 从元素提取文本到变量
# ─────────────────────────────────────────────────────────────────
- extractText:
    element: "Price label"
    locator:
      id: "price_label"
    variable: "price"
```

---

## 4. 元素选择器设计

### 4.1 三层定位策略

FSQ 2.0 采用三层定位：**locator (精确)** > **text (稳定)** > **target (语义补充)**。

```
executor 收到命令
    │
    ├── 有 locator？ ──YES──→ Appium 直接定位（最快、最精确）
    │                          失败 → Repair 流程
    │
    ├── 有 text？ ────YES──→ Appium text locator 定位（稳定、可验证）
    │                          失败 → Repair 流程
    │
    └── 仅 target？ ─YES──→ executor 决策定位策略
                              ├── 1. LLM 语义理解
                              │     分析 accessibility tree + target 描述
                              │     LLM 推理出定位方式 → Appium 执行
                              │
                              └── 2. 失败 → Repair 流程
                                    AI 分析失败原因，调整定位策略
                                    注意：不要在非 vision 模型下截图猜坐标
```

```yaml
# 精确定位 (推荐，优先使用)
- tapOn:
    locator:
      accessibilityId: "SettingsAndMore"

# text locator (稳定，简写默认)
- tapOn: "Settings and more"
# 等价于:
- tapOn:
    text: "Settings and more"

# text + locator 组合
- tapOn:
    text: "Settings and more"
    locator:
      accessibilityId: "SettingsAndMore"

# target 语义补充 (locator 不确定时)
- tapOn:
    target: "the three-dot menu button on the top right toolbar"
```

### 4.2 locator 定位方式

| 字段 | 说明 | 推荐度 |
|------|------|--------|
| `accessibilityId` | Accessibility ID | 最推荐 |
| `text` | 文本内容 (支持正则) | 推荐 |
| `id` | 元素 ID / resource-id | 其次 |
| `class` | 元素类名 | 少用 |
| `xpath` | XPath 表达式 | 不推荐 |

### 4.3 关系定位 (辅助消歧)

当有多个相似元素时，用关系定位精确区分：

```yaml
- tapOn:
    text: "Confirm"
    below: "Order total"
    above: "Cancel"
    leftOf: "Cancel"
    rightOf: "Confirm"
    near: "icon"
    childOf:
      id: "login_form"
```

### 4.4 状态过滤

```yaml
- tapOn:
    text: "Submit"
    locator:
      text: "Submit"
      enabled: true
      visible: true                      # 默认 true
      selected: false
      checked: true
      focused: false
```

### 4.5 行为修饰

```yaml
- tapOn:
    text: "Login"
    timeout: 5000                        # 等待元素出现
    retry: 3                             # 操作失败重试次数
    optional: false                      # 失败是否中断流程
    index: 0                             # 多个匹配时取第几个
```

### 4.6 简写规则

所有接受元素的命令支持字符串简写，**字符串值落到 text locator**（稳定、可验证）：

```yaml
# 简写形式                               # 等价完整形式
- tapOn: "Login"                         # tapOn: { text: "Login" }
- longPress: "Delete"                    # longPress: { text: "Delete" }
- doubleTap: "Like"                      # doubleTap: { text: "Like" }
- rightClick: "Tab header"              # rightClick: { text: "Tab header" }
- assertVisible: "Welcome"              # assertVisible: { text: "Welcome" }
- assertNotVisible: "Loading"            # assertNotVisible: { text: "Loading" }
- waitVisible: "Done"                    # waitVisible: { text: "Done" }
- waitGone: "Loading"                    # waitGone: { text: "Loading" }

# 这些命令简写含义不同：
- inputText: "hello"                     # inputText: { text: "hello" } — text 是输入内容
- assertAi: "page loaded"               # assertAi: { assertion: "page loaded" }
- swipe: "up"                            # swipe: { direction: "up" }
- openUrl: "https://..."                 # openUrl: { url: "https://..." }
- pressKey: "enter"                      # pressKey: { key: "enter" }
```

### 4.7 选择器优先级规则 (给 AI 的指导)

1. **优先使用 locator** — accessibilityId > text > id，精确可靠
2. **其次使用 text** — 简写字符串，落到 text locator，稳定可验证
3. **使用关系定位处理模糊情况** — below/above/near 消歧
4. **locator 不确定时使用 target** — 自然语言描述，executor 决策定位方式
5. **避免使用 xpath** — 太脆弱，布局变化易失效
6. **避免使用 index** — 不稳定，优先用关系定位替代
7. **坚决禁止截图猜坐标** — 非 vision 模型下不要通过截图猜测元素坐标

---

## 5. 流程控制设计

### 5.1 条件表达式

```yaml
condition:
  # 元素条件
  visible: "Login button"
  notVisible: "Loading"

  # 平台条件
  platform: "android"                    # android / ios / mac / windows

  # 表达式条件 (JavaScript)
  expression: "${count > 0 && status == 'ready'}"

  # 组合条件 (AND 关系)
  visible: "Login button"
  platform: "android"
```

### 5.2 变量系统

```yaml
# 内置变量
${platform}                              # 当前平台 (mac/android/ios/windows)
${deviceName}                            # 设备名称
${timestamp}                             # 当前时间戳

# 全局环境变量 (由执行器命令行传入)
# executor run --env APP_ID=com.microsoft.edgemac --env TIMEOUT=30000
${APP_ID}
${TIMEOUT}

# 局部环境变量 (来自头部 env，覆盖全局同名变量)
${USERNAME}
${PASSWORD}

# 自定义变量
- setVariable:
    name: "counter"
    value: 0

- setVariable:
    name: "counter"
    expression: "${counter + 1}"

# 从元素提取
- extractText:
    element: "Price label"
    locator:
      id: "price_label"
    variable: "price"
```

---

## 6. W3C 协议映射

### 6.1 映射原则

所有高阶命令最终翻译为 W3C WebDriver 协议调用。映射遵循以下原则：

1. **交互操作 → W3C Actions API** (`POST /session/{id}/actions`)
2. **应用/设备控制 → Execute Methods** (`POST /session/{id}/execute`)
3. **元素查询 → Find Element** (`POST /session/{id}/element`)
4. **元素属性 → Get Element Property/Attribute** (`GET /session/{id}/element/{id}/property`)
5. **导航 → Navigation endpoints** (`POST /session/{id}/url`, `POST /session/{id}/back`)

### 6.2 高阶命令 → W3C 等价

| 高阶命令 | W3C 协议等价 | pywinauto MCP (Windows) |
|----------|-------------|--------------------------|
| **应用控制** | | |
| `launchApp` | `New Session` / `execute('mobile: activateApp')` | `app_launch()` |
| `killApp` | `execute('mobile: terminateApp')` | `app_close()` |
| `clearData` | `execute('mobile: clearApp')` | 文件系统/注册表清理 |
| **交互操作** | | |
| `tapOn` | `Actions: pointerMove → pointerDown → pointerUp` | `element_click(click_count=1)` |
| `longPress` | `Actions: pointerMove → pointerDown → pause(duration) → pointerUp` | `element_click()` + `app_wait()` |
| `doubleTap` | `Actions: pointerDown → pointerUp → pause → pointerDown → pointerUp` | `element_click(click_count=2)` |
| `rightClick` | `Actions: pointerMove → pointerDown(button=2) → pointerUp(button=2)` | `right_click()` |
| `inputText` | `Element Send Keys` / `Actions: key sequence` | `enter_text(content)` |
| `clearText` | `Element Clear` | `enter_text(content="")` |
| `swipe` | `Actions: pointerMove(start) → pointerDown → pointerMove(end) → pointerUp` | `mouse_drag_drop(by_offset)` |
| `scroll` | `execute('mobile: scroll')` 或循环 swipe | `mouse_scroll(wheel_dist)` |
| `drag` | `Actions: pointerMove(from) → pointerDown → pause → pointerMove(to) → pointerUp` | `mouse_drag_drop(to_element)` |
| **断言验证** | | |
| `assertVisible` | `Find Element` + 验证可见性 | `verify_element_exists()` |
| `assertNotVisible` | `Find Element` 期望失败或不可见 | `verify_element_not_exist()` |
| `assertText` | `Get Element Property('textContent')` + 比较 | `verify_element_value()` |
| `assertEnabled` | `Get Element Property('enabled')` | 检查 `IsEnabled` 属性 |
| `assertChecked` | `Get Element Attribute('checked')` | `verify_checkbox_state()` |
| `assertAi` | `Take Screenshot` → AI LLM 判断 | `verify_visual_task()` |
| **等待命令** | | |
| `waitVisible` | 轮询 `Find Element` 至可见 | 轮询 `verify_element_exists()` |
| `waitGone` | 轮询 `Find Element` 至不可见 | 轮询 `verify_element_not_exist()` |
| `waitText` | 轮询 `Get Element Property` 至匹配 | 轮询 `verify_element_value()` |
| `waitSeconds` | 客户端 sleep | `app_wait(duration)` |
| **导航命令** | | |
| `back` | `Back` (`POST /session/{id}/back`) | `send_keystrokes("Alt+Left")` |
| `home` | `execute('mobile: pressButton', {name:'home'})` | `send_keystrokes("Win")` |
| `openUrl` | `Navigate To` (`POST /session/{id}/url`) | 组合键 + `enter_text(url)` |
| `pressKey` | `Actions: key.down → key.up` | `send_keystrokes()` |
| **设备控制** | | |
| `setOrientation` | `Set Orientation` | N/A |
| `setLocation` | `Set Geolocation` | N/A |
| `screenshot` | `Take Screenshot` (`GET /session/{id}/screenshot`) | `app_screenshot()` |
| `startRecording` | `execute('mobile: startRecordingScreen')` | 系统级录屏 |
| **W3C 原语** | | |
| `performActions` | `POST /session/{id}/actions` (直通) | N/A |
| `releaseActions` | `DELETE /session/{id}/actions` (直通) | N/A |
| `executeMethod` | `POST /session/{id}/execute` (直通) | N/A |
| **pywinauto 独有** | | |
| — | — | `mouse_hover()` (可扩展) |
| — | — | `select_item()` (可扩展) |
| — | — | `open_folder()` (可扩展) |

### 6.3 选择器 → W3C 定位策略映射

| DSL locator | W3C Locator Strategy |
|-------------|---------------------|
| `accessibilityId` | `accessibility id` |
| `text` | `link text` / `-android uiautomator` / `NSPredicate` (平台相关) |
| `id` | `css selector` `[id="..."]` / `resource-id` |
| `class` | `css selector` / `class name` |
| `xpath` | `xpath` |

### 6.4 target 定位执行流程

当命令只有 `target` 没有 `locator` 和 `text` 时，由 executor 决策定位策略：

```
1. Executor 获取当前页面的 accessibility tree
2. 将 accessibility tree + target 描述发送给 LLM
3. LLM 语义理解，推理出最佳 W3C locator strategy
   - 返回: accessibilityId / text / id 等定位信息
4. Executor 使用推理结果通过 W3C Find Element 定位并执行

失败时进入 Repair 流程:
5. AI 分析失败原因（元素未找到 / 状态不对 / 页面未就绪）
6. AI 调整策略重新尝试（如换用其他 locator 方式）

重要原则:
- 坚决禁止在非 vision 模型下截图猜坐标
- 定位失败应走 Repair 流程，而不是 fallback 到视觉猜测
```

---

## 7. AI 提示词配套

### 7.1 System Prompt

```markdown
# 角色定义

你是一个 UI 自动化测试专家。你的任务是根据用户描述或测试需求，生成符合 FSQ 2.0 DSL 规范的测试脚本。

# DSL 格式

文件格式: 头部元数据 + --- + 命令列表

# 支持的命令 (camelCase)

**应用控制**: launchApp, killApp, clearData
**交互操作**: tapOn, longPress, doubleTap, rightClick, inputText, clearText, swipe, scroll, drag
**断言验证**: assertVisible, assertNotVisible, assertText, assertEnabled, assertChecked, assertAi
**等待命令**: waitVisible, waitGone, waitText, waitSeconds
**导航命令**: back, home, openUrl, pressKey
**设备控制**: setOrientation, setLocation, screenshot, startRecording
**流程控制**: if, retry, repeat, runFlow
**数据操作**: setVariable, extractText
**W3C 原语**: performActions, releaseActions, executeMethod

## 元素定位

三层优先级：locator > text > target

1. **locator (最精确)** — accessibilityId / text / id
2. **text (稳定)** — 字符串简写默认落到 text locator
3. **target (语义补充)** — locator 不确定时，自然语言描述

locator 优先级: accessibilityId > text > id > class > xpath

**重要：坚决禁止在非 vision 模型下截图猜坐标。**

## 简写规则

- `- tapOn: "Login"` 等价于 `- tapOn: { text: "Login" }`（text locator）
- `- launchApp` 等价于无参启动
- `- assertAi: "page loaded"` 等价于 `- assertAi: { assertion: "page loaded" }`

只在需要额外参数时使用完整形式。

## 断言选择指南

- **精确值校验** → assertText (equals/contains/matches)
- **元素存在性** → assertVisible / assertNotVisible
- **状态校验** → assertEnabled / assertChecked
- **视觉/复杂判断** → assertAi（截图 + AI 判断，optional 默认 false）

## 输出格式

始终输出有效的 YAML 格式：

```yaml
appId: ${APP_ID}
name: "..."
---
- launchApp
- tapOn: "..."
```

## 禁止事项

- 不要猜测元素 ID，不确定时用 target 自然语言描述
- 不要使用未定义的命令
- 不要使用 XPath 除非绝对必要
- 不要过度使用 waitSeconds，优先用 waitVisible
- 不要在一个步骤中组合多个操作
- 坚决禁止在非 vision 模型下截图猜坐标
- assertAi 的 optional 默认为 false，不要随意设为 true
```

### 7.2 Few-shot Examples

```markdown
## 示例 1: 简单登录测试

用户: "测试登录功能，用户名 test@example.com，密码 123456"

```yaml
appId: ${APP_ID}
name: "Login flow test"
priority: p0
tags: [smoke, login]
env:
  USERNAME: "test@example.com"
  PASSWORD: "123456"
---
- launchApp

- tapOn: "Login"

- inputText:
    text: "${USERNAME}"
    element: "Email input"
    clearFirst: true

- inputText:
    text: "${PASSWORD}"
    element: "Password input"

- tapOn: "Confirm login"

- assertVisible: "Welcome"

- assertAi:
    assertion: "page shows login success with welcome message and avatar"
    label: "Login success check"
```

## 示例 2: 使用 W3C 原语的高级操作

```yaml
appId: ${APP_ID}
name: "Pinch zoom test"
tags: [gesture]
---
# 双指缩放 — 高阶命令无法表达，使用原语
- performActions:
    actions:
      - type: pointer
        id: finger1
        parameters: { pointerType: touch }
        actions:
          - { type: pointerMove, x: 200, y: 400 }
          - { type: pointerDown, button: 0 }
          - { type: pointerMove, x: 100, y: 300, duration: 500 }
          - { type: pointerUp, button: 0 }
      - type: pointer
        id: finger2
        parameters: { pointerType: touch }
        actions:
          - { type: pointerMove, x: 200, y: 400 }
          - { type: pointerDown, button: 0 }
          - { type: pointerMove, x: 300, y: 500, duration: 500 }
          - { type: pointerUp, button: 0 }

- assertAi: "the map has zoomed out"

# 使用 execute method 获取剪贴板
- executeMethod:
    method: "mobile: getClipboard"
    args:
      contentType: "plaintext"
```

## 示例 3: 使用双层定位

```yaml
appId: ${APP_ID}
name: "Dual layer locator demo"
---
# text locator (简写，推荐)
- tapOn: "Settings and more"

# locator 精确定位 (优先)
- tapOn:
    locator:
      accessibilityId: "SettingsButton"

# text + locator 组合
- tapOn:
    text: "Settings button"
    locator:
      accessibilityId: "SettingsButton"

# target 语义补充 (locator 不确定时)
- tapOn:
    target: "the three-dot menu button on top right"

# 关系定位消歧
- inputText:
    text: "123456"
    element: "Password input"
    locator:
      text: "Password"
    below: "Username"
```
```

---

## 8. 示例与最佳实践

### 8.1 完整示例：Edge macOS Settings 测试

```yaml
appId: ${APP_ID}
name: "Search in settings search box"
description: "验证设置页面搜索功能"
priority: p0
tags: [regression, settings]
preconditions:
  - runFlow: shared/launch_edge.yaml
---
- tapOn: "Settings and more"

- tapOn: "Settings"

- assertAi:
    assertion: "the settings page should be opened"
    label: "Settings page loaded"

- assertText:
    element: "Address bar"
    locator:
      accessibilityId: "addressBar"
    contains: "edge://settings"

- inputText:
    text: "Privacy"
    element: "settings search box"

- assertAi:
    assertion: "search results display relevant settings related to Privacy"
    label: "Privacy search results"

- clearText:
    element: "settings search box"

- assertAi:
    assertion: "search results reset to show all settings categories"
    label: "Search reset"

- inputText:
    text: "123"
    element: "settings search box"

- assertVisible: "No search results found"
```

### 8.2 完整示例：Edge Android Weather Mini-app

```yaml
appId: ${APP_ID}
name: "Weather mini-app UI"
description: "测试天气小程序界面"
priority: p0
tags: [regression, mini_app]
---
- tapOn: "weather widget icon on NTP"

- if:
    condition:
      visible: "Allow this time"
    then:
      - tapOn: "Allow this time"

- if:
    condition:
      visible: "Only this time"
    then:
      - tapOn: "Only this time"

- if:
    condition:
      visible: "I Accept"
    then:
      - tapOn: "I Accept"

- if:
    condition:
      visible: "Maybe later"
    then:
      - tapOn: "Maybe later"

- assertAi:
    assertion: "MSN Weather page is shown with weather information"
    label: "Weather loaded"

- tapOn: "Hourly Forecast"

- assertAi:
    assertion: "Hourly Forecast page is displayed with hourly weather data"
    label: "Hourly page"
```

### 8.3 完整示例：带 retry 和 session restore

```yaml
appId: ${APP_ID}
name: "Restore previous session tabs"
priority: p0
tags: [regression, settings]
---
- openUrl: "edge://settings/startHomeNTP"

- tapOn: "Open tabs from the previous session"

- pressKey:
    key: "cmd+t"

- openUrl: "https://www.bing.com"

- waitSeconds: 2

- killApp
- launchApp

- retry:
    maxRetries: 3
    steps:
      - assertAi:
          assertion: "edge://settings/startHomeNTP tab is restored"
          label: "Settings tab restored"

- assertAi:
    assertion: "https://www.bing.com tab is restored"
    label: "Bing tab restored"
```

### 8.4 最佳实践

```markdown
## DO

1. **使用有意义的 name**
   - 好: `name: "User login flow test"`
   - 差: `name: "test1"`

2. **优先使用 locator 精确定位**
   - 好: `- tapOn: { locator: { accessibilityId: "btn_login" } }`
   - 差: `- tapOn: { locator: { xpath: "//Button[1]" } }`

3. **字符串简写用于稳定 text**
   - 好: `- tapOn: "Login"` (text locator, 稳定)
   - 差: 不确定 text 时不要猜，用 target

4. **locator 不确定时用 target**
   - `- tapOn: { target: "the button with three dots" }`

5. **使用 waitVisible 而非 waitSeconds**
   - 好: `- waitVisible: "Done"`
   - 差: `- waitSeconds: 5`

6. **精确值用 assertText，视觉判断用 assertAi**
   - URL: `- assertText: { element: "Address bar", contains: "edge://settings" }`
   - 主题: `- assertAi: "the browser theme is dark"`

7. **使用变量避免硬编码**
   - 好: `text: "${USERNAME}"`
   - 差: `text: "test@example.com"`

8. **assertAi 需要 soft assert 时显式声明**
   - `- assertAi: { assertion: "...", optional: true }`

9. **高阶命令无法覆盖时使用 W3C 原语**
   - 双指手势: `performActions`
   - 平台特有 API: `executeMethod`

## DON'T

1. **不要猜测元素 ID** — 不确定时用 target 自然语言
2. **不要滥用 XPath** — 脆弱，维护成本高
3. **不要滥用 waitSeconds** — 优先用 waitVisible/waitGone
4. **不要一步做太多事** — 每个 step 只做一件事
5. **不要用 index** — 优先用关系定位 (below/above/near)
6. **不要默认 assertAi optional: true** — 失败应阻断，除非显式声明
7. **不要在高阶命令能解决时用 performActions** — 保持可读性
```

---

## 附录 A: 命令速查表

| 命令 | 简写形式 | 简写含义 | 用途 |
|------|---------|---------|------|
| `launchApp` | `- launchApp` | 无参启动 | 启动应用 |
| `killApp` | `- killApp` | 无参关闭 | 关闭应用 |
| `clearData` | `- clearData` | 无参清除 | 清除数据 |
| `tapOn` | `- tapOn: "text"` | `{ text: "text" }` | 点击元素 |
| `longPress` | `- longPress: "text"` | `{ text: "text" }` | 长按元素 |
| `doubleTap` | `- doubleTap: "text"` | `{ text: "text" }` | 双击元素 |
| `rightClick` | `- rightClick: "text"` | `{ text: "text" }` | 右键点击 |
| `inputText` | `- inputText: "content"` | `{ text: "content" }` | 输入文本 |
| `clearText` | `- clearText` | 无参清焦点 | 清除文本 |
| `swipe` | `- swipe: "up"` | `{ direction: "up" }` | 滑动 |
| `scroll` | - | - | 滚动到元素 |
| `drag` | - | - | 拖拽 |
| `assertVisible` | `- assertVisible: "text"` | `{ text: "text" }` | 断言可见 |
| `assertNotVisible` | `- assertNotVisible: "text"` | `{ text: "text" }` | 断言不可见 |
| `assertText` | - | - | 断言文本 |
| `assertEnabled` | - | - | 断言可用 |
| `assertChecked` | - | - | 断言勾选 |
| `assertAi` | `- assertAi: "desc"` | `{ assertion: "desc" }` | AI 断言 |
| `waitVisible` | `- waitVisible: "text"` | `{ text: "text" }` | 等待出现 |
| `waitGone` | `- waitGone: "text"` | `{ text: "text" }` | 等待消失 |
| `waitText` | - | - | 等待文本 |
| `waitSeconds` | `- waitSeconds: 2` | 秒数 | 固定等待 |
| `back` | `- back` | - | 返回 |
| `home` | `- home` | - | 回主屏 |
| `openUrl` | `- openUrl: "url"` | `{ url: "url" }` | 打开链接 |
| `pressKey` | `- pressKey: "enter"` | `{ key: "enter" }` | 按键 |
| `setOrientation` | `- setOrientation: "landscape"` | 方向值 | 屏幕方向 |
| `setLocation` | - | - | 模拟 GPS |
| `screenshot` | `- screenshot: "name"` | 文件名 | 截图 |
| `startRecording` | `- startRecording: "name"` | 文件名 | 开始录屏 |
| `stopRecording` | `- stopRecording` | - | 停止录屏 |
| `if` | - | - | 条件执行 |
| `retry` | - | - | 重试 |
| `repeat` | - | - | 循环 |
| `runFlow` | `- runFlow: "file.yaml"` | 文件路径 | 子流程 |
| `setVariable` | - | - | 设置变量 |
| `extractText` | - | - | 提取文本 |
| `performActions` | - | - | W3C Actions |
| `releaseActions` | `- releaseActions` | - | 释放输入 |
| `executeMethod` | - | - | Execute Method |

## 附录 B: 与 Maestro 的差异

| 特性 | Maestro | FSQ 2.0 |
|------|---------|---------|
| 文件格式 | appId + --- + commands | appId/name/tags/env + --- + commands |
| 命令命名 | camelCase | camelCase (对齐) |
| 元素定位 | text/id 直接用 | locator > text > target 三层 |
| 字符串简写 | 落到 text selector | 落到 text locator (对齐) |
| 定位策略 | 固定策略 | executor 决策：locator → text → target → repair |
| AI 断言 | `assertWithAI:` (optional 默认 true) | `assertAi:` (optional 默认 false) |
| 传统断言 | `assertVisible:` 等 | `assertVisible` 等 (保留完整) |
| 右键操作 | 不支持 | `rightClick` (桌面端) |
| W3C 原语 | 不暴露 | `performActions` / `releaseActions` / `executeMethod` |
| 流程控制 | `runFlow:` | `runFlow:` + `retry:` + `repeat:` |
| Schema 约束 | 无官方 Schema | 完整 JSON Schema (v2 提供) |
| 平台管理 | 单文件多平台 | 一个平台一个仓库 |
| 元数据 | appId 仅 | appId / name / priority / tags / env |
| 环境变量 | env 单层 | 全局 env (执行器传入) + 局部 env (头部覆盖) |
| 前置条件 | 无 | preconditions |

---

*文档版本: 3.0 — Maestro-like 格式重写*
