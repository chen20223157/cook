import streamlit as st
import os
from openai import OpenAI
import base64
from io import BytesIO
from PIL import Image
import json
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 页面配置
st.set_page_config(
    page_title="AI 菜谱清道夫 🥘",
    page_icon="🥘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义 CSS 样式
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #FF6B6B;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .recipe-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
    .recipe-title {
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .ingredient-box {
        background: rgba(255,255,255,0.2);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #FF6B6B 0%, #FFE66D 100%);
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 0.75rem;
        border-radius: 10px;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# 初始化 OpenAI 客户端
@st.cache_resource
def init_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("⚠️ 请设置 OPENAI_API_KEY 环境变量！")
        st.stop()
    return OpenAI(api_key=api_key)

# 将图片转换为 base64
def encode_image(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

# 识别食材并生成菜谱
def generate_recipes(image, restrictions, kitchen_equipment, dietary_preferences):
    client = init_openai_client()
    
    # 构建避雷选项文本
    restriction_text = ""
    if restrictions:
        restriction_text = f"\n⚠️ 避雷要求：{', '.join(restrictions)}"
    
    equipment_text = ""
    if kitchen_equipment:
        equipment_text = f"\n🔧 可用厨具：{', '.join(kitchen_equipment)}"
    else:
        equipment_text = "\n🔧 可用厨具：基本厨具（刀、锅、炉灶）"
    
    dietary_text = ""
    if dietary_preferences:
        dietary_text = f"\n🥗 饮食偏好：{', '.join(dietary_preferences)}"
    
    # 精心设计的 Prompt
    prompt = f"""你是一位专业的中餐厨师和营养师。请仔细观察这张照片中的食材，然后为用户生成 3 个实用的菜谱。

📋 任务要求：
1. 识别照片中所有可见的食材
2. 基于这些食材，创造 3 个不同风格的菜谱（家常菜、快手菜、创意菜各一个）
3. 每个菜谱都必须：
   - 主要使用照片中的食材
   - 可以添加常见的调味料（盐、油、酱油等）
   - 步骤简单清晰，适合家庭烹饪
   - 烹饪时间在 30 分钟以内

{restriction_text}
{equipment_text}
{dietary_text}

🎯 输出格式（严格按照此 JSON 格式）：
{{
    "identified_ingredients": ["食材1", "食材2", "食材3"],
    "recipes": [
        {{
            "name": "菜品名称",
            "style": "家常菜/快手菜/创意菜",
            "difficulty": "简单/中等/困难",
            "time": "X分钟",
            "servings": "X人份",
            "main_ingredients": ["主要食材1", "主要食材2"],
            "additional_ingredients": ["额外需要的调味料或配料"],
            "steps": [
                "步骤1：详细描述",
                "步骤2：详细描述",
                "步骤3：详细描述"
            ],
            "tips": "烹饪小贴士"
        }}
    ]
}}

请确保菜谱实用、美味、容易操作！"""

    # 将图片转为 base64
    base64_image = encode_image(image)
    
    try:
        with st.spinner('🤖 AI 大厨正在识别食材并创作菜谱...'):
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{base64_image}",
                                    "detail": "high"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=2000,
                temperature=0.8
            )
        
        # 解析返回的 JSON
        result_text = response.choices[0].message.content
        # 提取 JSON（如果包含在 markdown 代码块中）
        if "```json" in result_text:
            result_text = result_text.split("```json")[1].split("```")[0].strip()
        elif "```" in result_text:
            result_text = result_text.split("```")[1].split("```")[0].strip()
        
        result = json.loads(result_text)
        return result
    
    except Exception as e:
        st.error(f"❌ 生成菜谱时出错：{str(e)}")
        return None

# 显示菜谱卡片
def display_recipe(recipe, index):
    colors = [
        "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
        "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)"
    ]
    
    st.markdown(f"""
    <div style='background: {colors[index]}; padding: 2rem; border-radius: 15px; color: white; margin: 1rem 0;'>
        <div style='font-size: 1.8rem; font-weight: bold; margin-bottom: 0.5rem;'>
            {recipe['name']} 
        </div>
        <div style='font-size: 1rem; opacity: 0.9; margin-bottom: 1rem;'>
            🏷️ {recipe['style']} | ⏱️ {recipe['time']} | 👥 {recipe['servings']} | 📊 {recipe['difficulty']}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🥘 主要食材")
        for ingredient in recipe['main_ingredients']:
            st.markdown(f"• {ingredient}")
        
        if recipe['additional_ingredients']:
            st.markdown("### 🧂 额外需要")
            for ingredient in recipe['additional_ingredients']:
                st.markdown(f"• {ingredient}")
    
    with col2:
        st.markdown("### 👨‍🍳 烹饪步骤")
        for i, step in enumerate(recipe['steps'], 1):
            st.markdown(f"**{i}.** {step}")
    
    if recipe.get('tips'):
        st.info(f"💡 **小贴士**：{recipe['tips']}")
    
    st.markdown("---")

# 主界面
def main():
    # 标题
    st.markdown('<div class="main-header">🥘 AI 菜谱清道夫</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">拍张照片，AI 大厨为你的剩余食材创造美味菜谱！</div>', unsafe_allow_html=True)
    
    # 侧边栏 - 避雷选项
    with st.sidebar:
        st.header("⚙️ 偏好设置")
        
        st.subheader("🚫 食材避雷")
        col1, col2 = st.columns(2)
        with col1:
            avoid_cilantro = st.checkbox("不吃香菜")
            avoid_spicy = st.checkbox("不吃辣")
            avoid_seafood = st.checkbox("不吃海鲜")
        with col2:
            avoid_pork = st.checkbox("不吃猪肉")
            avoid_beef = st.checkbox("不吃牛肉")
            avoid_alcohol = st.checkbox("不用酒")
        
        custom_avoid = st.text_input("其他避雷食材（用逗号分隔）", placeholder="例如：葱、姜、蒜")
        
        # 构建避雷列表
        restrictions = []
        if avoid_cilantro:
            restrictions.append("不使用香菜")
        if avoid_spicy:
            restrictions.append("不加辣椒")
        if avoid_seafood:
            restrictions.append("不使用海鲜")
        if avoid_pork:
            restrictions.append("不使用猪肉")
        if avoid_beef:
            restrictions.append("不使用牛肉")
        if avoid_alcohol:
            restrictions.append("不使用料酒或白酒")
        if custom_avoid:
            restrictions.extend([f"不使用{item.strip()}" for item in custom_avoid.split(",")])
        
        st.subheader("🔧 可用厨具")
        has_oven = st.checkbox("有烤箱", value=False)
        has_microwave = st.checkbox("有微波炉", value=True)
        has_air_fryer = st.checkbox("有空气炸锅", value=False)
        has_pressure_cooker = st.checkbox("有高压锅", value=False)
        has_steamer = st.checkbox("有蒸锅", value=True)
        
        kitchen_equipment = ["炉灶", "炒锅", "刀具"]
        if has_oven:
            kitchen_equipment.append("烤箱")
        if has_microwave:
            kitchen_equipment.append("微波炉")
        if has_air_fryer:
            kitchen_equipment.append("空气炸锅")
        if has_pressure_cooker:
            kitchen_equipment.append("高压锅")
        if has_steamer:
            kitchen_equipment.append("蒸锅")
        
        st.subheader("🥗 饮食偏好")
        diet_type = st.multiselect(
            "选择饮食类型",
            ["低脂", "低糖", "高蛋白", "素食", "儿童友好", "老人友好"]
        )
        
        dietary_preferences = diet_type
    
    # 主要内容区
    st.markdown("### 📸 上传食材照片")
    st.info("💡 提示：拍摄时请确保光线充足，食材清晰可见，效果更好哦！")
    
    uploaded_file = st.file_uploader(
        "选择一张冰箱食材照片",
        type=["jpg", "jpeg", "png"],
        help="支持 JPG、JPEG、PNG 格式"
    )
    
    if uploaded_file is not None:
        # 显示上传的图片
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            image = Image.open(uploaded_file)
            st.image(image, caption="📷 你的食材照片", use_column_width=True)
        
        # 生成菜谱按钮
        if st.button("🎯 立即生成菜谱", type="primary"):
            result = generate_recipes(image, restrictions, kitchen_equipment, dietary_preferences)
            
            if result:
                # 显示识别的食材
                st.markdown("## 🔍 识别到的食材")
                ingredients_text = " • ".join(result['identified_ingredients'])
                st.success(f"**{ingredients_text}**")
                
                st.markdown("---")
                
                # 显示菜谱
                st.markdown("## 👨‍🍳 为你定制的 3 道菜谱")
                
                for i, recipe in enumerate(result['recipes']):
                    display_recipe(recipe, i)
                
                # 下载菜谱
                st.markdown("### 💾 保存菜谱")
                recipe_text = f"""AI 菜谱清道夫 - 生成的菜谱
{'='*50}

识别到的食材：
{', '.join(result['identified_ingredients'])}

{'='*50}

"""
                for i, recipe in enumerate(result['recipes'], 1):
                    recipe_text += f"""
【菜谱 {i}】{recipe['name']}
风格：{recipe['style']} | 难度：{recipe['difficulty']} | 时间：{recipe['time']} | 份量：{recipe['servings']}

主要食材：
{chr(10).join(['• ' + ing for ing in recipe['main_ingredients']])}

额外需要：
{chr(10).join(['• ' + ing for ing in recipe['additional_ingredients']])}

烹饪步骤：
{chr(10).join([f'{j}. {step}' for j, step in enumerate(recipe['steps'], 1)])}

小贴士：{recipe['tips']}

{'='*50}
"""
                
                st.download_button(
                    label="📥 下载菜谱（文本格式）",
                    data=recipe_text,
                    file_name="ai_recipes.txt",
                    mime="text/plain"
                )
    else:
        # 示例说明
        st.markdown("### 📝 使用说明")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **第一步：上传照片**
            
            📷 拍一张冰箱里剩余食材的照片
            
            💡 确保食材清晰可见
            """)
        
        with col2:
            st.markdown("""
            **第二步：设置偏好**
            
            ⚙️ 在左侧设置避雷选项
            
            🔧 选择可用的厨具
            """)
        
        with col3:
            st.markdown("""
            **第三步：获取菜谱**
            
            🎯 点击生成按钮
            
            👨‍🍳 获得 3 个专属菜谱
            """)
        
        st.markdown("---")
        
        # 功能亮点
        st.markdown("### ✨ 功能亮点")
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("🤖 **AI 视觉识别**\n\n使用 GPT-4o Vision 精准识别食材")
            st.info("⏱️ **快速生成**\n\n30 秒内生成 3 个实用菜谱")
        
        with col2:
            st.warning("🚫 **智能避雷**\n\n自动排除不喜欢的食材和厨具")
            st.success("💡 **贴心建议**\n\n每个菜谱都附带烹饪小贴士")

if __name__ == "__main__":
    main()
