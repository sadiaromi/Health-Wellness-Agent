import re
from dotenv import load_dotenv
import streamlit as st
import asyncio
from agent_config import create_health_wellness_agent
from context import UserSessionContext
from fpdf import FPDF

# ----------------- Load environment and set config -----------------
load_dotenv()
st.set_page_config(page_title="Health & Wellness Assistant", page_icon="💪", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: #000000;'>🧠 Health & Wellness Planner Agent</h1>",
    unsafe_allow_html=True,
)

# ----------------- Emoji Remover (for PDF only) -----------------
def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F3AF"     # 🎯
        "\U0001F4AA"     # 💪
        "\U0001FA7A"     # 🩺
        "\U0001F468"     # 👨
        "\U0001F469"     # 👩
        "\U00002695"     # ⚕
        "\U0001F957"     # 🥗
        "\U0001F37D"     # 🍽
        "\U0001F3CB"     # 🏋
        "\U00002642"     # ♂
        "\U00002640"     # ♀
        "\U0001F4C5"     # 📅
        "\U000023F0"     # ⏰
        "\U0001F4CA"     # 📊
        "\U0001F31F"     # 🌟
        "\U0001F6D1"     # 🛑
        "\U0001F3E5"     # 🏥
        "\U0001F91D"     # 🤝
        "\U0001F9E0"     # 🧠
        "\U0001F504"     # 🔄
        "\U00002705"     # ✅
        "\U0001F4DD"     # 📝
        "\U0001F4C4"     # 📄
        "\U0001F4E5"     # 📥
        "\U0001F60A"     # 😊
        "\u200d"         # Zero width joiner
        "\ufe0f"         # Variation selector
        "]+",
        flags=re.UNICODE
    )

    # Remove composite emojis manually
    composites = [
        "\U0001F468\u200d\u2695\ufe0f",  # 👨‍⚕️
        "\U0001F469\u200d\u2695\ufe0f",  # 👩‍⚕️
        "\U0001F3CB\ufe0f\u200d\u2642\ufe0f",  # 🏋️‍♂️
        "\U0001F3CB\ufe0f\u200d\u2640\ufe0f",  # 🏋️‍♀️
    ]

    for emoji in composites:
        text = text.replace(emoji, '')

    return emoji_pattern.sub(r'', text)

# ----------------- Initialize Agent and User Context -----------------
agent = create_health_wellness_agent()
context = UserSessionContext(name="User", uid=1)

# ----------------- User Input Form -----------------
with st.form(key="user_form"):
    user_input = st.text_input(
        "💬 Ask a health-related question (e.g., 'goal, meal, injury, vitamin, progress...')",
        key="input"
    )
    submit = st.form_submit_button("Send")

# ----------------- Agent Response Section -----------------
if submit and user_input:
    with st.spinner("🔄 Thinking..."):
        response = asyncio.run(agent.run(user_input))

    st.success("✅ Agent Response")
    st.markdown(f"**🗣️ You:** {user_input}")
    st.markdown(f"**🤖 Agent:** {response}")

    # Save for PDF download
    st.session_state["last_response"] = response
    st.session_state["last_question"] = user_input

# ----------------- Download PDF Section -----------------
if "last_response" in st.session_state:
    if st.button("📄 Download Response as PDF"):
        # Remove emojis and em dash before saving to PDF
        clean_question = remove_emojis(st.session_state["last_question"]).replace("—", "-")
        clean_response = remove_emojis(st.session_state["last_response"]).replace("—", "-")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, f"Question: {clean_question}\n\nResponse:\n{clean_response}")

        file_path = "health_response.pdf"
        pdf.output(file_path)

        with open(file_path, "rb") as f:
            st.download_button(
                label="⬇️ Download PDF",
                data=f,
                file_name="HealthResponse.pdf",
                mime="application/pdf"
            )
