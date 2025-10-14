import streamlit as st

st.set_page_config(page_title="Dashboard - Demo", layout="wide")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #202225;
            color: white;
        }
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        h1, h2, h3, h4 {
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=80)
    st.title("Demo Panel")
    st.markdown(f"👋 Xin chào, **{st.session_state.username}**")
    st.markdown("---")
    menu = st.radio("Chọn chức năng:", [
        "🏠 Home",
        "💬 Chatbot",
        "📅 Lịch học",
        "👤 Hồ sơ cá nhân",
        "🧠 Sắp xếp lịch học",
        "🚪 Đăng xuất"
    ])
    st.markdown("---")
    st.caption("© 2025 Demo AI Dashboard")

if menu == "🏠 Home":
    st.title("📊 Trang chủ")
    st.write("Chào mừng bạn đến với hệ thống quản lý và tư vấn lịch học.")
    st.image("https://cdn.dribbble.com/users/252114/screenshots/11818310/media/bb992e04b8ce64e3e26a8d1f72826317.png", use_column_width=True)

elif menu == "💬 Chatbot":
    st.title("💬 Chatbot tư vấn")
    st.info("Chức năng Chatbot sẽ hiển thị khung chat bạn đã có sẵn ở đây.")

elif menu == "📅 Lịch học":
    st.title("📅 Quản lý lịch học")
    st.info("Chức năng thêm / xóa / xem lịch học (sẽ hoàn thiện sau).")

elif menu == "👤 Hồ sơ cá nhân":
    st.title("👤 Hồ sơ người dùng")
    name = st.text_input("Tên hiển thị:", st.session_state.username)
    bio = st.text_area("Giới thiệu:", "Yêu công nghệ và AI 💻")
    st.button("💾 Lưu thay đổi")

elif menu == "🧠 Sắp xếp lịch học":
    st.title("🧠 Trợ lý sắp xếp lịch học")
    st.info("Thuật toán sắp xếp sẽ thêm sau (chưa cần).")

elif menu == "🚪 Đăng xuất":
    st.session_state.logged_in = False
    st.switch_page("app.py")

col1, col2, col3, col4 = st.columns(4)
col1.metric("📈 Total Traffic", "325,456", "+5%")
col2.metric("🧑‍💻 New Users", "3,006", "-4.54%")
col3.metric("⚙️ Performance", "60%", "+2.54%")
col4.metric("💰 Sales", "852", "+6.54%")

st.line_chart([100, 200, 150, 300, 400, 350, 450])
st.bar_chart([200, 400, 600, 800, 700, 900, 1000])
