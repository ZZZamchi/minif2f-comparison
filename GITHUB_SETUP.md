# GitHub 上传指南

## 准备工作

项目已经初始化了 Git 仓库，所有文件已添加到暂存区。

## 上传到 GitHub 的步骤

### 1. 在 GitHub 上创建新仓库

1. 登录 GitHub
2. 点击右上角的 "+" 号，选择 "New repository"
3. 填写仓库信息：
   - Repository name: `minif2f-comparison` (或您喜欢的名称)
   - Description: "Detailed comparison analysis of miniF2F v1 vs v2 datasets"
   - 选择 Public 或 Private
   - **不要**初始化 README、.gitignore 或 license（我们已经有了）
4. 点击 "Create repository"

### 2. 连接本地仓库到 GitHub

在项目目录下运行以下命令（替换 YOUR_USERNAME 和 REPO_NAME）：

```bash
# 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# 或者使用 SSH
git remote add origin git@github.com:YOUR_USERNAME/REPO_NAME.git
```

### 3. 提交并推送

```bash
# 提交所有更改
git commit -m "Initial commit: miniF2F v1 vs v2 comparison analysis"

# 推送到 GitHub
git branch -M main
git push -u origin main
```

## 文件说明

### 已包含的文件

- `README.md` - 项目说明文档
- `LICENSE` - Apache-2.0 许可证
- `.gitignore` - Git 忽略文件配置
- `CONTRIBUTING.md` - 贡献指南
- `datasets/` - v2 数据集文件
- `assets/` - 资源文件（图片）
- `minif2f_v1/` - v1 数据集
- `compare_datasets.py` - 比较脚本
- `generate_detailed_report.py` - 报告生成脚本
- `download_tonic_minif2f.py` - 下载脚本
- `miniF2F_comparison_report.docx` - Word 格式报告
- `Google_Docs_完整对比_纯文本.txt` - Google 文档格式对比

### 注意事项

1. **大文件**: 数据集 JSON 文件可能较大，如果超过 100MB，考虑使用 Git LFS
2. **敏感信息**: 确保没有包含任何敏感信息
3. **许可证**: 已包含 Apache-2.0 许可证

## 使用 Git LFS（如果需要）

如果数据集文件很大，可以使用 Git LFS：

```bash
# 安装 Git LFS
git lfs install

# 跟踪大文件
git lfs track "*.json"
git lfs track "*.jsonl"

# 添加 .gitattributes
git add .gitattributes
git commit -m "Add Git LFS tracking for large files"
```

## 后续更新

```bash
# 添加更改
git add .

# 提交
git commit -m "描述您的更改"

# 推送
git push
```
