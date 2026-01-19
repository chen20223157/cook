# 🥘 AI 菜谱清道夫

> 拍一张冰箱照片，AI 大厨为你的剩余食材创造美味菜谱！

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ 核心功能

- 📷 **智能识别食材**：使用 GPT-4o Vision 精准识别照片中的食材
- 👨‍🍳 **AI 生成菜谱**：根据现有食材自动生成 3 个实用菜谱
- 🚫 **智能避雷**：支持设置不喜欢的食材和厨具限制
- 🎯 **多样化菜谱**：家常菜、快手菜、创意菜，满足不同需求
- 💡 **贴心建议**：每个菜谱都附带详细步骤和烹饪小贴士
- 💾 **一键保存**：支持下载菜谱文本，随时查看

## 🎬 快速开始

### 1. 环境准备

确保你已安装 Python 3.8 或更高版本：

```bash
python --version
```

### 2. 克隆项目

```bash
git clone <your-repo-url>
cd vegetable
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置 API Key

在项目根目录创建 `.env` 文件，添加你的 OpenAI API Key：

```env
OPENAI_API_KEY=your-api-key-here
```

**获取 API Key：**
1. 访问 [OpenAI Platform](https://platform.openai.com/api-keys)
2. 登录或注册账号
3. 创建新的 API Key
4. 复制并粘贴到 `.env` 文件中

### 5. 运行应用

```bash
streamlit run app.py
```

应用会自动在浏览器中打开（默认地址：http://localhost:8501）

## 📖 使用指南

### 第一步：上传食材照片

1. 点击"选择一张冰箱食材照片"按钮
2. 从电脑中选择一张食材照片
3. 确保照片光线充足，食材清晰可见

**拍摄技巧：**
- 📸 使用自然光或充足的照明
- 🎯 将食材平铺展开，避免重叠
- 📏 保持适当距离，确保所有食材都在镜头内
- 🔍 照片清晰度越高，识别越准确

### 第二步：设置偏好（可选）

在左侧边栏中设置：

#### 🚫 食材避雷
- 不吃香菜
- 不吃辣
- 不吃海鲜
- 不吃猪肉/牛肉
- 不用酒
- 自定义其他避雷食材

#### 🔧 可用厨具
- 炉灶、炒锅（默认）
- 烤箱
- 微波炉
- 空气炸锅
- 高压锅
- 蒸锅

#### 🥗 饮食偏好
- 低脂
- 低糖
- 高蛋白
- 素食
- 儿童友好
- 老人友好

### 第三步：生成菜谱

1. 点击"🎯 立即生成菜谱"按钮
2. AI 会在 30 秒内完成分析
3. 查看识别到的食材和 3 个定制菜谱

### 第四步：保存菜谱

点击"📥 下载菜谱"按钮，将菜谱保存为文本文件，方便后续查看。

## 🎯 功能亮点

### 1. 多模态 AI 技术

使用 OpenAI GPT-4o Vision 模型，结合图像识别和自然语言处理：
- 高精度食材识别
- 智能理解食材组合
- 创造性菜谱生成

### 2. Prompt Engineering

精心设计的提示词工程，确保：
- 菜谱实用性强
- 步骤简单易懂
- 烹饪时间合理（≤30分钟）
- 考虑用户限制条件

### 3. 美观的用户界面

- 🎨 现代化渐变色设计
- 📱 响应式布局，支持各种屏幕尺寸
- 💫 流畅的交互体验
- 🎯 清晰的信息层级

### 4. 智能避雷系统

- 自动过滤不喜欢的食材
- 根据可用厨具调整烹饪方法
- 尊重饮食偏好和限制

## 📦 项目结构

```
vegetable/
│
├── app.py              # Streamlit 主应用
├── requirements.txt    # Python 依赖包
├── .gitignore         # Git 忽略文件
├── README.md          # 项目说明文档
└── .env               # 环境变量配置（需自行创建）
```

## 🔧 技术栈

- **前端框架**：Streamlit 1.31.0
- **AI 模型**：OpenAI GPT-4o Vision
- **图像处理**：Pillow 10.2.0
- **环境管理**：python-dotenv 1.0.0
- **编程语言**：Python 3.8+

## 💡 Prompt Engineering 技巧

本项目的核心是精心设计的 Prompt，关键要点：

1. **清晰的角色定位**："你是一位专业的中餐厨师和营养师"
2. **结构化输出**：使用 JSON 格式确保结果可解析
3. **约束条件**：明确烹饪时间、难度、可用食材等限制
4. **上下文信息**：包含用户的避雷选项和厨具信息
5. **多样性要求**：要求生成不同风格的菜谱

## 🚀 进阶功能（待开发）

- [ ] 支持多张照片上传
- [ ] 菜谱评分和收藏功能
- [ ] 营养成分分析
- [ ] 购物清单生成
- [ ] 视频教程链接
- [ ] 用户历史记录
- [ ] 社区分享功能
- [ ] 支持更多语言

## ⚠️ 注意事项

1. **API 费用**：GPT-4o Vision 是付费 API，请注意使用量
2. **网络连接**：需要稳定的网络连接才能访问 OpenAI API
3. **图片质量**：照片质量直接影响识别准确度
4. **隐私保护**：上传的图片会发送到 OpenAI 服务器进行处理

## 🐛 常见问题

### Q1: API Key 无效？
**A:** 请检查：
- API Key 是否正确复制到 `.env` 文件
- API Key 是否有效（未过期或被撤销）
- OpenAI 账户是否有足够余额

### Q2: 识别不准确？
**A:** 建议：
- 提高照片清晰度
- 确保光线充足
- 食材不要重叠
- 尽量使用白色或浅色背景

### Q3: 生成菜谱太慢？
**A:** 可能原因：
- 网络连接不稳定
- OpenAI API 响应较慢（高峰期）
- 照片文件过大（建议 < 5MB）

### Q4: 无法运行 Streamlit？
**A:** 解决方案：
```bash
# 升级 pip
python -m pip install --upgrade pip

# 重新安装依赖
pip install -r requirements.txt --force-reinstall
```

## 📝 更新日志

### v1.0.0 (2026-01-14)
- ✨ 初始版本发布
- 📷 支持图片上传和食材识别
- 🍳 AI 生成 3 个定制菜谱
- 🚫 智能避雷功能
- 💾 菜谱下载功能

## 👨‍💻 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 开源协议

本项目采用 MIT 协议开源，详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- [OpenAI](https://openai.com/) - 提供强大的 GPT-4o Vision API
- [Streamlit](https://streamlit.io/) - 提供优秀的 Web 框架
- 所有贡献者和使用者

## 📧 联系方式

如有问题或建议，欢迎通过以下方式联系：

- 提交 Issue
- 发送邮件
- 加入讨论组

---

**Made with ❤️ by AI Enthusiasts**

*让 AI 帮助你减少食物浪费，创造美味生活！*
