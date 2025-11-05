# pages/1_Home.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# -------------------------
# Page config & simple auth
# -------------------------
st.set_page_config(
    page_title="🏠 Trang chủ - Cổng thông tin sinh viên",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ Vui lòng đăng nhập để truy cập trang này!")
    st.stop()

username = st.session_state.get("username", "Sinh viên")

# -------------------------
# CSS: modern light theme
# -------------------------
st.markdown(
    """
    <style>
    :root{
      --primary:#004aad;
      --secondary:#007bff;
      --muted:#6c757d;
      --card-shadow: 0 6px 18px rgba(24,39,75,0.08);
    }
    .page-header{
      background: linear-gradient(90deg, var(--primary), var(--secondary));
      color: white;
      padding: 28px;
      border-radius: 12px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.08);
      margin-bottom: 20px;
    }
    .page-header h1{ margin:0; font-size:28px; font-weight:700;}
    .page-header p{ margin:4px 0 0 0; opacity:0.95; }
    .card { background:white; padding:18px; border-radius:10px; box-shadow: var(--card-shadow); }
    .metric-card { text-align:center; padding:18px; border-radius:10px; background:white; box-shadow: var(--card-shadow); }
    .metric-card .value { font-size:22px; font-weight:700; color:var(--primary); }
    .metric-card .label { color:var(--muted); margin-top:6px; }
    .news-card { background:white; border-left:4px solid var(--secondary); padding:14px; border-radius:8px; box-shadow: var(--card-shadow); margin-bottom:12px;}
    .tips { background:linear-gradient(90deg,#e9f4ff,#f6fbff); padding:16px; border-radius:10px; border-left:4px solid var(--secondary); box-shadow: var(--card-shadow); }
    .small { color:var(--muted); font-size:13px; }
    /* make Plotly text darker for light theme */
    .plotly-graph-div .gtitle { color:#102a43; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Sample data (replace with real later)
# -------------------------
today = datetime.now().date()
weeks = [f"Tuần {i}" for i in range(1, 9)]
progress = np.clip(np.random.randint(55, 100, size=8), 0, 100)

days = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật"]
hours = np.random.randint(1, 5, size=len(days))

news_data = [
    {"title": "Đăng ký học phần HKII 2025–2026", "snippet": "Thời gian: 10/11 - 25/11/2025. Đăng ký tại cổng sinh viên.", "date": "05/11/2025"},
    {"title": "Lễ tốt nghiệp 12/2025", "snippet": "Sinh viên đủ điều kiện sẽ nhận email thông báo lịch.", "date": "03/11/2025"},
    {"title": "Hội thảo AI trong giáo dục", "snippet": "08:00 20/10/2025 - Phòng A203. Đăng ký tham dự.", "date": "25/10/2025"},
]

# -------------------------
# HEADER / BANNER
# -------------------------
st.markdown(
    f"""
    <div class="page-header">
        <div style="display:flex; align-items:center; gap:16px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/3/37/Logo_TDMU.png" width="64" style="border-radius:8px; background:white; padding:6px;" />
            <div>
                <h1>🎓 Cổng thông tin sinh viên - TDMU</h1>
                <p>Xin chào <strong>{username}</strong> — hệ thống quản lý & trợ giúp học tập thông minh.</p>
            </div>
            <div style="margin-left:auto; text-align:right;">
                <div class="small">Phiên bản demo • Cập nhật: {datetime.now().strftime('%d/%m/%Y')}</div>
                <div style="margin-top:8px; font-weight:600; color:#fff;">Xin chúc 1 học kỳ hiệu quả!</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# TOP METRICS
# -------------------------
col1, col2, col3, col4 = st.columns([1,1,1,1], gap="large")
with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown('<div class="small">📘 Tổng số môn học</div>', unsafe_allow_html=True)
    st.markdown('<div class="value">5</div>', unsafe_allow_html=True)
    st.markdown('<div class="label small">+1 so với tháng trước</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown('<div class="small">📅 Buổi học sắp tới</div>', unsafe_allow_html=True)
    st.markdown('<div class="value">2</div>', unsafe_allow_html=True)
    st.markdown('<div class="label small">-1 so với tuần trước</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown('<div class="small">⏱️ Thời gian học trung bình</div>', unsafe_allow_html=True)
    st.markdown('<div class="value">2h 15p</div>', unsafe_allow_html=True)
    st.markdown('<div class="label small">+10% so với tuần trước</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown('<div class="small">🔥 Hiệu suất học tập</div>', unsafe_allow_html=True)
    st.markdown('<div class="value">85%</div>', unsafe_allow_html=True)
    st.markdown('<div class="label small">+5% so với tháng trước</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# -------------------------
# MAIN LAYOUT: left content + right column
# -------------------------
left_col, right_col = st.columns([3,1], gap="large")

# LEFT: charts and news
with left_col:
    # Progress chart (plotly)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#004aad; margin-bottom:8px;">📈 Tiến độ học tập 8 tuần</h3>', unsafe_allow_html=True)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=weeks,
        y=progress,
        mode='lines+markers',
        line=dict(color="#007bff", width=3),
        marker=dict(size=8, color="#007bff")
    ))
    fig.update_layout(
        xaxis=dict(title="Tuần"),
        yaxis=dict(title="Hoàn thành (%)", range=[0,100]),
        margin=dict(t=10, b=30, l=30, r=10),
        template="none",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig, use_container_width=True, height=320)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="height:18px;"></div>', unsafe_allow_html=True)

    # Bar chart for hours per day
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#004aad; margin-bottom:8px;">📚 Thời gian học trong tuần</h3>', unsafe_allow_html=True)
    df_hours = pd.DataFrame({"Ngày": days, "Giờ học": hours})
    fig2 = px.bar(df_hours, x="Ngày", y="Giờ học", text="Giờ học", color="Giờ học",
                  color_continuous_scale=["#cfe9ff", "#007bff"])
    fig2.update_traces(textposition='outside', marker_line_color='rgba(255,255,255,0.6)', marker_line_width=1)
    fig2.update_layout(margin=dict(t=10,b=30,l=30,r=10), showlegend=False, coloraxis_showscale=False, plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig2, use_container_width=True, height=320)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="height:20px;"></div>', unsafe_allow_html=True)

    # News / Announcements grid
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#004aad; margin-bottom:12px;">📰 Thông báo & Tin tức</h3>', unsafe_allow_html=True)
    news_cols = st.columns(2)
    for i, n in enumerate(news_data):
        col = news_cols[i % 2]
        with col:
            st.markdown(
                f"""
                <div class="news-card">
                    <h4 style="margin:0 0 8px 0;">📢 {n['title']}</h4>
                    <div class="small">{n['snippet']}</div>
                    <div style="margin-top:8px; color:#6c757d; font-size:13px;">📅 {n['date']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown('</div>', unsafe_allow_html=True)

# RIGHT: profile card, quick actions, tips
with right_col:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#004aad; margin-bottom:8px;">👤 Hồ sơ nhanh</h3>', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/1946/1946429.png", width=86)
    st.markdown(f"**{username}**")
    st.markdown("MSSV: **2025XXXXX**")
    st.markdown("Lớp: **CN-05-2025**")
    st.markdown("Ngành: **Công nghệ Thông tin**")
    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
    if st.button("✏️ Chỉnh sửa hồ sơ"):
        st.info("Chức năng chỉnh sửa hồ sơ sẽ có trong bản tiếp theo.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="height:14px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="tips">', unsafe_allow_html=True)
    st.markdown('<h4 style="margin-top:0; color:#004aad;">💡 Mẹo nhanh</h4>', unsafe_allow_html=True)
    st.markdown("<ul style='margin:0 0 0 18px; color:#274c77;'><li>Học 45 phút — nghỉ 10 phút</li><li>Ôn lại bài cũ trước khi học bài mới</li><li>Học môn khó vào buổi sáng</li></ul>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="height:14px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h4 style="color:#004aad; margin-bottom:8px;">📥 Tải báo cáo nhanh</h4>', unsafe_allow_html=True)
    # Example: generate CSV from sample stats
    @st.cache_data
    def make_report():
        df = pd.DataFrame({
            "Metric": ["Tổng môn học", "Buổi học sắp tới", "Thời gian trung bình", "Hiệu suất"],
            "Value": ["5", "2", "2h 15p", "85%"]
        })
        return df
    report = make_report()
    csv = report.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Tải file CSV", csv, file_name="report_summary.csv", mime="text/csv")
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# Footer
# -------------------------
st.markdown("---")
st.markdown(
    f"""
    <div style="text-align:center; color:#6c757d; font-size:13px; padding:6px 0 30px 0;">
        © {datetime.now().year} Trường Đại học Thủ Dầu Một — Cổng thông tin sinh viên. • Phiên bản demo
    </div>
    """,
    unsafe_allow_html=True,
)
