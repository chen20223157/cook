#!/bin/bash

echo "==================================="
echo "  AI 菜谱清道夫 启动脚本"
echo "==================================="
echo ""

# 检查 .env 文件是否存在
if [ ! -f .env ]; then
    echo "[错误] 未找到 .env 文件！"
    echo ""
    echo "请创建 .env 文件并添加你的 OpenAI API Key："
    echo "OPENAI_API_KEY=your-api-key-here"
    echo ""
    echo "详细步骤请查看 setup_guide.md"
    exit 1
fi

# 检查是否安装了依赖
python3 -c "import streamlit" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "[提示] 检测到依赖未安装，正在安装..."
    echo ""
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "[错误] 依赖安装失败！"
        exit 1
    fi
    echo ""
    echo "[成功] 依赖安装完成！"
    echo ""
fi

echo "[启动] 正在启动应用..."
echo ""
echo "浏览器会自动打开，如果没有，请手动访问："
echo "http://localhost:8501"
echo ""
echo "按 Ctrl+C 停止应用"
echo ""

streamlit run app.py
