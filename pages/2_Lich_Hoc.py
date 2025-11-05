import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px

# =================== CẤU HÌNH TRANG ===================
st.set_page_config(page_title="📅 Quản lý Lịch học nâng cao", layout="wide", page_icon="📚")

# =================== KIỂM TRA ĐĂNG NHẬP ===================
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⚠️ Bạn cần đăng nhập để truy cập trang này.")
    st.stop()

username = st.session_state.get("username", "Sinh viên")

# =================== CSS GIAO DIỆN ===================
st.markdown("""
<style>
body { background-color: #f0f2f6; }
h1, h2, h3, h4, h5 { font-family: "Inter", sans-serif; }
.stMetric { background-color: white; padding: 10px; border-radius: 12px; box-shadow: 0 3px 6px rgba(0,0,0,0.05); }
div[data-testid="stDataFrame"] table { border-radius: 10px; overflow: hidden; }
button[kind="primary"] {
    background: linear-gradient(90deg, #004aad, #007bff);
    border: none;
    color: white;
    border-radius: 8px;
}
.add-box {
    background: white;
    border-radius: 10px;
    padding: 1.5rem;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# =================== HEADER ===================
st.markdown(f"""
<div style='background:linear-gradient(90deg,#004aad,#007bff);
            color:white;padding:1rem 2rem;border-radius:12px;
            text-align:center;box-shadow:0 3px 8px rgba(0,0,0,0.15);'>
    <h2>📅 LỊCH HỌC CÁ NHÂN - {username.upper()}</h2>
    <p>Quản lý – Theo dõi – Cập nhật lịch học thông minh</p>
</div>
""", unsafe_allow_html=True)
st.markdown("")

# =================== DỮ LIỆU GIẢ LẬP ===================
today = datetime.now().date()
df = pd.DataFrame([
    {"Ngày": today + timedelta(days=0), "Môn học": "Cấu trúc dữ liệu", "Phòng": "A101", "Giờ học": "07:30 - 09:30"},
    {"Ngày": today + timedelta(days=1), "Môn học": "Cơ sở dữ liệu", "Phòng": "B203", "Giờ học": "09:45 - 11:30"},
    {"Ngày": today + timedelta(days=2), "Môn học": "Lập trình Python", "Phòng": "C105", "Giờ học": "13:00 - 15:00"},
    {"Ngày": today + timedelta(days=3), "Môn học": "Toán rời rạc", "Phòng": "D202", "Giờ học": "07:00 - 09:00"},
    {"Ngày": today + timedelta(days=4), "Môn học": "Trí tuệ nhân tạo", "Phòng": "E301", "Giờ học": "15:30 - 17:00"},
])

# =================== THANH CHỨC NĂNG ===================
search = st.text_input("🔍 Tìm kiếm môn học hoặc phòng:", placeholder="Nhập tên môn hoặc phòng...")
filtered_df = df[df.apply(lambda row: search.lower() in str(row).lower(), axis=1)] if search else df

tab1, tab2, tab3 = st.tabs(["🗓️ Xem lịch", "📈 Thống kê học tập", "➕ Thêm buổi học"])

# =================== TAB 1: LỊCH HỌC ===================
with tab1:
    st.subheader("🗓️ Thời khóa biểu trong tuần")
    view = st.radio("Chế độ xem:", ["Danh sách", "Lịch (Calendar)"], horizontal=True)
    
    if view == "Danh sách":
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    else:
        # Vẽ lịch dạng calendar ảo bằng plotly
        cal_df = filtered_df.copy()
        cal_df["Ngày"] = pd.to_datetime(cal_df["Ngày"])
        cal_df["Day"] = cal_df["Ngày"].dt.strftime("%a %d/%m")
        fig = px.timeline(
            cal_df,
            x_start="Ngày",
            x_end="Ngày",
            y="Môn học",
            color="Phòng",
            title="Lịch học trong tuần (minimap)",
            height=350
        )
        fig.update_yaxes(categoryorder="total ascending")
        st.plotly_chart(fig, use_container_width=True)

# =================== TAB 2: THỐNG KÊ ===================
with tab2:
    st.subheader("📊 Thống kê học tập")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📘 Tổng môn học", df["Môn học"].nunique())
    col2.metric("🏫 Số phòng học", df["Phòng"].nunique())
    col3.metric("🧾 Tổng buổi học", len(df))
    col4.metric("🔥 Tỷ lệ chuyên cần", f"{np.random.randint(80,100)}%")

    st.markdown("---")
    st.markdown("### ⏱️ Số giờ học trong tuần")
    days = ["Th 2","Th 3","Th 4","Th 5","Th 6","Th 7","CN"]
    data = pd.DataFrame({
        "Ngày": days,"Giờ học": np.random.randint(1,5,len(days))
    })
    st.bar_chart(data, x="Ngày", y="Giờ học", height=300)

    st.markdown("### 💡 Gợi ý học tập thông minh")
    st.success("""
    - Học các môn khó (CSDL, AI) vào buổi sáng giúp tăng 20% hiệu quả ghi nhớ.  
    - Ôn lại bài cũ trước khi học môn mới để củng cố kiến thức.  
    - Nghỉ giải lao 10 phút sau mỗi 45 phút học giúp não hoạt động tốt hơn.  
    """)

# =================== TAB 3: THÊM BUỔI HỌC ===================
with tab3:
    st.subheader("➕ Thêm buổi học mới")
    st.markdown("<div class='add-box'>", unsafe_allow_html=True)
    with st.form("add_form"):
        col1, col2 = st.columns(2)
        with col1:
            ngay = st.date_input("📅 Ngày học", today)
            mon = st.text_input("📘 Môn học")
            phong = st.text_input("🏫 Phòng học")
        with col2:
            gio = st.text_input("⏰ Thời gian (VD: 07:30 - 09:30)")
            ghi_chu = st.text_area("📝 Ghi chú", "...")
        submitted = st.form_submit_button("💾 Lưu buổi học")
        if submitted:
            st.success(f"✅ Đã thêm buổi học '{mon}' vào ngày {ngay.strftime('%d/%m/%Y')}. (Demo)")
    st.markdown("</div>", unsafe_allow_html=True)


