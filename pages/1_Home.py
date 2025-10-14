import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =============================
# CẤU HÌNH TRANG
# =============================
st.set_page_config(page_title="🎓 Cổng thông tin sinh viên", layout="wide")

# =============================
# KIỂM TRA ĐĂNG NHẬP
# =============================
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ Vui lòng đăng nhập để truy cập trang này!")
    st.stop()

username = st.session_state.get("username", "Sinh viên")

# =============================
# PHẦN HEADER / BANNER
# =============================
st.markdown(
    f"""
    <style>
    .banner {{
        background: linear-gradient(90deg, #004aad, #007bff);
        color: white;
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }}
    .banner h1 {{
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }}
    .banner p {{
        font-size: 1.1rem;
        opacity: 0.9;
    }}
    </style>
    <div class="banner">
        <h1>🎓 CỔNG THÔNG TIN SINH VIÊN - TDMU</h1>
        <p>Chào mừng <b>{username}</b> đến với hệ thống quản lý và tư vấn học tập thông minh!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# =============================
# THỐNG KÊ TỔNG QUAN
# =============================
st.subheader("📊 Thống kê học tập tổng quan")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("📘 Tổng số môn học", "5", "+1 so với tháng trước")
with col2:
    st.metric("📅 Buổi học sắp tới", "2", "-1 so với tuần trước")
with col3:
    st.metric("⏱️ Thời gian học trung bình", "2h 15p", "+10% so với tuần trước")
with col4:
    st.metric("🔥 Hiệu suất học tập", "85%", "+5% so với tháng trước")

st.markdown("---")

# =============================
# BIỂU ĐỒ TIẾN ĐỘ HỌC TẬP
# =============================
st.subheader("📈 Tiến độ học tập 8 tuần gần đây")

weeks = [f"Tuần {i}" for i in range(1, 9)]
progress = np.random.randint(60, 100, size=8)

fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(weeks, progress, marker="o", color="#007bff", linewidth=2)
ax.fill_between(weeks, progress, color="#cce5ff", alpha=0.4)
ax.set_ylim(0, 100)
ax.set_ylabel("Hoàn thành (%)")
ax.set_title("Mức độ hoàn thành học tập", fontsize=12)
st.pyplot(fig)

# =============================
# BIỂU ĐỒ CỘT: THỜI GIAN HỌC TRONG TUẦN
# =============================
st.subheader("📚 Thời gian học mỗi ngày trong tuần")

days = ["Th 2", "Th 3", "Th 4", "Th 5", "Th 6", "Th 7", "CN"]
hours = np.random.randint(1, 5, size=7)
chart_data = pd.DataFrame({"Ngày": days, "Giờ học": hours})
st.bar_chart(chart_data, x="Ngày", y="Giờ học", height=300)

# =============================
# TIN TỨC / THÔNG BÁO NHÀ TRƯỜNG
# =============================
st.markdown("---")
st.subheader("📰 Thông báo mới từ nhà trường")

news_col1, news_col2 = st.columns(2)
with news_col1:
    st.markdown("""
    **📢 Thông báo đăng ký học phần học kỳ II (2025–2026)**  
    - Thời gian: từ **10/11 đến 25/11/2025**  
    - Đăng ký qua cổng sinh viên tại [portal.tdmu.edu.vn](https://portal.tdmu.edu.vn)  
    """)
    st.markdown("""
    **🎓 Lễ tốt nghiệp dự kiến tháng 12/2025**  
    - Sinh viên đủ điều kiện sẽ được nhà trường gửi email xác nhận lịch cụ thể.  
    """)

with news_col2:
    st.markdown("""
    **🏫 Khai giảng năm học mới 2025–2026**  
    - Dự kiến tổ chức vào **ngày 05/09/2025** tại hội trường lớn cơ sở chính.  
    """)
    st.markdown("""
    **💡 Hội thảo “AI trong giáo dục đại học”**  
    - Diễn ra lúc **08:00 ngày 20/10/2025** tại phòng A203.  
    """)

# =============================
# MẸO HỌC TẬP
# =============================
st.markdown("---")
st.info("💡 *Mẹo:* Duy trì thời gian học đều đặn mỗi ngày giúp cải thiện kết quả học tập lên đến **30%**!")
