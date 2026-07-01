# 小红书合规检测工具 🚨

> AI 驱动的违禁词检测 + 合规改写，让你的小红书内容永不踩雷！

[![Stars](https://img.shields.io/github/stars/sleeppig0314-collab/xhs-compliance-prompt?style=flat)](https://github.com/sleeppig0314-collab/xhs-compliance-prompt)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## ✨ 功能特点

- 🔍 **违禁词检测** — 支持广告法禁词、平台专属禁词、行业特殊规则
- ✍️ **智能改写** — 在保留"人味"的同时合规表达
- 📊 **风险评级** — 高/中/低三档风险提示
- 🆓 **免费使用** — 基于 AI Prompt，无需付费

---

## 🚀 快速开始

### 方法 1：直接使用

1. 打开 [PROMPT.md](PROMPT.md)
2. 复制 Prompt 内容
3. 粘贴到 ChatGPT / Claude / Kimi 等 AI 对话框
4. 输入你的文案，获取检测结果

### 方法 2：命令行工具

```bash
# 克隆项目
git clone https://github.com/sleeppig0314-collab/xhs-compliance-prompt.git
cd xhs-compliance-prompt

# 运行检测
python xhs_checker.py "这是最棒的产品，100%有效！"
```

**输出示例：**
```
🔍 检测结果 (发现 2 个风险词)
==================================================
  🚨 高风险: 最, 100%

📝 改写建议：
  这是很棒的产品，超过9成有效！
```

### 方法 3：JSON 模式（适合脚本 / CI/CD）

```bash
python xhs_checker.py --json "这是最棒的产品，100%有效！"
```

**JSON 输出示例：**
```json
{
  "text": "这是最棒的产品，100%有效！",
  "total": 2,
  "high_risk": ["最", "100%"],
  "medium_risk": [],
  "low_risk": [],
  "rewritten": "这是很棒的产品，超过9成有效！",
  "pass": false
}
```

### 方法 4：批量检测

```bash
python xhs_checker.py --batch file.txt   # 从文件读取
python xhs_checker.py --batch            # 从 stdin 读取（输入 'done' 结束）
```

---

## 📁 项目结构

```
xhs-compliance-prompt/
├── PROMPT.md          # AI 检测 + 改写 Prompt（直接用）
├── WORDLIB.md         # 违禁词库（含行业分类）
├── XHS_POST.md        # 小红书发布模板
├── xhs_checker.py     # Python CLI 工具
├── CONTRIBUTING.md    # 贡献指南
└── README.md          # 本文件
```

---

## 🎯 适用场景

| 行业 | 痛点 | 解决方案 |
|------|------|----------|
| 电商 | "最便宜"等绝对化词汇 | 自动改写为合规表达 |
| 教育 | "保证提分"等承诺性词汇 | 改写为"有助于提升" |
| 美妆 | "根治"等医疗性词汇 | 改写为"改善"等安全词汇 |
| 理财 | "稳赚"等投资承诺 | 改写为"收益可观"等中性表达 |

---

## 💰 如何盈利（开发者参考）

如果你想基于此项目做商业化：

1. **网页工具** — 做成在线工具，免费用户每天 5 次，付费 $5/月 无限
2. **API 服务** — 封装成 API，按调用次数收费
3. **Chrome 插件** — 浏览器插件，一键检测
4. **定制词库** — 为企业客户提供行业专属词库服务

---

## 🤝 贡献

欢迎提交 Issue 和 PR！

- 添加新的违禁词 → 修改 `WORDLIB.md`
- 改进检测效果 → 优化 `PROMPT.md`
- 贡献代码 → 提交 PR

详见 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📜 免责声明

本工具仅供参考，实际运营请以小红书官方规则为准。

---

**如果对你有帮助，请点个 ⭐ 支持一下！**
