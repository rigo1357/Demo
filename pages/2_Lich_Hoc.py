import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# ================= CẤU HÌNH TRANG =================
st.set_page_config(page_title="📅 Lịch học", layout="wide")

# ================= KIỂM TRA ĐĂNG NHẬP =================
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⚠️ Bạn cần đăng nhập để truy cập trang này.")
    st.stop()

username = st.session_state.get("username", "Người dùng")

# ================= HEADER =================
st.title("📅 LỊCH HỌC CÁ NHÂN")
st.markdown(f"### Xin chào, **{username}** 👋")
st.caption("Dưới đây là thời khóa biểu và các buổi học sắp tới của bạn.")

st.markdown("---")

# ================= TÙY CHỌN HIỂN THỊ =================
col1, col2 = st.columns([1, 3])
with col1:
    view_mode = st.radio("🔍 Chế độ xem:", ["Theo tuần", "Theo tháng"], horizontal=True)
with col2:
    selected_week = st.selectbox("📆 Chọn tuần:", [f"Tuần {i}" for i in range(1, 6)])

# ================= DỮ LIỆU GIẢ LẬP =================
start_date = datetime.now().date()

sample_data = [
    {"Ngày": start_date + timedelta(days=0), "Môn học": "Cấu trúc dữ liệu", "Phòng": "A101", "Thời gian": "07:30 - 09:30"},
    {"Ngày": start_date + timedelta(days=1), "Môn học": "Cơ sở dữ liệu", "Phòng": "B203", "Thời gian": "09:45 - 11:30"},
    {"Ngày": start_date + timedelta(days=2), "Môn học": "Lập trình Python", "Phòng": "C105", "Thời gian": "13:00 - 15:00"},
    {"Ngày": start_date + timedelta(days=3), "Môn học": "Toán rời rạc", "Phòng": "D202", "Thời gian": "07:00 - 09:00"},
]

df = pd.DataFrame(sample_data)

# ================= HIỂN THỊ DỮ LIỆU =================
st.subheader(f"🗓️ {view_mode}: {selected_week}")
st.dataframe(df, use_container_width=True, hide_index=True)

# ================= THỐNG KÊ NHỎ =================
st.markdown("---")
colA, colB, colC = st.columns(3)
with colA:
    st.metric("🧾 Tổng số buổi học", len(df))
with colB:
    st.metric("🏫 Số phòng học khác nhau", df["Phòng"].nunique())
with colC:
    st.metric("📘 Môn học đang học", df["Môn học"].nunique())

# ================= GHI CHÚ =================
with st.expander("📖 Ghi chú - lưu ý trong tuần"):
    st.write("""
    - Nộp bài tập lớn Python vào **thứ 6, 17/10/2025**.
    - Ôn tập chương 3 môn CSDL.
    - Tuần sau có kiểm tra giữa kỳ môn Toán rời rạc.
    """)

# ================= CHÂN TRANG =================
st.markdown("---")
st.success("✅ Giao diện Lịch học đã sẵn sàng (placeholder).")
st.caption(f"© {datetime.now().year} | Trang lịch học sinh viên TDMU - Phiên bản Demo")
