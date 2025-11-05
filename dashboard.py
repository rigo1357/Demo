import streamlit as st
from datetime import datetime
import numpy as np
import pandas as pd

# ================= CẤU HÌNH TRANG =================
st.set_page_config(page_title="🎓 Dashboard Sinh viên TDMU", layout="wide", page_icon="🎓")

# ================= KIỂM TRA ĐĂNG NHẬP =================
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

# ================= GIAO DIỆN CHUNG (CSS) =================
st.markdown("""
<style>
/* Toàn trang */
body { background-color: #f7f9fc; }
h1, h2, h3, h4, h5 { font-family: 'Inter', sans-serif; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #004aad, #007bff);
    color: white;
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
    color: white !important;
}
.sidebar .sidebar-content { color: white; }

/* Nút bấm */
.stButton>button {
    border-radius: 8px;
    background: linear-gradient(90deg, #004aad, #007bff);
    color: white;
    font-weight: 600;
}

/* Header */
.header {
    background: linear-gradient(90deg, #004aad, #007bff);
    padding: 1rem 2rem;
    color: white;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 1.5rem;
    box-shadow: 0 3px 8px rgba(0,0,0,0.1);
}

/* Footer */
footer {
    text-align: center;
    color: #888;
    font-size: 0.9rem;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/37/Logo_TDMU.png", width=90)
    st.markdown("### 🎓 Cổng sinh viên TDMU")
    st.markdown(f"👋 Xin chào, **{st.session_state.username}**")
    st.markdown("---")
    menu = st.radio("📂 Chọn chức năng:", [
        "🏠 Trang chủ",
        "💬 Chatbot tư vấn",
        "📅 Lịch học",
        "🧠 Sắp xếp lịch học",
        "👤 Hồ sơ cá nhân",
        "🚪 Đăng xuất"
    ])
    st.markdown("---")
    st.caption("© 2025 | Hệ thống TDMU AI Dashboard")

# ================= NỘI DUNG =================
st.markdown("<div class='header'><h2>📊 BẢNG ĐIỀU KHIỂN HỌC TẬP SINH VIÊN</h2></div>", unsafe_allow_html=True)

if menu == "🏠 Trang chủ":
    st.subheader("📘 Tổng quan học tập")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📈 Tiến độ học tập", "85%", "+5%")
    col2.metric("🧑‍💻 Số môn học", "5", "+1")
    col3.metric("📅 Buổi học sắp tới", "2", "-1")
    col4.metric("🎯 Hiệu suất học", "Tốt", "")

    st.markdown("### 📉 Biểu đồ tiến độ 8 tuần gần đây")
    weeks = [f"Tuần {i}" for i in range(1, 9)]
    progress = np.random.randint(60, 100, size=8)
    df = pd.DataFrame({"Tuần": weeks, "Tiến độ (%)": progress})
    st.line_chart(df, x="Tuần", y="Tiến độ (%)", height=300)

    st.markdown("### 📊 Thời gian học mỗi ngày (giờ)")
    days = ["Th 2", "Th 3", "Th 4", "Th 5", "Th 6", "Th 7", "CN"]
    hours = np.random.randint(1, 5, size=7)
    st.bar_chart(pd.DataFrame({"Ngày": days, "Giờ học": hours}), x="Ngày", y="Giờ học")

    st.markdown("---")
    st.info("💡 *Mẹo:* Duy trì 2–3 giờ học mỗi ngày giúp cải thiện kết quả học tập tới 30%!")

elif menu == "💬 Chatbot tư vấn":
    st.subheader("💬 Trợ lý học tập thông minh")
    st.info("Khung chat sẽ được tích hợp trực tiếp từ tính năng Chatbot trong `app.py`.")

elif menu == "📅 Lịch học":
    st.subheader("📅 Quản lý thời khóa biểu")
    st.info("Trang quản lý lịch học chi tiết đã có trong `2_Lich_Hoc.py`.")

elif menu == "🧠 Sắp xếp lịch học":
    st.subheader("🧠 Trợ lý sắp xếp lịch học thông minh")
    st.success("Tính năng tự động gợi ý lịch học tối ưu đang được tích hợp trong `4_Sap_Xep_Lich.py`.")

elif menu == "👤 Hồ sơ cá nhân":
    st.subheader("👤 Hồ sơ sinh viên")
    st.write(f"**Tên đăng nhập:** {st.session_state.username}")
    name = st.text_input("Họ và tên", "Nguyễn Văn A")
    email = st.text_input("Email", f"{st.session_state.username}@tdmu.edu.vn")
    st.text_area("Giới thiệu bản thân", "Yêu công nghệ, thích AI 💻")
    st.button("💾 Cập nhật thông tin")

elif menu == "🚪 Đăng xuất":
    st.session_state.logged_in = False
    st.toast("👋 Đã đăng xuất khỏi hệ thống.", icon="✅")
    st.switch_page("app.py")

# ================= CHÂN TRANG =================
st.markdown(f"<footer>© {datetime.now().year} | Trường Đại học Thủ Dầu Một | Phiên bản Dashboard 2.0</footer>", unsafe_allow_html=True)
