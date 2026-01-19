# 🚀 快速设置指南

## 第一步：创建 .env 文件

在项目根目录创建一个名为 `.env` 的文件，内容如下：

```env
OPENAI_API_KEY=sk-your-actual-api-key-here
```

**重要提示：**
- 将 `sk-your-actual-api-key-here` 替换为你的真实 API Key
- 不要将 `.env` 文件提交到 Git（已在 .gitignore 中排除）

## 第二步：安装依赖

打开终端或命令提示符，在项目目录下运行：

```bash
pip install -r requirements.txt
```

## 第三步：运行应用

```bash
streamlit run app.py
```

应用会自动在浏览器中打开！

## 获取 OpenAI API Key

1. 访问：https://platform.openai.com/api-keys
2. 登录或注册 OpenAI 账号
3. 点击 "Create new secret key"
4. 复制生成的 API Key（格式：sk-...）
5. 粘贴到 `.env` 文件中

## Windows 用户

如果使用 PowerShell，可以运行：

```powershell
# 创建虚拟环境（推荐）
python -m venv venv
.\venv\Scripts\Activate.ps1

# 安装依赖
pip install -r requirements.txt

# 运行应用
streamlit run app.py
```

## macOS/Linux 用户

```bash
# 创建虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 运行应用
streamlit run app.py
```

## 测试建议

第一次使用时，建议用以下方式测试：

1. **准备测试照片**：
   - 拍摄 3-5 种常见食材的照片
   - 确保照片清晰，光线充足
   - 建议食材：番茄、鸡蛋、青菜、豆腐、肉类等

2. **设置偏好**：
   - 先不设置任何避雷选项
   - 使用默认厨具配置
   - 生成第一个菜谱

3. **体验避雷功能**：
   - 选择一些避雷选项（如"不吃香菜"）
   - 重新生成菜谱，观察差异
   - 调整厨具配置，看菜谱的变化

## 故障排除

### 问题 1：找不到 streamlit 命令

**解决方案**：
```bash
python -m streamlit run app.py
```

### 问题 2：API Key 错误

**检查**：
- `.env` 文件是否在正确位置（项目根目录）
- API Key 格式是否正确（以 sk- 开头）
- 是否有额外的空格或引号

### 问题 3：依赖安装失败

**解决方案**：
```bash
# 升级 pip
python -m pip install --upgrade pip

# 使用国内镜像（如果在中国）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 开始使用吧！🎉

设置完成后，打开浏览器访问 http://localhost:8501，开始你的 AI 菜谱之旅！
