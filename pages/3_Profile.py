import streamlit as st
from datetime import datetime

# ================= CẤU HÌNH TRANG =================
st.set_page_config(page_title="👤 Hồ sơ cá nhân", layout="wide")

# ================= KIỂM TRA ĐĂNG NHẬP =================
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⚠️ Bạn cần đăng nhập để truy cập trang này.")
    st.stop()

username = st.session_state.get("username", "Người dùng")

# ================= HEADER =================
st.title("👤 HỒ SƠ CÁ NHÂN")
st.markdown(f"### Xin chào, **{username}** 👋")
st.caption("Quản lý và cập nhật thông tin sinh viên của bạn.")

st.markdown("---")

# ================= GIAO DIỆN HỒ SƠ =================
col_avatar, col_info = st.columns([1, 2])
with col_avatar:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/1946/1946429.png",
        width=150,
        caption="Ảnh đại diện",
    )
    st.markdown("🟢 **Trạng thái:** Đang hoạt động")
    st.markdown(f"⏰ Lần đăng nhập gần nhất: **{datetime.now().strftime('%H:%M %d/%m/%Y')}**")

with col_info:
    st.subheader("🧾 Thông tin sinh viên")
    with st.form("form_profile"):
        col1, col2 = st.columns(2)
        with col1:
            hoten = st.text_input("👤 Họ và tên", "Nguyễn Văn A")
            masv = st.text_input("🎓 Mã sinh viên", "SV001")
            sdt = st.text_input("📞 Số điện thoại", "0123456789")
        with col2:
            email = st.text_input("✉️ Email", f"{username}@tdmu.edu.vn")
            nganh = st.text_input("🏫 Ngành học", "Công nghệ thông tin")
            lop = st.text_input("📍 Lớp", "DCT123")

        submitted = st.form_submit_button("💾 Cập nhật thông tin")
        if submitted:
            st.success("✅ Thông tin đã được cập nhật (demo).")

st.markdown("---")

# ================= PHẦN THỐNG KÊ =================
st.subheader("📊 Thống kê học tập nhanh")
colA, colB, colC, colD = st.columns(4)
colA.metric("📘 Tổng số môn học", "5", "+1")
colB.metric("💯 Điểm trung bình (GPA)", "3.45", "+0.1")
colC.metric("🏆 Thành tích", "Sinh viên giỏi", "")
colD.metric("🎯 Mục tiêu học kỳ này", "3.7 GPA")

# ================= GHI CHÚ =================
with st.expander("📝 Ghi chú cá nhân"):
    st.write("""
    - Hoàn thành đồ án môn **Cơ sở dữ liệu** trước 25/10/2025.
    - Ôn tập giữa kỳ **Python nâng cao**.
    - Tham gia hội thảo "AI & Ứng dụng trong giáo dục" vào ngày 20/10.
    """)

# ================= CHÂN TRANG =================
st.markdown("---")
st.info("💡 *Mẹo:* Cập nhật thông tin đầy đủ giúp nhà trường dễ dàng hỗ trợ học tập và học bổng.")
st.caption(f"© {datetime.now().year} | Hồ sơ sinh viên - Phiên bản Demo")
