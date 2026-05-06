我发现我们之前转化case 不是很精确，我们需要有更精确的转换case的方法。

在转化case 之前，我觉得我们应该学习 Gherkin 语法：

资料在这里： https://cucumber.io/docs/gherkin/reference

feature 文件和 steps的文件的映射关系在这里： https://cucumber.io/docs/gherkin/step-organization

在这些case 中，我们使用的python 的BDD 实现方式： https://github.com/behave/behave

另外，需要注意 BDD 的HOOK 内容：
- 例如： 这个文件https://github.com/edge-microsoft/FSQ_AI_Testcases_Android/blob/main/features/environment.py 中的before_all, after_all, before_scenario 和 after_scenario 这些Hook 操作都需被转化。