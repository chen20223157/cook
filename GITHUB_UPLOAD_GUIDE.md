# 🚀 GitHub 上传指南

## 已完成的步骤 ✅

- [x] 初始化 Git 仓库
- [x] 添加 .gitignore（保护你的 API Key）
- [x] 创建首次提交

## 接下来的步骤

### 1️⃣ 在 GitHub 上创建新仓库

访问：https://github.com/new

填写信息：
- **Repository name**: `ai-recipe-cleaner`
- **Description**: `AI 菜谱清道夫 - 基于 GPT-4o Vision 的智能食材识别和菜谱生成系统`
- **Public** 或 **Private**（根据需要选择）
- ⚠️ **不要勾选** "Add a README file"
- ⚠️ **不要勾选** "Add .gitignore"

### 2️⃣ 连接远程仓库并推送

在终端中运行以下命令（替换成你的 GitHub 用户名）：

```bash
# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/ai-recipe-cleaner.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 3️⃣ 验证上传

访问你的 GitHub 仓库页面，应该能看到所有文件已上传成功！

## 📁 已上传的文件

- ✅ app.py - 主应用程序
- ✅ requirements.txt - 依赖包列表
- ✅ README.md - 项目说明文档
- ✅ setup_guide.md - 快速设置指南
- ✅ run.bat - Windows 启动脚本
- ✅ run.sh - Linux/macOS 启动脚本
- ✅ .gitignore - Git 忽略文件
- ✅ ENV_SETUP.txt - 环境变量说明

## 🔒 安全提示

你的 API Key 已被保护：
- ❌ `.env` 文件**不会**被上传（已在 .gitignore 中）
- ❌ `openai.env` 文件**不会**被上传（已在 .gitignore 中）
- ✅ 只上传了代码和文档

## 后续更新代码

当你修改代码后，使用以下命令更新 GitHub：

```bash
# 添加修改的文件
git add .

# 创建提交
git commit -m "描述你的修改"

# 推送到 GitHub
git push
```

## 常见问题

### Q: 如果提示需要登录？
**A**: 使用 GitHub Personal Access Token：
1. 访问：https://github.com/settings/tokens
2. 创建新 token（classic）
3. 勾选 `repo` 权限
4. 复制 token
5. 推送时用 token 作为密码

### Q: 如何克隆到其他电脑？
**A**: 
```bash
git clone https://github.com/YOUR_USERNAME/ai-recipe-cleaner.git
cd ai-recipe-cleaner
pip install -r requirements.txt
# 创建 .env 文件并添加 API Key
streamlit run app.py
```

---

**祝你开源愉快！** 🎉
