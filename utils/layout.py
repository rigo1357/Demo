import streamlit as st
from datetime import datetime

def apply_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .header {
        background: linear-gradient(90deg, #004aad, #007bff);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        font-size: 0.85rem;
        color: #777;
        margin-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

def base_layout(title, render_func):
    apply_style()
    st.sidebar.image("assets/logo.png", width=100)
    st.sidebar.title("🎓 Cổng Sinh viên TDMU")
    menu = st.sidebar.radio("Chọn trang:", [
        "🏠 Trang chủ",
        "📅 Lịch học",
        "🧠 Sắp xếp lịch học",
        "💬 Chatbot tư vấn",
        "👤 Hồ sơ cá nhân",
        "🚪 Đăng xuất"
    ])
    st.markdown(f"<div class='header'>{title}</div>", unsafe_allow_html=True)
    render_func(menu)
    st.markdown(f"<div class='footer'>© {datetime.now().year} Trường Đại học Thủ Dầu Một</div>", unsafe_allow_html=True)
