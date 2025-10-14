import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# ================= CẤU HÌNH TRANG =================
st.set_page_config(page_title="🧠 Sắp xếp lịch học", layout="wide")

# ================= KIỂM TRA ĐĂNG NHẬP =================
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⚠️ Bạn cần đăng nhập để truy cập trang này.")
    st.stop()

username = st.session_state.get("username", "Người dùng")

# ================= HEADER =================
st.title("🧠 TRỢ LÝ SẮP XẾP LỊCH HỌC THÔNG MINH")
st.markdown(f"### Xin chào, **{username}** 👋")
st.caption("Công cụ gợi ý lịch học hiệu quả giúp bạn cân bằng giữa thời gian học và nghỉ ngơi.")

st.markdown("---")

# ================= CẤU HÌNH NGƯỜI DÙNG =================
st.subheader("⚙️ Cấu hình ưu tiên học tập")

col1, col2 = st.columns(2)
with col1:
    so_mon = st.number_input("📚 Số môn học trong kỳ", 1, 10, 5)
    gio_uu_tien = st.slider("🕐 Giờ học tối đa mỗi ngày", 1, 6, 3)
with col2:
    ngay_bat_dau = st.date_input("📅 Ngày bắt đầu học", datetime.now())
    uu_tien_mon = st.selectbox(
        "🏆 Ưu tiên môn học nào nhất?",
        ["Tất cả như nhau", "Lập trình Python", "Cơ sở dữ liệu", "Mạng máy tính", "Trí tuệ nhân tạo"],
    )

if st.button("✨ Gợi ý lịch học tự động"):
    st.success("✅ Đã tạo gợi ý lịch học phù hợp!")

    # ====== Sinh dữ liệu demo ======
    ngay = ["Th 2", "Th 3", "Th 4", "Th 5", "Th 6", "Th 7"]
    mon = np.random.choice(
        ["Python", "CSDL", "Mạng", "AI", "Cấu trúc DL"], size=6, replace=True
    )
    gio = np.random.randint(1, 4, size=6)

    df = pd.DataFrame({"Ngày": ngay, "Môn học": mon, "Giờ học": gio})

    # ====== Hiển thị bảng ======
    st.markdown("### 🗓️ Lịch học đề xuất")
    st.table(df)

    # ====== Biểu đồ cột ======
    st.markdown("### 📊 Biểu đồ thời gian học trong tuần")
    fig, ax = plt.subplots()
    ax.bar(df["Ngày"], df["Giờ học"], color="skyblue")
    ax.set_ylabel("Giờ học")
    ax.set_title("Phân bổ thời gian học trong tuần")
    st.pyplot(fig)

# ================= GỢI Ý HỌC TẬP AI =================
st.markdown("---")
st.subheader("🤖 Gợi ý học tập từ AI")

with st.expander("Xem gợi ý chi tiết"):
    st.markdown("""
    - 📅 Học 2-3 giờ mỗi ngày giúp duy trì tập trung tối ưu.  
    - 🧘 Đừng quên nghỉ ngơi sau 45 phút học.  
    - 💡 Học môn khó (như AI hoặc CSDL) vào buổi sáng giúp tiếp thu tốt hơn.  
    - ✍️ Ôn lại bài cũ trước khi học bài mới để củng cố kiến thức.  
    """)

# ================= CHÂN TRANG =================
st.markdown("---")
st.info("💡 *Mẹo:* Sử dụng công cụ này mỗi tuần để tối ưu lịch học và nâng cao hiệu suất.")
st.caption(f"© {datetime.now().year} | Trợ lý sắp xếp lịch học - Phiên bản Demo")
