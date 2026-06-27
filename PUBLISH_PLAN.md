# pptx-lint 项目发布与推广计划

## 背景

`pptx-lint` 是一个用于检测 python-pptx 生成 PPT 质量问题的开源工具。已成功上架 GitHub（https://github.com/LeppardWang/pptx-lint），包含17个文件、920行代码，具备完整的 CLI、单元测试和 CI 配置。

**核心功能：**
- 超框检测（overflow）
- 重叠检测（overlap）
- 假表格检测（fake_table）
- 小字体检测（font_size）
- 空白页检测（empty_slide）

---

## Task 1：发布到 PyPI（pip install）

### 1.1 注册 PyPI 账号并获取 API Token
- 访问 https://pypi.org/account/register/ 注册账号
- 登录后进入 Account Settings → API tokens
- 点击 "Add API token"，选择 Scope: Entire account (all projects)
- 复制生成的 token（格式类似 `pypi-AgEi...`）

### 1.2 安装构建工具
```bash
pip install build twine
```

### 1.3 构建包
```bash
cd "c:\Users\Administrator\Documents\短暂同步\pptx-lint"
python -m build
```
这会生成：
- `dist/pptx_lint-0.1.0-py3-none-any.whl`
- `dist/pptx_lint-0.1.0.tar.gz`

### 1.4 上传到 PyPI
```bash
twine upload dist/*
```
会提示输入用户名和密码：
- Username: `__token__`
- Password: 粘贴刚才复制的 API token

### 1.5 验证安装
```bash
pip install pptx-lint
pptx-lint --version
```

---

## Task 2：添加 Badge 和文档增强

### 2.1 更新 README.md
在 README 顶部添加以下 badges（替换占位符）：

```markdown
[![PyPI](https://img.shields.io/pypi/v/pptx-lint)](https://pypi.org/project/pptx-lint/)
[![Python](https://img.shields.io/pypi/pyversions/pptx-lint)](https://pypi.org/project/pptx-lint/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/LeppardWang/pptx-lint/actions/workflows/test.yml/badge.svg)](https://github.com/LeppardWang/pptx-lint/actions/workflows/test.yml)
[![Downloads](https://pepy.tech/badge/pptx-lint)](https://pepy.tech/project/pptx-lint)
```

### 2.2 添加 Usage Examples 章节
在 README 中增加：
- 更多使用示例（JSON/HTML 输出）
- 常见错误案例截图
- 与其他工具对比表

### 2.3 添加 CHANGELOG.md
记录版本历史：
```markdown
# Changelog

## [0.1.0] - 2026-06-27
### Added
- Initial release with overflow, overlap, fake table, font size, and empty slide detection
- CLI tool with colored terminal output
- pytest test suite
- GitHub Actions CI for Python 3.9-3.13
```

---

## Task 3：社区推广

### 3.1 python-pptx 官方渠道
- **GitHub Discussions**: 在 https://github.com/scanny/python-pptx/discussions 发帖介绍
- **GitHub Issues**: 如果有相关 issue，可以评论推荐此工具

### 3.2 Reddit
- **r/Python**: 发帖标题 "I built a linter for python-pptx presentations — detects overflow, overlap, and fake tables"
- **r/datascience**: 如果涉及数据报告场景
- **r/powerpoint**: 针对 PPT 用户群体

### 3.3 Hacker News
- 提交到 Show HN: https://news.ycombinator.com/showhn.html
- 标题: "Show HN: pptx-lint – Lint your python-pptx presentations for quality issues"

### 3.4 Twitter/X
- 发推带标签: `#python #powerpoint #opensource #pptx`
- @scanny (python-pptx 作者) 可能会转发

### 3.5 LinkedIn
- 发布专业文章介绍工具的技术细节和应用场景

---

## Task 4：功能增强（v0.2.0）

### 4.1 JSON/HTML 报告输出
新增 `--format json` 和 `--format html` 参数：
```bash
pptx-lint presentation.pptx --format json > report.json
pptx-lint presentation.pptx --format html > report.html
```

### 4.2 自动修复功能（--fix）
部分规则支持自动修复：
```bash
pptx-lint presentation.pptx --fix  # 自动调整坐标避免重叠
```

### 4.3 更多检测规则
- **配色检查**：对比度不足警告
- **对齐检查**：文本/形状未对齐
- **图片分辨率**：低 DPI 图片警告
- **动画检查**：过多动画元素

### 4.4 配置文件支持
允许用户自定义规则阈值（`.pptxlint.yml`）：
```yaml
rules:
  overflow:
    tolerance: 0.05  # inches
  overlap:
    threshold: 0.5   # 50%
  font_size:
    min: 8           # points
```

---

## Task 5：长期维护

### 5.1 响应 Issue 和 PR
- 设置 GitHub Issue 模板
- 定期查看并回复社区反馈

### 5.2 持续集成优化
- 添加测试覆盖率 badge（codecov.io）
- 集成 pre-commit hooks

### 5.3 文档完善
- 添加 Sphinx 文档站点
- 录制演示视频

---

## 执行顺序

1. **立即执行**：Task 1（PyPI 发布）+ Task 2（Badge 更新）
2. **本周内**：Task 3（社区推广）
3. **下个月**：Task 4（功能增强 v0.2.0）
4. **持续**：Task 5（长期维护）

---

## 成功指标

- ✅ PyPI 下载量 > 100/月
- ✅ GitHub Stars > 100
- ✅ 收到至少 1 个外部 PR
- ✅ 被 python-pptx 官方文档引用

---

## 关键文件

- `README.md` - 添加 badges 和文档
- `CHANGELOG.md` - 新建版本历史
- `src/pptx_lint/reporters/json.py` - 新建 JSON 输出器
- `src/pptx_lint/reporters/html.py` - 新建 HTML 输出器
- `.pptxlint.yml.example` - 配置文件示例
- `setup.cfg` / `pyproject.toml` - 可能需要调整元数据
