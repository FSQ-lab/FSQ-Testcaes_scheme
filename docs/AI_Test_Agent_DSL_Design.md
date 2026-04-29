# AI 自动化测试 Agent DSL 设计文档

> 基于 Maestro 架构分析，为 AI Agent 驱动的移动端自动化测试设计 DSL 与 Schema

---

## 目录

1. [设计目标](#1-设计目标)
2. [DSL 架构总览](#2-dsl-架构总览)
3. [命令集设计](#3-命令集设计)
4. [元素选择器设计](#4-元素选择器设计)
5. [流程控制设计](#5-流程控制设计)
6. [JSON Schema 完整定义](#6-json-schema-完整定义)
7. [AI 提示词配套](#7-ai-提示词配套)
8. [与 Appium 的映射](#8-与-appium-的映射)
9. [示例与最佳实践](#9-示例与最佳实践)

---

## 1. 设计目标

### 1.1 核心原则

| 原则 | 说明 | Maestro 参考 |
|------|------|-------------|
| **AI 友好** | 命令集小（<40），语义明确，AI 容易掌握 | Maestro 约 40 个命令 |
| **渐进复杂** | 简单场景简单写，复杂场景有能力 | 支持字符串/对象双态 |
| **类型安全** | JSON Schema 约束，减少 AI 生成错误 | sealed interface 设计 |
| **可执行** | 直接映射到 Appium API | Command → Driver 调用 |
| **可扩展** | 支持 AI 断言等高级特性 | assertWithAI 设计 |

### 1.2 与 Maestro 的对比定位

```
Maestro: 人类编写为主，AI 辅助生成
   ↓
我们: AI 生成为主，人类审查确认
   ↓
关键差异:
- 更严格的 Schema 约束
- 更详细的错误反馈
- 单步执行 + 状态观察
- AI 专用的恢复策略
```

---

## 2. DSL 架构总览

### 2.1 三层架构

```
┌─────────────────────────────────────────────────────────────────┐
│                         YAML/JSON 层                            │
│  - 用户/AI 编写的测试脚本                                       │
│  - 支持 YAML 和 JSON 两种格式                                   │
└────────────────────────────┬────────────────────────────────────┘
                             │ JSON Schema 验证
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                         命令模型层                              │
│  - TypeScript/Python 类型定义                                   │
│  - 命令解析与验证                                               │
│  - 脚本变量求值 (${...})                                        │
└────────────────────────────┬────────────────────────────────────┘
                             │ 命令执行
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                         执行引擎层                              │
│  - Appium WebDriver 调用                                        │
│  - 屏幕状态观察                                                 │
│  - 错误处理与恢复                                               │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Flow 文件结构

```yaml
# ═══════════════════════════════════════════════════════════════
# 配置区 (必须)
# ═══════════════════════════════════════════════════════════════
config:
  app_id: "com.example.app"          # Android 包名 或 iOS Bundle ID
  name: "登录流程测试"                # 流程名称
  description: "验证用户登录功能"     # 流程描述
  timeout: 30000                      # 全局超时 (ms)
  retry_on_fail: true                 # 失败时是否允许 AI 重试
  env:                                # 环境变量
    BASE_URL: "https://api.example.com"
    USERNAME: "test@example.com"

# ═══════════════════════════════════════════════════════════════
# 步骤区 (必须)
# ═══════════════════════════════════════════════════════════════
steps:
  - launch_app

  - tap: "登录"

  - input_text:
      text: "${USERNAME}"
      element:
        id: "input_email"

  - assert_visible: "欢迎回来"
```

---

## 3. 命令集设计

### 3.1 命令分类总览 (共 36 个命令)

```
┌─────────────────────────────────────────────────────────────────┐
│                      命令分类 (36 个)                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  应用控制 (5)     交互操作 (8)      断言验证 (6)               │
│  ─────────────    ─────────────     ─────────────              │
│  launch_app       tap               assert_visible              │
│  kill_app         long_press        assert_not_visible          │
│  clear_data       double_tap        assert_text                 │
│  install_app      input_text        assert_enabled              │
│  set_permissions  clear_text        assert_checked              │
│                   swipe             assert_ai                   │
│                   scroll                                        │
│                   drag                                          │
│                                                                 │
│  等待命令 (4)     导航命令 (4)      设备控制 (5)               │
│  ─────────────    ─────────────     ─────────────              │
│  wait_visible     back              set_orientation             │
│  wait_gone        home              set_location                │
│  wait_text        open_url          set_network                 │
│  wait_seconds     press_key         screenshot                  │
│                                     start_recording             │
│                                                                 │
│  流程控制 (4)                                                   │
│  ─────────────                                                  │
│  if                                                             │
│  repeat                                                         │
│  run_flow                                                       │
│  set_variable                                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 命令详细定义

#### 3.2.1 应用控制命令

```yaml
# ─────────────────────────────────────────────────────────────────
# launch_app - 启动应用
# ─────────────────────────────────────────────────────────────────
# 简单形式
- launch_app

# 完整形式
- launch_app:
    app_id: "com.example.app"      # 可选，默认使用 config.app_id
    clear_data: false              # 启动前是否清除数据
    wait_for_ready: true           # 等待应用就绪
    timeout: 10000                 # 启动超时 (ms)
    arguments:                     # 启动参数
      debug: true
      env: "staging"

# ─────────────────────────────────────────────────────────────────
# kill_app - 强制关闭应用
# ─────────────────────────────────────────────────────────────────
- kill_app
- kill_app:
    app_id: "com.example.app"

# ─────────────────────────────────────────────────────────────────
# clear_data - 清除应用数据
# ─────────────────────────────────────────────────────────────────
- clear_data
- clear_data:
    app_id: "com.example.app"

# ─────────────────────────────────────────────────────────────────
# install_app - 安装应用
# ─────────────────────────────────────────────────────────────────
- install_app:
    path: "/path/to/app.apk"       # 或 .ipa
    replace: true                   # 是否覆盖安装

# ─────────────────────────────────────────────────────────────────
# set_permissions - 设置权限
# ─────────────────────────────────────────────────────────────────
- set_permissions:
    app_id: "com.example.app"      # 可选
    permissions:
      camera: "allow"              # allow / deny / ask
      location: "allow"
      notifications: "deny"
      # 或使用通配符
      all: "allow"
```

#### 3.2.2 交互操作命令

```yaml
# ─────────────────────────────────────────────────────────────────
# tap - 点击元素
# ─────────────────────────────────────────────────────────────────
# 简单形式 (按文本)
- tap: "登录"

# 完整形式
- tap:
    # 选择器 (三选一)
    text: "登录"                   # 文本匹配 (支持正则)
    id: "btn_login"                # 元素 ID
    point: [100, 200]              # 屏幕坐标

    # 定位修饰
    index: 0                       # 多个匹配时选第几个
    below: "用户名"                # 位于某元素下方
    above: "忘记密码"              # 位于某元素上方
    near: "图标"                   # 靠近某元素

    # 行为修饰
    timeout: 5000                  # 等待元素出现
    retry: 3                       # 失败重试次数
    optional: false                # 失败是否中断流程

# ─────────────────────────────────────────────────────────────────
# long_press - 长按
# ─────────────────────────────────────────────────────────────────
- long_press: "删除"
- long_press:
    text: "删除"
    duration: 1000                 # 长按时长 (ms)

# ─────────────────────────────────────────────────────────────────
# double_tap - 双击
# ─────────────────────────────────────────────────────────────────
- double_tap: "点赞"
- double_tap:
    text: "点赞"
    interval: 100                  # 两次点击间隔 (ms)

# ─────────────────────────────────────────────────────────────────
# input_text - 输入文本
# ─────────────────────────────────────────────────────────────────
# 简单形式 (输入到当前焦点)
- input_text: "hello world"

# 完整形式
- input_text:
    text: "${USERNAME}"            # 支持变量
    element:                       # 目标输入框 (可选)
      id: "input_email"
    clear_first: true              # 输入前清空
    hide_keyboard: true            # 输入后隐藏键盘

# ─────────────────────────────────────────────────────────────────
# clear_text - 清除文本
# ─────────────────────────────────────────────────────────────────
- clear_text                       # 清除当前焦点
- clear_text:
    element:
      id: "input_email"
    characters: 10                 # 或指定删除字符数

# ─────────────────────────────────────────────────────────────────
# swipe - 滑动
# ─────────────────────────────────────────────────────────────────
# 方向滑动
- swipe: "up"                      # up / down / left / right

# 完整形式
- swipe:
    direction: "up"
    distance: "medium"             # short / medium / long
    duration: 500                  # 滑动时长 (ms)
    element:                       # 在指定元素上滑动
      id: "list_container"
    # 或使用坐标
    from: [200, 800]
    to: [200, 200]

# ─────────────────────────────────────────────────────────────────
# scroll - 滚动到元素可见
# ─────────────────────────────────────────────────────────────────
- scroll:
    to: "第 20 条"                 # 滚动直到该元素可见
    direction: "down"              # up / down
    max_scrolls: 10                # 最大滚动次数
    timeout: 30000

# ─────────────────────────────────────────────────────────────────
# drag - 拖拽
# ─────────────────────────────────────────────────────────────────
- drag:
    from:
      text: "任务 A"
    to:
      text: "已完成"
    duration: 1000
```

#### 3.2.3 断言验证命令

```yaml
# ─────────────────────────────────────────────────────────────────
# assert_visible - 断言元素可见
# ─────────────────────────────────────────────────────────────────
- assert_visible: "欢迎"

- assert_visible:
    text: "欢迎.*"                 # 正则匹配
    timeout: 5000                  # 等待超时
    optional: false                # 失败是否中断

# ─────────────────────────────────────────────────────────────────
# assert_not_visible - 断言元素不可见
# ─────────────────────────────────────────────────────────────────
- assert_not_visible: "加载中"

- assert_not_visible:
    id: "loading_spinner"
    timeout: 10000

# ─────────────────────────────────────────────────────────────────
# assert_text - 断言元素文本内容
# ─────────────────────────────────────────────────────────────────
- assert_text:
    element:
      id: "price_label"
    equals: "¥99.00"               # 精确匹配
    # 或
    contains: "99"                 # 包含
    # 或
    matches: "¥\\d+\\.\\d{2}"      # 正则匹配

# ─────────────────────────────────────────────────────────────────
# assert_enabled - 断言元素可用状态
# ─────────────────────────────────────────────────────────────────
- assert_enabled:
    element:
      id: "submit_button"
    enabled: true                  # true = 可用, false = 禁用

# ─────────────────────────────────────────────────────────────────
# assert_checked - 断言勾选状态
# ─────────────────────────────────────────────────────────────────
- assert_checked:
    element:
      text: "记住密码"
    checked: true

# ─────────────────────────────────────────────────────────────────
# assert_ai - AI 视觉断言 (兜底)
# ─────────────────────────────────────────────────────────────────
- assert_ai: "页面显示登录成功，有欢迎语和用户头像"

- assert_ai:
    assertion: "购物车显示 3 件商品，总价在 ¥100-200 之间"
    confidence: 0.8                # AI 置信度阈值
    optional: true                 # AI 断言建议设为 optional
```

#### 3.2.4 等待命令

```yaml
# ─────────────────────────────────────────────────────────────────
# wait_visible - 等待元素出现
# ─────────────────────────────────────────────────────────────────
- wait_visible: "加载完成"

- wait_visible:
    text: "加载完成"
    timeout: 30000
    poll_interval: 500             # 轮询间隔

# ─────────────────────────────────────────────────────────────────
# wait_gone - 等待元素消失
# ─────────────────────────────────────────────────────────────────
- wait_gone: "加载中..."

- wait_gone:
    id: "loading_spinner"
    timeout: 30000

# ─────────────────────────────────────────────────────────────────
# wait_text - 等待文本内容变化
# ─────────────────────────────────────────────────────────────────
- wait_text:
    element:
      id: "status_label"
    contains: "完成"
    timeout: 60000

# ─────────────────────────────────────────────────────────────────
# wait_seconds - 固定等待 (尽量少用)
# ─────────────────────────────────────────────────────────────────
- wait_seconds: 2
```

#### 3.2.5 导航命令

```yaml
# ─────────────────────────────────────────────────────────────────
# back - 返回
# ─────────────────────────────────────────────────────────────────
- back

# ─────────────────────────────────────────────────────────────────
# home - 回到主屏幕
# ─────────────────────────────────────────────────────────────────
- home

# ─────────────────────────────────────────────────────────────────
# open_url - 打开链接
# ─────────────────────────────────────────────────────────────────
- open_url: "https://example.com"

- open_url:
    url: "myapp://product/123"     # Deep Link
    in_app: true                   # 是否在应用内打开

# ─────────────────────────────────────────────────────────────────
# press_key - 按键
# ─────────────────────────────────────────────────────────────────
- press_key: "enter"               # enter / tab / escape / delete / ...

- press_key:
    key: "volume_up"
    times: 3                       # 重复次数
```

#### 3.2.6 设备控制命令

```yaml
# ─────────────────────────────────────────────────────────────────
# set_orientation - 设置屏幕方向
# ─────────────────────────────────────────────────────────────────
- set_orientation: "landscape"     # portrait / landscape

# ─────────────────────────────────────────────────────────────────
# set_location - 模拟 GPS 位置
# ─────────────────────────────────────────────────────────────────
- set_location:
    latitude: 39.9042
    longitude: 116.4074
    altitude: 50                   # 可选

# ─────────────────────────────────────────────────────────────────
# set_network - 网络状态
# ─────────────────────────────────────────────────────────────────
- set_network:
    wifi: true
    mobile_data: false
    airplane_mode: false

# ─────────────────────────────────────────────────────────────────
# screenshot - 截图
# ─────────────────────────────────────────────────────────────────
- screenshot: "login_page"

- screenshot:
    name: "login_page"
    crop:                          # 裁剪到指定元素
      id: "form_container"

# ─────────────────────────────────────────────────────────────────
# start_recording / stop_recording - 录屏
# ─────────────────────────────────────────────────────────────────
- start_recording: "test_video"
- stop_recording
```

#### 3.2.7 流程控制命令

```yaml
# ─────────────────────────────────────────────────────────────────
# if - 条件执行
# ─────────────────────────────────────────────────────────────────
- if:
    condition:
      visible: "登录按钮"          # 或 not_visible / platform / expression
    then:
      - tap: "登录按钮"
      - wait_visible: "首页"
    else:                          # 可选
      - assert_visible: "已登录"

# 平台条件
- if:
    condition:
      platform: "android"          # android / ios
    then:
      - tap:
          id: "android_specific_button"

# 表达式条件
- if:
    condition:
      expression: "${retryCount < 3}"
    then:
      - tap: "重试"

# ─────────────────────────────────────────────────────────────────
# repeat - 循环
# ─────────────────────────────────────────────────────────────────
# 固定次数
- repeat:
    times: 3
    steps:
      - tap: "下一页"
      - wait_seconds: 1

# 条件循环
- repeat:
    while:
      visible: "加载更多"
    max_times: 10                  # 防止无限循环
    steps:
      - tap: "加载更多"
      - wait_seconds: 2

# ─────────────────────────────────────────────────────────────────
# run_flow - 调用子流程
# ─────────────────────────────────────────────────────────────────
- run_flow: "flows/login.yaml"

- run_flow:
    file: "flows/login.yaml"
    condition:
      not_visible: "已登录"
    env:
      USERNAME: "test@example.com"
      PASSWORD: "secret123"

# 内联子流程
- run_flow:
    steps:
      - tap: "设置"
      - tap: "退出登录"
    condition:
      visible: "已登录"

# ─────────────────────────────────────────────────────────────────
# set_variable - 设置变量
# ─────────────────────────────────────────────────────────────────
- set_variable:
    name: "retryCount"
    value: 0

- set_variable:
    name: "retryCount"
    expression: "${retryCount + 1}"
```

---

## 4. 元素选择器设计

### 4.1 选择器类型

```yaml
# ═══════════════════════════════════════════════════════════════
# 选择器支持两种形式
# ═══════════════════════════════════════════════════════════════

# 形式 1: 简单字符串 (默认按文本匹配)
- tap: "登录"                       # 等价于 { text: "登录" }

# 形式 2: 对象形式 (精确控制)
- tap:
    text: "登录"
    id: "btn_login"
    # ... 更多选项
```

### 4.2 完整选择器定义

```yaml
selector:
  # ═══════════════════════════════════════════════════════════════
  # 基础定位 (选择其一或组合)
  # ═══════════════════════════════════════════════════════════════
  text: "登录"                     # 文本内容 (支持正则)
  id: "btn_login"                  # 元素 ID / resource-id / accessibility-id
  class: "android.widget.Button"   # 元素类名
  xpath: "//Button[@text='登录']"  # XPath (尽量避免)

  # ═══════════════════════════════════════════════════════════════
  # 索引定位
  # ═══════════════════════════════════════════════════════════════
  index: 0                         # 多个匹配时取第几个 (从 0 开始)

  # ═══════════════════════════════════════════════════════════════
  # 状态过滤
  # ═══════════════════════════════════════════════════════════════
  enabled: true                    # 是否可用
  visible: true                    # 是否可见 (默认 true)
  selected: false                  # 是否选中
  checked: true                    # 是否勾选
  focused: false                   # 是否获得焦点

  # ═══════════════════════════════════════════════════════════════
  # 关系定位 (值为另一个选择器)
  # ═══════════════════════════════════════════════════════════════
  below: "用户名"                  # 在某元素下方
  above: "忘记密码"                # 在某元素上方
  left_of: "取消"                  # 在某元素左侧
  right_of: "确认"                 # 在某元素右侧
  near: "图标"                     # 靠近某元素
  child_of:                        # 是某元素的子元素
    id: "login_form"
  contains:                        # 包含某子元素
    text: "图标"

  # ═══════════════════════════════════════════════════════════════
  # 行为修饰 (仅用于交互命令)
  # ═══════════════════════════════════════════════════════════════
  timeout: 10000                   # 等待元素出现的超时 (ms)
  retry: 3                         # 操作失败重试次数
  optional: false                  # 失败是否中断流程
```

### 4.3 选择器优先级规则 (给 AI 的指导)

```markdown
## 选择器选择优先级

1. **优先使用 text**
   - 最稳定，不受布局变化影响
   - 用户可见，易于理解和维护
   - 示例: `- tap: "登录"`

2. **其次使用 id**
   - 当文本不唯一或经常变化时使用
   - 需要从 View Hierarchy 获取确切 ID
   - 示例: `- tap: { id: "btn_login" }`

3. **使用关系定位处理模糊情况**
   - 当有多个相同文本时，用 below/above 区分
   - 示例: `- tap: { text: "确认", below: "订单金额" }`

4. **避免使用 xpath**
   - XPath 脆弱，布局变化易失效
   - 仅在其他方式都不可行时使用

5. **避免使用 index**
   - index 依赖顺序，不稳定
   - 优先用关系定位替代
```

---

## 5. 流程控制设计

### 5.1 条件表达式

```yaml
condition:
  # 元素条件
  visible: "登录按钮"              # 元素可见
  not_visible: "加载中"            # 元素不可见

  # 平台条件
  platform: "android"              # android / ios

  # 表达式条件 (JavaScript)
  expression: "${count > 0 && status == 'ready'}"

  # 组合条件 (AND 关系)
  visible: "登录按钮"
  platform: "android"
```

### 5.2 变量系统

```yaml
# 内置变量
${platform}                        # 当前平台 (android/ios)
${device_name}                     # 设备名称
${timestamp}                       # 当前时间戳

# 环境变量 (来自 config.env)
${USERNAME}
${PASSWORD}

# 自定义变量
- set_variable:
    name: "counter"
    value: 0

- set_variable:
    name: "counter"
    expression: "${counter + 1}"

# 从元素提取
- extract_text:
    element:
      id: "price_label"
    variable: "price"

- assert_ai:
    assertion: "价格合理"
    extract:
      variable: "ai_result"        # AI 返回结果存入变量
```

---

## 6. JSON Schema 完整定义

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://example.com/ai-test-dsl.schema.json",
  "title": "AI Test Agent DSL",
  "description": "AI 驱动的移动端自动化测试 DSL Schema",
  "type": "object",

  "required": ["steps"],

  "properties": {
    "config": {
      "$ref": "#/definitions/Config"
    },
    "steps": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/Step"
      },
      "minItems": 1
    }
  },

  "definitions": {

    "Config": {
      "type": "object",
      "properties": {
        "app_id": {
          "type": "string",
          "description": "应用包名 (Android) 或 Bundle ID (iOS)"
        },
        "name": {
          "type": "string",
          "description": "测试流程名称"
        },
        "description": {
          "type": "string",
          "description": "测试流程描述"
        },
        "timeout": {
          "type": "integer",
          "minimum": 1000,
          "maximum": 300000,
          "default": 30000,
          "description": "全局超时时间 (ms)"
        },
        "retry_on_fail": {
          "type": "boolean",
          "default": true,
          "description": "失败时是否允许 AI 重试"
        },
        "env": {
          "type": "object",
          "additionalProperties": {
            "type": "string"
          },
          "description": "环境变量"
        }
      }
    },

    "Selector": {
      "description": "元素选择器",
      "oneOf": [
        {
          "type": "string",
          "description": "简单文本匹配"
        },
        {
          "type": "object",
          "properties": {
            "text": {
              "type": "string",
              "description": "文本匹配 (支持正则)"
            },
            "id": {
              "type": "string",
              "description": "元素 ID"
            },
            "class": {
              "type": "string",
              "description": "元素类名"
            },
            "xpath": {
              "type": "string",
              "description": "XPath 表达式 (不推荐)"
            },
            "index": {
              "type": "integer",
              "minimum": 0,
              "description": "多个匹配时取第几个"
            },
            "enabled": {
              "type": "boolean",
              "description": "是否可用"
            },
            "visible": {
              "type": "boolean",
              "default": true,
              "description": "是否可见"
            },
            "selected": {
              "type": "boolean"
            },
            "checked": {
              "type": "boolean"
            },
            "focused": {
              "type": "boolean"
            },
            "below": {
              "$ref": "#/definitions/Selector"
            },
            "above": {
              "$ref": "#/definitions/Selector"
            },
            "left_of": {
              "$ref": "#/definitions/Selector"
            },
            "right_of": {
              "$ref": "#/definitions/Selector"
            },
            "near": {
              "$ref": "#/definitions/Selector"
            },
            "child_of": {
              "$ref": "#/definitions/Selector"
            },
            "contains": {
              "$ref": "#/definitions/Selector"
            },
            "timeout": {
              "type": "integer",
              "minimum": 0,
              "maximum": 60000,
              "description": "等待超时 (ms)"
            },
            "retry": {
              "type": "integer",
              "minimum": 0,
              "maximum": 10,
              "description": "重试次数"
            },
            "optional": {
              "type": "boolean",
              "default": false,
              "description": "失败是否继续"
            }
          },
          "additionalProperties": false
        }
      ]
    },

    "Condition": {
      "type": "object",
      "properties": {
        "visible": {
          "$ref": "#/definitions/Selector"
        },
        "not_visible": {
          "$ref": "#/definitions/Selector"
        },
        "platform": {
          "type": "string",
          "enum": ["android", "ios"]
        },
        "expression": {
          "type": "string",
          "description": "JavaScript 表达式"
        }
      },
      "additionalProperties": false
    },

    "Step": {
      "description": "测试步骤",
      "oneOf": [
        { "$ref": "#/definitions/LaunchAppStep" },
        { "$ref": "#/definitions/KillAppStep" },
        { "$ref": "#/definitions/TapStep" },
        { "$ref": "#/definitions/LongPressStep" },
        { "$ref": "#/definitions/DoubleTapStep" },
        { "$ref": "#/definitions/InputTextStep" },
        { "$ref": "#/definitions/ClearTextStep" },
        { "$ref": "#/definitions/SwipeStep" },
        { "$ref": "#/definitions/ScrollStep" },
        { "$ref": "#/definitions/AssertVisibleStep" },
        { "$ref": "#/definitions/AssertNotVisibleStep" },
        { "$ref": "#/definitions/AssertTextStep" },
        { "$ref": "#/definitions/AssertAiStep" },
        { "$ref": "#/definitions/WaitVisibleStep" },
        { "$ref": "#/definitions/WaitGoneStep" },
        { "$ref": "#/definitions/WaitSecondsStep" },
        { "$ref": "#/definitions/BackStep" },
        { "$ref": "#/definitions/HomeStep" },
        { "$ref": "#/definitions/OpenUrlStep" },
        { "$ref": "#/definitions/PressKeyStep" },
        { "$ref": "#/definitions/SetOrientationStep" },
        { "$ref": "#/definitions/ScreenshotStep" },
        { "$ref": "#/definitions/IfStep" },
        { "$ref": "#/definitions/RepeatStep" },
        { "$ref": "#/definitions/RunFlowStep" },
        { "$ref": "#/definitions/SetVariableStep" }
      ]
    },

    "LaunchAppStep": {
      "oneOf": [
        {
          "type": "string",
          "const": "launch_app"
        },
        {
          "type": "object",
          "properties": {
            "launch_app": {
              "oneOf": [
                { "type": "null" },
                {
                  "type": "object",
                  "properties": {
                    "app_id": { "type": "string" },
                    "clear_data": { "type": "boolean", "default": false },
                    "wait_for_ready": { "type": "boolean", "default": true },
                    "timeout": { "type": "integer" },
                    "arguments": {
                      "type": "object",
                      "additionalProperties": true
                    }
                  },
                  "additionalProperties": false
                }
              ]
            }
          },
          "required": ["launch_app"],
          "additionalProperties": false
        }
      ]
    },

    "KillAppStep": {
      "oneOf": [
        { "type": "string", "const": "kill_app" },
        {
          "type": "object",
          "properties": {
            "kill_app": {
              "oneOf": [
                { "type": "null" },
                {
                  "type": "object",
                  "properties": {
                    "app_id": { "type": "string" }
                  }
                }
              ]
            }
          },
          "required": ["kill_app"]
        }
      ]
    },

    "TapStep": {
      "type": "object",
      "properties": {
        "tap": {
          "$ref": "#/definitions/Selector"
        }
      },
      "required": ["tap"],
      "additionalProperties": false
    },

    "LongPressStep": {
      "type": "object",
      "properties": {
        "long_press": {
          "oneOf": [
            { "$ref": "#/definitions/Selector" },
            {
              "type": "object",
              "allOf": [
                { "$ref": "#/definitions/Selector" }
              ],
              "properties": {
                "duration": {
                  "type": "integer",
                  "minimum": 500,
                  "maximum": 5000,
                  "default": 1000
                }
              }
            }
          ]
        }
      },
      "required": ["long_press"],
      "additionalProperties": false
    },

    "DoubleTapStep": {
      "type": "object",
      "properties": {
        "double_tap": {
          "oneOf": [
            { "$ref": "#/definitions/Selector" },
            {
              "type": "object",
              "allOf": [
                { "$ref": "#/definitions/Selector" }
              ],
              "properties": {
                "interval": {
                  "type": "integer",
                  "minimum": 50,
                  "maximum": 500,
                  "default": 100
                }
              }
            }
          ]
        }
      },
      "required": ["double_tap"],
      "additionalProperties": false
    },

    "InputTextStep": {
      "type": "object",
      "properties": {
        "input_text": {
          "oneOf": [
            {
              "type": "string",
              "description": "直接输入文本"
            },
            {
              "type": "object",
              "properties": {
                "text": {
                  "type": "string",
                  "description": "要输入的文本"
                },
                "element": {
                  "$ref": "#/definitions/Selector",
                  "description": "目标输入框"
                },
                "clear_first": {
                  "type": "boolean",
                  "default": false
                },
                "hide_keyboard": {
                  "type": "boolean",
                  "default": false
                }
              },
              "required": ["text"],
              "additionalProperties": false
            }
          ]
        }
      },
      "required": ["input_text"],
      "additionalProperties": false
    },

    "ClearTextStep": {
      "oneOf": [
        { "type": "string", "const": "clear_text" },
        {
          "type": "object",
          "properties": {
            "clear_text": {
              "oneOf": [
                { "type": "null" },
                {
                  "type": "object",
                  "properties": {
                    "element": { "$ref": "#/definitions/Selector" },
                    "characters": { "type": "integer", "minimum": 1 }
                  }
                }
              ]
            }
          },
          "required": ["clear_text"]
        }
      ]
    },

    "SwipeStep": {
      "type": "object",
      "properties": {
        "swipe": {
          "oneOf": [
            {
              "type": "string",
              "enum": ["up", "down", "left", "right"]
            },
            {
              "type": "object",
              "properties": {
                "direction": {
                  "type": "string",
                  "enum": ["up", "down", "left", "right"]
                },
                "distance": {
                  "type": "string",
                  "enum": ["short", "medium", "long"],
                  "default": "medium"
                },
                "duration": {
                  "type": "integer",
                  "minimum": 100,
                  "maximum": 3000,
                  "default": 500
                },
                "element": {
                  "$ref": "#/definitions/Selector"
                },
                "from": {
                  "type": "array",
                  "items": { "type": "integer" },
                  "minItems": 2,
                  "maxItems": 2
                },
                "to": {
                  "type": "array",
                  "items": { "type": "integer" },
                  "minItems": 2,
                  "maxItems": 2
                }
              },
              "additionalProperties": false
            }
          ]
        }
      },
      "required": ["swipe"],
      "additionalProperties": false
    },

    "ScrollStep": {
      "type": "object",
      "properties": {
        "scroll": {
          "type": "object",
          "properties": {
            "to": {
              "$ref": "#/definitions/Selector",
              "description": "滚动直到该元素可见"
            },
            "direction": {
              "type": "string",
              "enum": ["up", "down"],
              "default": "down"
            },
            "max_scrolls": {
              "type": "integer",
              "minimum": 1,
              "maximum": 50,
              "default": 10
            },
            "timeout": {
              "type": "integer",
              "default": 30000
            }
          },
          "required": ["to"],
          "additionalProperties": false
        }
      },
      "required": ["scroll"],
      "additionalProperties": false
    },

    "AssertVisibleStep": {
      "type": "object",
      "properties": {
        "assert_visible": {
          "oneOf": [
            { "$ref": "#/definitions/Selector" },
            {
              "type": "object",
              "allOf": [{ "$ref": "#/definitions/Selector" }],
              "properties": {
                "timeout": { "type": "integer" },
                "optional": { "type": "boolean" }
              }
            }
          ]
        }
      },
      "required": ["assert_visible"],
      "additionalProperties": false
    },

    "AssertNotVisibleStep": {
      "type": "object",
      "properties": {
        "assert_not_visible": {
          "oneOf": [
            { "$ref": "#/definitions/Selector" },
            {
              "type": "object",
              "allOf": [{ "$ref": "#/definitions/Selector" }],
              "properties": {
                "timeout": { "type": "integer" },
                "optional": { "type": "boolean" }
              }
            }
          ]
        }
      },
      "required": ["assert_not_visible"],
      "additionalProperties": false
    },

    "AssertTextStep": {
      "type": "object",
      "properties": {
        "assert_text": {
          "type": "object",
          "properties": {
            "element": {
              "$ref": "#/definitions/Selector"
            },
            "equals": { "type": "string" },
            "contains": { "type": "string" },
            "matches": { "type": "string" },
            "timeout": { "type": "integer" },
            "optional": { "type": "boolean" }
          },
          "required": ["element"],
          "oneOf": [
            { "required": ["equals"] },
            { "required": ["contains"] },
            { "required": ["matches"] }
          ],
          "additionalProperties": false
        }
      },
      "required": ["assert_text"],
      "additionalProperties": false
    },

    "AssertAiStep": {
      "type": "object",
      "properties": {
        "assert_ai": {
          "oneOf": [
            {
              "type": "string",
              "description": "AI 断言描述"
            },
            {
              "type": "object",
              "properties": {
                "assertion": {
                  "type": "string",
                  "description": "AI 断言描述"
                },
                "confidence": {
                  "type": "number",
                  "minimum": 0,
                  "maximum": 1,
                  "default": 0.8
                },
                "optional": {
                  "type": "boolean",
                  "default": true
                }
              },
              "required": ["assertion"],
              "additionalProperties": false
            }
          ]
        }
      },
      "required": ["assert_ai"],
      "additionalProperties": false
    },

    "WaitVisibleStep": {
      "type": "object",
      "properties": {
        "wait_visible": {
          "oneOf": [
            { "$ref": "#/definitions/Selector" },
            {
              "type": "object",
              "allOf": [{ "$ref": "#/definitions/Selector" }],
              "properties": {
                "timeout": {
                  "type": "integer",
                  "default": 30000
                },
                "poll_interval": {
                  "type": "integer",
                  "default": 500
                }
              }
            }
          ]
        }
      },
      "required": ["wait_visible"],
      "additionalProperties": false
    },

    "WaitGoneStep": {
      "type": "object",
      "properties": {
        "wait_gone": {
          "oneOf": [
            { "$ref": "#/definitions/Selector" },
            {
              "type": "object",
              "allOf": [{ "$ref": "#/definitions/Selector" }],
              "properties": {
                "timeout": {
                  "type": "integer",
                  "default": 30000
                }
              }
            }
          ]
        }
      },
      "required": ["wait_gone"],
      "additionalProperties": false
    },

    "WaitSecondsStep": {
      "type": "object",
      "properties": {
        "wait_seconds": {
          "type": "number",
          "minimum": 0.1,
          "maximum": 60,
          "description": "等待秒数 (尽量少用)"
        }
      },
      "required": ["wait_seconds"],
      "additionalProperties": false
    },

    "BackStep": {
      "oneOf": [
        { "type": "string", "const": "back" },
        {
          "type": "object",
          "properties": {
            "back": { "type": "null" }
          },
          "required": ["back"]
        }
      ]
    },

    "HomeStep": {
      "oneOf": [
        { "type": "string", "const": "home" },
        {
          "type": "object",
          "properties": {
            "home": { "type": "null" }
          },
          "required": ["home"]
        }
      ]
    },

    "OpenUrlStep": {
      "type": "object",
      "properties": {
        "open_url": {
          "oneOf": [
            { "type": "string", "format": "uri" },
            {
              "type": "object",
              "properties": {
                "url": { "type": "string", "format": "uri" },
                "in_app": { "type": "boolean", "default": false }
              },
              "required": ["url"],
              "additionalProperties": false
            }
          ]
        }
      },
      "required": ["open_url"],
      "additionalProperties": false
    },

    "PressKeyStep": {
      "type": "object",
      "properties": {
        "press_key": {
          "oneOf": [
            {
              "type": "string",
              "enum": ["enter", "tab", "escape", "delete", "backspace",
                       "space", "volume_up", "volume_down", "home", "back"]
            },
            {
              "type": "object",
              "properties": {
                "key": {
                  "type": "string"
                },
                "times": {
                  "type": "integer",
                  "minimum": 1,
                  "maximum": 10,
                  "default": 1
                }
              },
              "required": ["key"],
              "additionalProperties": false
            }
          ]
        }
      },
      "required": ["press_key"],
      "additionalProperties": false
    },

    "SetOrientationStep": {
      "type": "object",
      "properties": {
        "set_orientation": {
          "type": "string",
          "enum": ["portrait", "landscape"]
        }
      },
      "required": ["set_orientation"],
      "additionalProperties": false
    },

    "ScreenshotStep": {
      "type": "object",
      "properties": {
        "screenshot": {
          "oneOf": [
            { "type": "string" },
            {
              "type": "object",
              "properties": {
                "name": { "type": "string" },
                "crop": { "$ref": "#/definitions/Selector" }
              },
              "required": ["name"],
              "additionalProperties": false
            }
          ]
        }
      },
      "required": ["screenshot"],
      "additionalProperties": false
    },

    "IfStep": {
      "type": "object",
      "properties": {
        "if": {
          "type": "object",
          "properties": {
            "condition": {
              "$ref": "#/definitions/Condition"
            },
            "then": {
              "type": "array",
              "items": { "$ref": "#/definitions/Step" },
              "minItems": 1
            },
            "else": {
              "type": "array",
              "items": { "$ref": "#/definitions/Step" }
            }
          },
          "required": ["condition", "then"],
          "additionalProperties": false
        }
      },
      "required": ["if"],
      "additionalProperties": false
    },

    "RepeatStep": {
      "type": "object",
      "properties": {
        "repeat": {
          "type": "object",
          "properties": {
            "times": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100
            },
            "while": {
              "$ref": "#/definitions/Condition"
            },
            "max_times": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "default": 10
            },
            "steps": {
              "type": "array",
              "items": { "$ref": "#/definitions/Step" },
              "minItems": 1
            }
          },
          "required": ["steps"],
          "additionalProperties": false
        }
      },
      "required": ["repeat"],
      "additionalProperties": false
    },

    "RunFlowStep": {
      "type": "object",
      "properties": {
        "run_flow": {
          "oneOf": [
            {
              "type": "string",
              "description": "子流程文件路径"
            },
            {
              "type": "object",
              "properties": {
                "file": {
                  "type": "string",
                  "description": "子流程文件路径"
                },
                "steps": {
                  "type": "array",
                  "items": { "$ref": "#/definitions/Step" },
                  "description": "内联步骤 (与 file 互斥)"
                },
                "condition": {
                  "$ref": "#/definitions/Condition"
                },
                "env": {
                  "type": "object",
                  "additionalProperties": { "type": "string" }
                }
              },
              "oneOf": [
                { "required": ["file"] },
                { "required": ["steps"] }
              ],
              "additionalProperties": false
            }
          ]
        }
      },
      "required": ["run_flow"],
      "additionalProperties": false
    },

    "SetVariableStep": {
      "type": "object",
      "properties": {
        "set_variable": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "pattern": "^[a-zA-Z_][a-zA-Z0-9_]*$"
            },
            "value": {
              "oneOf": [
                { "type": "string" },
                { "type": "number" },
                { "type": "boolean" }
              ]
            },
            "expression": {
              "type": "string",
              "description": "JavaScript 表达式"
            }
          },
          "required": ["name"],
          "oneOf": [
            { "required": ["value"] },
            { "required": ["expression"] }
          ],
          "additionalProperties": false
        }
      },
      "required": ["set_variable"],
      "additionalProperties": false
    }
  }
}
```

---

## 7. AI 提示词配套

### 7.1 System Prompt

```markdown
# 角色定义

你是一个移动端 UI 自动化测试专家。你的任务是根据用户描述或测试需求，生成符合 DSL 规范的测试脚本。

# DSL 规范

## 命令格式

你生成的脚本必须符合以下 JSON Schema 约束。

### 支持的命令列表 (共 36 个)

**应用控制**: launch_app, kill_app, clear_data, install_app, set_permissions
**交互操作**: tap, long_press, double_tap, input_text, clear_text, swipe, scroll, drag
**断言验证**: assert_visible, assert_not_visible, assert_text, assert_enabled, assert_checked, assert_ai
**等待命令**: wait_visible, wait_gone, wait_text, wait_seconds
**导航命令**: back, home, open_url, press_key
**设备控制**: set_orientation, set_location, set_network, screenshot, start_recording
**流程控制**: if, repeat, run_flow, set_variable

### 选择器优先级

1. **优先使用 text** - 最稳定
2. **其次使用 id** - 需确切知道 ID
3. **使用关系定位** - 处理模糊情况 (below, above, near)
4. **避免 xpath** - 太脆弱
5. **避免 index** - 不稳定

### 简单 vs 复杂语法

大多数命令支持简单形式:
- `- tap: "登录"` 等价于 `- tap: { text: "登录" }`
- `- launch_app` 等价于 `- launch_app: null`

只在需要额外参数时使用复杂形式。

## 输出格式

始终输出有效的 YAML 格式，结构如下:

```yaml
config:
  app_id: "..."
  name: "..."
steps:
  - ...
```

## 禁止事项

- ❌ 不要猜测元素 ID，如果不知道就用 text
- ❌ 不要使用未定义的命令
- ❌ 不要使用 XPath 除非绝对必要
- ❌ 不要过度使用 wait_seconds，优先用 wait_visible
- ❌ 不要在一个步骤中组合多个操作
```

### 7.2 Few-shot Examples

```markdown
## 示例 1: 简单登录测试

用户: "测试登录功能，用户名 test@example.com，密码 123456"

```yaml
config:
  app_id: "com.example.app"
  name: "登录测试"

steps:
  - launch_app

  - tap: "登录"

  - input_text:
      text: "test@example.com"
      element:
        id: "input_email"
      clear_first: true

  - input_text:
      text: "123456"
      element:
        id: "input_password"

  - tap: "确认登录"

  - assert_visible: "欢迎"
```

## 示例 2: 带条件的复杂流程

用户: "如果已登录则跳过登录，然后搜索商品并加入购物车"

```yaml
config:
  app_id: "com.example.shop"
  name: "搜索并加购"

steps:
  - launch_app

  - if:
      condition:
        visible: "登录"
      then:
        - tap: "登录"
        - input_text: "user@example.com"
        - input_text: "password"
        - tap: "确认"
        - wait_visible: "首页"

  - tap:
      id: "search_bar"

  - input_text: "iPhone 15"

  - press_key: "enter"

  - wait_gone: "加载中"

  - tap:
      text: "iPhone 15 Pro"
      index: 0

  - scroll:
      to: "加入购物车"
      direction: "down"

  - tap: "加入购物车"

  - assert_visible: "已加入购物车"
```

## 示例 3: 使用关系定位

用户: "在用户名输入框下方的密码框中输入密码"

```yaml
steps:
  - input_text:
      text: "123456"
      element:
        text: "密码"
        below: "用户名"
```
```

---

## 8. 与 Appium 的映射

### 8.1 命令映射表

| DSL 命令 | Appium WebDriver API |
|----------|---------------------|
| `launch_app` | `driver.activate_app(app_id)` 或 `driver.launch_app()` |
| `kill_app` | `driver.terminate_app(app_id)` |
| `clear_data` | `driver.reset()` 或 ADB/XCTest 命令 |
| `tap` | `element.click()` |
| `long_press` | `TouchAction.long_press()` |
| `double_tap` | `TouchAction.tap().tap()` |
| `input_text` | `element.send_keys(text)` |
| `clear_text` | `element.clear()` |
| `swipe` | `driver.swipe(start_x, start_y, end_x, end_y)` |
| `scroll` | `driver.execute_script("mobile: scroll")` |
| `assert_visible` | `WebDriverWait.until(visibility_of_element_located)` |
| `assert_not_visible` | `WebDriverWait.until(invisibility_of_element)` |
| `wait_visible` | `WebDriverWait.until(visibility_of_element_located)` |
| `wait_gone` | `WebDriverWait.until(invisibility_of_element)` |
| `back` | `driver.back()` |
| `home` | `driver.press_keycode(AndroidKey.HOME)` |
| `press_key` | `driver.press_keycode(key)` |
| `set_orientation` | `driver.orientation = LANDSCAPE/PORTRAIT` |
| `set_location` | `driver.set_location(lat, lng, alt)` |
| `screenshot` | `driver.get_screenshot_as_file()` |

### 8.2 选择器映射

| DSL 选择器 | Appium 定位策略 |
|-----------|----------------|
| `text` | `AppiumBy.XPATH("//[contains(@text, '...')]")` 或 `-android uiautomator` |
| `id` | `AppiumBy.ID` 或 `AppiumBy.ACCESSIBILITY_ID` |
| `class` | `AppiumBy.CLASS_NAME` |
| `xpath` | `AppiumBy.XPATH` |

### 8.3 Python 执行器示例

```python
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml

class DSLExecutor:
    def __init__(self, driver):
        self.driver = driver
        self.variables = {}

    def execute(self, script: str):
        """执行 YAML 脚本"""
        flow = yaml.safe_load(script)

        if 'config' in flow:
            self._apply_config(flow['config'])

        for step in flow['steps']:
            self._execute_step(step)

    def _execute_step(self, step):
        """执行单个步骤"""
        if isinstance(step, str):
            # 简单命令: "launch_app", "back", "home"
            getattr(self, f'_cmd_{step}')()
        else:
            # 复杂命令: { tap: "..." }
            cmd_name = list(step.keys())[0]
            cmd_args = step[cmd_name]
            getattr(self, f'_cmd_{cmd_name}')(cmd_args)

    def _cmd_launch_app(self, args=None):
        if args and 'app_id' in args:
            self.driver.activate_app(args['app_id'])
        else:
            self.driver.launch_app()

    def _cmd_tap(self, selector):
        element = self._find_element(selector)
        element.click()

    def _cmd_input_text(self, args):
        if isinstance(args, str):
            # 简单形式: 输入到当前焦点
            active = self.driver.switch_to.active_element
            active.send_keys(args)
        else:
            text = self._evaluate(args['text'])
            if 'element' in args:
                element = self._find_element(args['element'])
                if args.get('clear_first'):
                    element.clear()
                element.send_keys(text)
            else:
                active = self.driver.switch_to.active_element
                active.send_keys(text)

    def _cmd_assert_visible(self, selector):
        timeout = 10
        if isinstance(selector, dict) and 'timeout' in selector:
            timeout = selector['timeout'] / 1000

        locator = self._to_locator(selector)
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def _find_element(self, selector):
        """根据选择器查找元素"""
        locator = self._to_locator(selector)
        timeout = 10
        if isinstance(selector, dict):
            timeout = selector.get('timeout', 10000) / 1000

        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def _to_locator(self, selector):
        """将 DSL 选择器转换为 Appium 定位器"""
        if isinstance(selector, str):
            # 简单字符串 -> 文本匹配
            return (AppiumBy.XPATH, f"//*[contains(@text, '{selector}')]")

        if 'id' in selector:
            return (AppiumBy.ID, selector['id'])

        if 'text' in selector:
            text = selector['text']
            xpath = f"//*[contains(@text, '{text}')]"

            # 处理关系定位
            if 'below' in selector:
                below_text = selector['below'] if isinstance(selector['below'], str) else selector['below'].get('text')
                xpath = f"//*[contains(@text, '{below_text}')]/following::*[contains(@text, '{text}')]"

            return (AppiumBy.XPATH, xpath)

        if 'xpath' in selector:
            return (AppiumBy.XPATH, selector['xpath'])

        raise ValueError(f"无法解析选择器: {selector}")

    def _evaluate(self, value: str) -> str:
        """求值变量表达式 ${...}"""
        import re
        def replace(match):
            var_name = match.group(1)
            return str(self.variables.get(var_name, ''))

        return re.sub(r'\$\{(\w+)\}', replace, value)
```

---

## 9. 示例与最佳实践

### 9.1 完整测试流程示例

```yaml
# ═══════════════════════════════════════════════════════════════
# 电商 App 购买流程测试
# ═══════════════════════════════════════════════════════════════

config:
  app_id: "com.example.shop"
  name: "完整购买流程"
  description: "测试从登录到下单的完整流程"
  timeout: 60000
  env:
    USERNAME: "test@example.com"
    PASSWORD: "Test123456"
    PRODUCT: "iPhone 15 Pro"

steps:
  # ─────────────────────────────────────────────────────────────
  # 1. 启动应用
  # ─────────────────────────────────────────────────────────────
  - launch_app:
      clear_data: true
      wait_for_ready: true

  # ─────────────────────────────────────────────────────────────
  # 2. 登录流程
  # ─────────────────────────────────────────────────────────────
  - tap: "登录/注册"

  - input_text:
      text: "${USERNAME}"
      element:
        text: "请输入手机号/邮箱"
      clear_first: true

  - input_text:
      text: "${PASSWORD}"
      element:
        text: "请输入密码"

  - tap: "登录"

  - wait_gone: "登录中..."

  - assert_visible: "首页"

  # ─────────────────────────────────────────────────────────────
  # 3. 搜索商品
  # ─────────────────────────────────────────────────────────────
  - tap:
      id: "search_bar"

  - input_text: "${PRODUCT}"

  - press_key: "enter"

  - wait_gone: "搜索中"

  - assert_visible: "${PRODUCT}"

  # ─────────────────────────────────────────────────────────────
  # 4. 选择商品
  # ─────────────────────────────────────────────────────────────
  - tap:
      text: "${PRODUCT}"
      index: 0

  - wait_visible: "加入购物车"

  - scroll:
      to: "立即购买"
      direction: "down"

  # ─────────────────────────────────────────────────────────────
  # 5. 选择规格
  # ─────────────────────────────────────────────────────────────
  - tap: "立即购买"

  - wait_visible: "选择规格"

  - tap: "256GB"

  - tap: "黑色"

  - tap: "确定"

  # ─────────────────────────────────────────────────────────────
  # 6. 确认订单
  # ─────────────────────────────────────────────────────────────
  - wait_visible: "确认订单"

  - assert_text:
      element:
        text: "商品名称"
        near: "${PRODUCT}"
      contains: "${PRODUCT}"

  - scroll:
      to: "提交订单"
      direction: "down"

  - tap: "提交订单"

  # ─────────────────────────────────────────────────────────────
  # 7. 验证结果
  # ─────────────────────────────────────────────────────────────
  - wait_visible:
      text: "支付"
      timeout: 10000

  - assert_ai: "页面显示支付方式选择，包含微信支付和支付宝选项"

  - screenshot: "order_success"
```

### 9.2 最佳实践

```markdown
## DO ✅

1. **使用有意义的 config.name**
   - 好: `name: "用户登录流程测试"`
   - 差: `name: "test1"`

2. **优先使用 text 选择器**
   - 好: `- tap: "登录"`
   - 差: `- tap: { xpath: "//android.widget.Button[1]" }`

3. **使用 wait_visible 而非 wait_seconds**
   - 好: `- wait_visible: "加载完成"`
   - 差: `- wait_seconds: 5`

4. **合理使用 optional**
   - AI 断言建议 optional: true
   - 关键断言使用 optional: false (默认)

5. **使用变量避免硬编码**
   - 好: `text: "${USERNAME}"`
   - 差: `text: "test@example.com"`

## DON'T ❌

1. **不要过度使用 XPath**
   - XPath 脆弱，维护成本高

2. **不要猜测 ID**
   - 从 View Hierarchy 获取准确 ID
   - 不确定时用 text

3. **不要滥用 wait_seconds**
   - 只在没有其他选择时使用
   - 时间尽量短 (1-2 秒)

4. **不要一步做太多事**
   - 每个 step 只做一件事
   - 便于定位失败原因

5. **不要忽略错误处理**
   - 使用 optional 处理可接受的失败
   - 使用 if 处理条件分支
```

---

## 附录 A: 命令速查表

| 命令 | 简单形式 | 用途 |
|------|---------|------|
| `launch_app` | `- launch_app` | 启动应用 |
| `kill_app` | `- kill_app` | 关闭应用 |
| `tap` | `- tap: "文本"` | 点击元素 |
| `long_press` | `- long_press: "文本"` | 长按元素 |
| `double_tap` | `- double_tap: "文本"` | 双击元素 |
| `input_text` | `- input_text: "内容"` | 输入文本 |
| `clear_text` | `- clear_text` | 清除文本 |
| `swipe` | `- swipe: "up"` | 滑动 |
| `scroll` | - | 滚动到元素 |
| `assert_visible` | `- assert_visible: "文本"` | 断言可见 |
| `assert_not_visible` | `- assert_not_visible: "文本"` | 断言不可见 |
| `assert_text` | - | 断言文本内容 |
| `assert_ai` | `- assert_ai: "描述"` | AI 视觉断言 |
| `wait_visible` | `- wait_visible: "文本"` | 等待出现 |
| `wait_gone` | `- wait_gone: "文本"` | 等待消失 |
| `wait_seconds` | `- wait_seconds: 2` | 固定等待 |
| `back` | `- back` | 返回 |
| `home` | `- home` | 回主屏 |
| `press_key` | `- press_key: "enter"` | 按键 |
| `screenshot` | `- screenshot: "name"` | 截图 |
| `set_orientation` | `- set_orientation: "landscape"` | 屏幕方向 |
| `if` | - | 条件执行 |
| `repeat` | - | 循环 |
| `run_flow` | `- run_flow: "file.yaml"` | 子流程 |
| `set_variable` | - | 设置变量 |

---

## 附录 B: 与 Maestro 的差异

| 特性 | Maestro | 本设计 |
|------|---------|--------|
| 命令命名 | camelCase | snake_case |
| 简单命令 | `- launchApp` | `- launch_app` |
| 选择器 | `text:`, `id:` | `text:`, `id:` (相同) |
| 关系选择器 | `below:`, `above:` | `below:`, `above:`, `near:` |
| AI 断言 | `assertWithAI:` | `assert_ai:` |
| 流程控制 | `repeat:`, `runFlow:` | `repeat:`, `run_flow:`, `if:` |
| 变量语法 | `${var}` | `${var}` (相同) |
| Schema 约束 | 无官方 Schema | 完整 JSON Schema |

---

*文档版本: 1.0*
*最后更新: 2024-01*
