import streamlit as st
import json
import os
import time
from openai import OpenAI

# ==========================
# HÀM XỬ LÝ NGƯỜI DÙNG
# ==========================
def load_users():
    """Đọc file users.json (nếu lỗi thì trả về rỗng)."""
    if not os.path.exists("users.json"):
        with open("users.json", "w") as f:
            json.dump({}, f)

    with open("users.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_users(users):
    """Ghi lại danh sách người dùng vào file."""
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

# ==========================
# CẤU HÌNH GIAO DIỆN
# ==========================
st.set_page_config(
    page_title="🎓 Cổng thông tin sinh viên TDMU",
    page_icon="🎓",
    layout="wide"
)

# CSS tùy chỉnh giao diện tổng thể
st.markdown("""
<style>
body { background-color: #f5f8ff; }
h1, h2, h3, h4, h5 {
    font-family: 'Inter', sans-serif;
}
.sidebar .sidebar-content {
    background-color: #004aad;
    color: white;
}
.block-container {
    padding-top: 2rem;
}
.stButton>button {
    border-radius: 8px;
    background: linear-gradient(90deg, #004aad, #007bff);
    color: white;
    font-weight: 600;
}
.login-box {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    width: 420px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# SESSION KIỂM TRA
# ==========================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# ==========================
# GIAO DIỆN ĐĂNG NHẬP / ĐĂNG KÝ
# ==========================
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align:center;'>🔐 Đăng nhập / Đăng ký hệ thống</h1>", unsafe_allow_html=True)
    st.caption("Cổng thông tin sinh viên TDMU - Tư vấn và sắp xếp lịch học thông minh 🎓")

    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    action = st.radio("Chọn thao tác:", ["Đăng nhập", "Đăng ký"], horizontal=True)
    username = st.text_input("👤 Tên đăng nhập:")
    password = st.text_input("🔑 Mật khẩu:", type="password")

    users = load_users()

    if action == "Đăng ký":
        if st.button("📝 Đăng ký"):
            if username in users:
                st.warning("⚠️ Tên đăng nhập đã tồn tại!")
            elif username == "" or password == "":
                st.warning("⚠️ Không được để trống thông tin!")
            else:
                users[username] = {"password": password}
                save_users(users)
                st.success("✅ Đăng ký thành công! Hãy đăng nhập ngay.")
    else:
        if st.button("🚀 Đăng nhập"):
            if username in users and users[username]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.toast(f"🎉 Chào mừng {username} quay lại hệ thống!", icon="🎓")
                st.rerun()
            else:
                st.error("❌ Sai tên đăng nhập hoặc mật khẩu!")
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ==========================
# HÀM CHATBOT
# ==========================
def run_chatbot():
    st.title("💬 Chatbot tư vấn học tập thông minh")

    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

    PROMPT = """
    Em là trợ lý học tập thân thiện, nói chuyện hoàn toàn bằng tiếng Việt tự nhiên.
    Trả lời ngắn gọn, có cảm xúc, và giúp sinh viên học tốt hơn.
    """

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": PROMPT}]

    for msg in st.session_state.messages[1:]:
        st.chat_message(msg["role"]).write(msg["content"])

    if user_input := st.chat_input("Nhập tin nhắn..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        with st.spinner("Đang trả lời..."):
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
                placeholder.markdown(reply + "▌")
                time.sleep(0.02)
            placeholder.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

# ==========================
# GIAO DIỆN CHÍNH SAU KHI ĐĂNG NHẬP
# ==========================
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/3/37/Logo_TDMU.png", width=80)
st.sidebar.title("🎓 Cổng thông tin sinh viên TDMU")

menu = st.sidebar.radio(
    "📂 Chọn trang:",
    ["🏠 Trang chủ", "📅 Lịch học", "📘 Sắp xếp lịch học", "💬 Chatbot tư vấn", "👤 Hồ sơ cá nhân", "🚪 Đăng xuất"]
)

st.sidebar.markdown("---")
st.sidebar.caption(f"👋 Xin chào, **{st.session_state.username}**")

# ==========================
# NỘI DUNG CÁC TRANG
# ==========================
if menu == "🏠 Trang chủ":
    st.markdown("""
    <div style='background:linear-gradient(90deg,#004aad,#007bff);
                color:white;padding:1.2rem;border-radius:10px;text-align:center;'>
        <h2>🎓 HỆ THỐNG TƯ VẤN & SẮP XẾP LỊCH HỌC THÔNG MINH</h2>
    </div>
    """, unsafe_allow_html=True)
    st.write("""
    Xin chào **{}** 👋  
    - 📅 Xem và sắp xếp thời khóa biểu tối ưu  
    - 🤖 Nhận gợi ý từ chatbot học tập  
    - 👤 Quản lý hồ sơ sinh viên  
    """.format(st.session_state.username))
    st.image("https://cdn.dribbble.com/users/252114/screenshots/11818310/media/bb992e04b8ce64e3e26a8d1f72826317.png", use_column_width=True)

elif menu == "📅 Lịch học":
    st.title("📅 Lịch học")
    st.info("Tính năng hiển thị thời khóa biểu chi tiết có trong `2_Lich_Hoc.py`.")

elif menu == "📘 Sắp xếp lịch học":
    st.title("📘 Sắp xếp lịch học thông minh")
    st.success("✅ Tính năng đề xuất lịch học tối ưu đang được tích hợp từ module `4_Sap_Xep_Lich.py`.")

elif menu == "💬 Chatbot tư vấn":
    run_chatbot()

elif menu == "👤 Hồ sơ cá nhân":
    st.title("👤 Hồ sơ cá nhân")
    st.write(f"Tài khoản hiện tại: **{st.session_state.username}**")
    st.info("Xem thêm thông tin chi tiết trong `3_Ho_So.py`.")

elif menu == "🚪 Đăng xuất":
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.toast("👋 Đã đăng xuất khỏi hệ thống.", icon="✅")
    st.rerun()
