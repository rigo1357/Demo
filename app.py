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
st.set_page_config(page_title="🎓 Cổng thông tin sinh viên", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# ==========================
# GIAO DIỆN ĐĂNG NHẬP / ĐĂNG KÝ
# ==========================
if not st.session_state.logged_in:
    st.title("🔐 Đăng nhập / Đăng ký hệ thống")
    st.caption("Hệ thống tư vấn và sắp xếp lịch học thông minh 🎓")

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
                st.success(f"🎉 Chào mừng {username} quay lại hệ thống!")
                st.rerun()
            else:
                st.error("❌ Sai tên đăng nhập hoặc mật khẩu!")

# ==========================
# HÀM CHATBOT
# ==========================
def run_chatbot():
    st.title("💬 Chatbot tư vấn học tập")

    # Kiểm tra đăng nhập
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.warning("Vui lòng đăng nhập để sử dụng chatbot.")
        return

    # Cấu hình client Ollama
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

    PROMPT = """
    Em là bạn gái tsundere của anh, nói chuyện hoàn toàn bằng *tiếng Việt tự nhiên như người Việt Nam*.
    Em gọi mình là “em” và gọi anh là “Darling” hoặc “anh” tùy tình huống.
    """

    # Khởi tạo lịch sử chat
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": PROMPT}]

    # Hiển thị lịch sử chat
    for msg in st.session_state.messages[1:]:
        st.chat_message(msg["role"]).write(msg["content"])

    # Nhập tin nhắn
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

    else:
        st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/3/37/Logo_TDMU.png", width=80)
    st.sidebar.title("🎓 Cổng thông tin sinh viên")

    menu = st.sidebar.radio(
        "📂 Chọn trang:",
        ["🏠 Trang chủ", "📅 Lịch học", "📘 Sắp xếp lịch học", "💬 Chatbot tư vấn", "👤 Hồ sơ cá nhân", "🚪 Đăng xuất"]
    )

    st.sidebar.markdown("---")
    st.sidebar.caption(f"👋 Xin chào, **{st.session_state.username}**")

    if menu == "🏠 Trang chủ":
        st.title("🏠 Trang chủ")
        st.markdown("""
        Chào mừng bạn đến với **Hệ thống tư vấn và sắp xếp lịch học thông minh** 🎓  
        - 📅 Xem và sắp xếp thời khóa biểu tối ưu  
        - 🤖 Nhận gợi ý từ chatbot học tập  
        - 👤 Quản lý hồ sơ sinh viên  
        """)

    elif menu == "📅 Lịch học":
        st.title("📅 Lịch học")
        st.info("Tính năng hiển thị thời khóa biểu của sinh viên sẽ được cập nhật sau.")

    elif menu == "📘 Sắp xếp lịch học":
        st.title("📘 Sắp xếp lịch học thông minh")
        st.write("Sử dụng thuật toán **Genetic Algorithm (GA)** để đề xuất lịch học tối ưu.")
        st.success("✅ Tính năng đang được tích hợp từ module 'SapXepLich.py'.")

    elif menu == "💬 Chatbot tư vấn":
        run_chatbot()

    elif menu == "👤 Hồ sơ cá nhân":
        st.title("👤 Hồ sơ cá nhân")
        st.write(f"Tài khoản hiện tại: **{st.session_state.username}**")
        st.write("Thông tin sinh viên, lớp, và chuyên ngành sẽ được cập nhật trong bản chính thức.")

    elif menu == "🚪 Đăng xuất":
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.success("👋 Đã đăng xuất khỏi hệ thống.")
        st.rerun()
