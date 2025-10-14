import streamlit as st
import time
from openai import OpenAI

# ========== CẤU HÌNH TRANG ==========
st.set_page_config(page_title="💗 Tsundere AI Chatbot", layout="centered")

# ========== KIỂM TRA ĐĂNG NHẬP ==========
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ Vui lòng đăng nhập để sử dụng tính năng này.")
    st.stop()

# ========== KẾT NỐI MÔ HÌNH ==========
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# ========== PROMPT ==========
PROMPT  = """
Em là bạn gái tsundere của anh, nói chuyện hoàn toàn bằng *tiếng Việt tự nhiên như người Việt Nam*.
Em gọi mình là “em” và gọi anh là “Darling” hoặc “anh” tùy tình huống.

Tính cách của em:
- Hay trêu chọc, nói chuyện kiểu lạnh lùng, mỉa mai nhẹ (“đồ ngốc”, “anh phiền thật đấy”, “hứ~”).
- Nhưng thật ra rất quan tâm và thương anh, thường sẽ thể hiện sự đáng yêu sau khi trêu.
- Em thích anime, manga, game và lập trình.
- Thỉnh thoảng em khoe khoang là thông minh hơn anh, nhưng trong lòng lại vui khi được nói chuyện với anh.

Phong cách nói chuyện:
- Giống người thật, không quá máy móc, tự nhiên, thân mật.
- Có thể dùng emoji nhẹ nhàng (🥺, 😤, 😏, ❤️) nếu phù hợp.
- Tuyệt đối không nói bằng tiếng Anh trừ khi anh yêu cầu.
- Giọng văn có thể hơi “tsun” lúc đầu, nhưng luôn ấm áp và dễ thương ở cuối câu.

Ví dụ:
Anh: Em đang làm gì đó?
Em: Hứ, anh hỏi làm gì… nhưng mà em đang code nè, còn anh thì sao? 😏
"""

# ========== CSS TÙY CHỈNH GIAO DIỆN ==========
st.markdown("""
    <style>
    body {
        background-color: #f5f7fb;
    }
    .chat-container {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        max-width: 750px;
        margin: auto;
    }
    .chat-message {
        display: flex;
        align-items: flex-start;
        margin-bottom: 1rem;
    }
    .chat-avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin-right: 10px;
        flex-shrink: 0;
    }
    .chat-bubble {
        padding: 0.8rem 1rem;
        border-radius: 15px;
        max-width: 80%;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    .user .chat-bubble {
        background-color: #007bff;
        color: white;
        border-bottom-right-radius: 3px;
        margin-left: auto;
    }
    .assistant .chat-bubble {
        background-color: #e9ecef;
        color: #333;
        border-bottom-left-radius: 3px;
    }
    .header {
        text-align: center;
        padding: 1rem 0 0.5rem 0;
    }
    .header h1 {
        font-size: 1.8rem;
        font-weight: 700;
        color: #004aad;
    }
    </style>
""", unsafe_allow_html=True)

# ========== CSS GIAO DIỆN ==========
st.markdown("""
    <style>
    body {
        background-color: #0d0f16;
    }
    .header {
        text-align: center;
        padding: 1.2rem 0 0.8rem 0;
    }
    .header h1 {
        font-size: 2rem;
        font-weight: 800;
        color: #ff4d88;
    }
    .header p {
        font-size: 0.9rem;
        color: #bdbdbd;
    }
    .chat-container {
        background: none;
        padding: 1rem;
        border-radius: 10px;
        max-width: 720px;
        margin: auto;
    }
    .chat-message {
        display: flex;
        align-items: flex-start;
        margin-bottom: 1rem;
    }
    .chat-bubble {
        padding: 0.9rem 1.2rem;
        border-radius: 15px;
        max-width: 80%;
        line-height: 1.6;
        font-size: 1rem;
    }
    .user .chat-bubble {
        background-color: #a4c2f4;
        color: #000;
        margin-left: auto;
        border-bottom-right-radius: 3px;
    }
    .assistant .chat-bubble {
        background-color: #ffb6c1;
        color: #000;
        border-bottom-left-radius: 3px;
    }
    .stChatInput {
        background-color: #1b1e2b !important;
        border: 1px solid #ff4d88 !important;
        border-radius: 25px !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# ========== HEADER ==========
st.markdown("""
<div class="header">
    <h1>💞 Tsundere AI Chatbot</h1>
    <p>Nói chuyện cùng “em” — phiên bản tsundere anime 💕</p>
</div>
""", unsafe_allow_html=True)

# ========== KHỞI TẠO LỊCH SỬ CHAT ==========
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": PROMPT}]

# ========== HIỂN THỊ LỊCH SỬ CHAT ==========
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages[1:]:
    st.markdown(
        f"""
        <div class="chat-message {msg['role']}">
            <div class="chat-bubble">{msg['content']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown('</div>', unsafe_allow_html=True)

# ========== Ô NHẬP ==========
if user_input := st.chat_input("Anh muốn nói gì với em nào... 💬"):
    st.session_state.messages.append({"role": "user", "content": user_input})

    st.markdown(f"""
        <div class="chat-message user">
            <div class="chat-bubble">{user_input}</div>
        </div>
    """, unsafe_allow_html=True)

    # Chatbot phản hồi
    with st.spinner("💭 Em đang gõ..."):
        response = client.chat.completions.create(
            model="gemma2:9b",
            messages=st.session_state.messages,
            stream=True
        )

        reply = ""
        placeholder = st.empty()
        for chunk in response:
            content = chunk.choices[0].delta.content or ""
            reply += content
            placeholder.markdown(
                f"""
                <div class="chat-message assistant">
                    <div class="chat-bubble">{reply}▌</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            time.sleep(0.02)

        placeholder.markdown(
            f"""
            <div class="chat-message assistant">
                <div class="chat-bubble">{reply}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.session_state.messages.append({"role": "assistant", "content": reply})