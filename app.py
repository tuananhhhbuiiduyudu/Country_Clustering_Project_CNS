import streamlit as st
import pandas as pd
import os
import joblib
import plotly.express as px
from io import BytesIO

# === Cấu hình Streamlit ===
st.set_page_config(page_title="🌐 Phân Cụm Quốc Gia - Trí Tuệ Dữ Liệu", page_icon="🌍", layout="wide")

# === CSS tinh gọn, hiện đại ===
st.markdown("""
    <style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    h1, h2 {
        color: #c62828;
        font-weight: 700;
    }
    .section-box {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
    }
    .info-box {
        background: #fff3e0;
        padding: 0.9rem;
        border-left: 5px solid #ff9800;
        border-radius: 8px;
        margin-top: 0.7rem;
        font-weight: 500;
    }
    .stButton>button, .stDownloadButton>button {
        border-radius: 6px;
        background-color: #c62828;
        color: white;
        font-weight: 600;
        padding: 0.4rem 1rem;
        font-size: 0.9rem;
    }
    .stButton>button:hover, .stDownloadButton>button:hover {
        background-color: #b71c1c;
    }
    </style>
""", unsafe_allow_html=True)

# === Header đẹp ===
st.markdown("""
<div class="section-box">
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div>
            <h2>🌐 PHÂN CỤM QUỐC GIA BẰNG Artificial Intelligence</h2>
            <p style="margin: 0;">Khám phá mức độ phát triển và nhu cầu hỗ trợ của các quốc gia thông qua học máy không giám sát.</p>
        </div>
        <img src="https://cdn-icons-png.flaticon.com/512/1533/1533916.png" width="60">
    </div>
    <div class="info-box">
        🇻🇳 Một sản phẩm cá nhân ứng tuyển Phòng Công nghệ Số - Made by Bùi Duy Tuấn Anh
    </div>
</div>
""", unsafe_allow_html=True)

# === Load model đã huấn luyện ===
model_path = os.path.join("model", "model.pkl")
try:
    model = joblib.load(model_path)
    st.success("✅ Mô hình đã sẵn sàng để sử dụng.")
except:
    st.error("❌ Không tìm thấy mô hình tại `model/model.pkl`. Hãy kiểm tra lại.")
    st.stop()

# === Upload dữ liệu ===
uploaded_file = st.file_uploader("📂 **BƯỚC 1:** Tải lên file CSV chứa dữ liệu quốc gia", type=["csv"])

# === Các cột cần thiết ===
required_cols = ['country', 'child_mort', 'exports', 'health', 'imports',
                 'income', 'inflation', 'life_expec', 'total_fer', 'gdpp']

# === Xử lý khi có file ===
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        missing = [col for col in required_cols if col not in df.columns]
        if missing:
            st.error(f"⚠️ Thiếu cột cần thiết: {missing}")
            st.stop()

        preds = model.predict(df)
        label_map = {
            0: ("🟡 Có thể cần hỗ trợ", "orange"),
            1: ("🟢 Không cần hỗ trợ", "green"),
            2: ("🔴 Cần hỗ trợ", "red")
        }
        df["Phân loại"] = [label_map[p][0] for p in preds]
        df["Màu"] = [label_map[p][1] for p in preds]

        # === Hiển thị kết quả ===
        with st.container():
            st.markdown("### 🧠 BƯỚC 2: Kết quả phân loại theo cụm quốc gia")
            st.dataframe(df[["country", "Phân loại"]], use_container_width=True)

            st.markdown("### 📊 Thống kê theo nhóm")
            counts = df["Phân loại"].value_counts().rename_axis("Nhóm").reset_index(name="Số lượng")
            st.dataframe(counts, use_container_width=True)

            st.markdown("### 🗺️ Bản đồ phân bố theo cụm")
            fig = px.choropleth(
                df,
                locations="country",
                locationmode="country names",
                color="Phân loại",
                color_discrete_map={
                    "🔴 Cần hỗ trợ": "red",
                    "🟡 Có thể cần hỗ trợ": "orange",
                    "🟢 Không cần hỗ trợ": "green"
                },
                title="Phân bố quốc gia theo mức độ cần hỗ trợ"
            )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("### 💾 BƯỚC 3: Tải kết quả về máy")
            buffer = BytesIO()
            df.to_csv(buffer, index=False)
            st.download_button(
                label="📥 Tải kết quả (.csv)",
                data=buffer.getvalue(),
                file_name="ket_qua_phan_cum.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"❌ Lỗi khi xử lý file: {e}")
else:
    st.info("📌 Vui lòng tải lên file CSV chứa dữ liệu quốc gia để tiếp tục.")
