# 🌍 Country Clustering Project CNS - Dự án ứng tuyển phòng CNS
## 🌐 Sản phẩm Demo
Bạn có thể test mô hình phân cụm Country trực tiếp tại (chạy data để quyết định chi tiêu ngân sách hợp nhất với tập data hiện có):

🔗 [**Streamlit App — Country Clustering**](https://countryclusteringprojectcns-jnt7sslytihlcjmk85nf6r.streamlit.app/)


## 📥 Dữ liệu mẫu

Bạn tải tập dữ liệu để chạy mô hình và đưa ra quyết định:

📥 [Tải dữ liệu Country-data.csv](https://github.com/tuananhhhbuiiduyudu/Country_Clustering_Project_CNS/raw/main/data/Country-data.csv)
> 👉 Nhấn chuột phải vào link > “Save link as...” để tải về


Dự án ứng dụng học máy không giám sát để phân nhóm các quốc gia dựa trên các đặc trưng kinh tế - xã hội. Mục tiêu là phát hiện những nhóm quốc gia tương đồng, hỗ trợ phân tích, trực quan hóa dữ liệu và ra quyết định chính sách.

---

## 📌 Mô tả dự án

Dự án sử dụng các thuật toán phân cụm như **K-Means**, **Hierarchical Clustering**,  kết hợp với kỹ thuật tiền xử lý và giảm chiều PCA để:

- Phân loại các quốc gia thành các nhóm tương đồng.
- Trực quan hóa mối quan hệ giữa các quốc gia.
- Tạo ra một công cụ tương tác hiển thị kết quả phân cụm.

---

## 📁 Cấu trúc thư mục

```
Country_Clustering_Project_CNS/
├── app.py                      # Ứng dụng web với Streamlit(chạy mô hình tốt nhất)
├── data/
│   └── Country-data.csv        # Dữ liệu gốc về các quốc gia
├── model/
│   └── model.pkl               # Mô hình clustering đã lưu
├── notebooks/
│   ├── EDA_and_TrainModel.ipynb     # Phân tích và huấn luyện mô hình
│   └── feature_explanation.py       # Giải thích đặc trưng
├── src/                        
│   ├── __init__.py
│   ├── clustering.py           # Thuật toán phân cụm
│   ├── config.py               # Cấu hình tham số
│   ├── data_loader.py          # Đọc dữ liệu
│   ├── data_preprocessing.py   # Tiền xử lý dữ liệu
│   ├── evaluation.py           # Đánh giá mô hình
│   └── visualization.py        # Trực quan hóa kết quả
├── .env
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt            # Danh sách thư viện cần thiết
```

---

## 🛠️ Cài đặt

```bash
# Bước 1: Clone dự án
git clone https://github.com/tuananhhhbuiiduyudu/Country_Clustering_Project_CNS.git
cd Country_Clustering_Project_CNS

# Bước 2: Tạo môi trường ảo và cài thư viện
python -m venv venv
venv\Scripts\activate  # Hoặc source venv/bin/activate trên macOS/Linux
pip install -r requirements.txt
```

---

## 🚀 Sử dụng

### 🔬 Phân tích và huấn luyện mô hình

Mở và chạy notebook:
```bash
notebooks/EDA_and_TrainModel.ipynb
```

### 🌐 Chạy ứng dụng web (Streamlit)

```bash
streamlit run app.py
```

Truy cập trình duyệt tại: `http://localhost:8501`

---

## 📊 Kết quả

- ✅ **Clusters**: Tệp kết quả lưu trong `model/model.pkl`
- 📈 **Biểu đồ**: Được hiển thị thông qua Streamlit hoặc notebook
- 🧠 **Đánh giá**: Silhouette Score, Elbow Method

---

## 🔧 Kỹ thuật sử dụng

- **Tiền xử lý**: StandardScaler, xử lý null, encode
- **Giảm chiều**: PCA
- **Clustering**: KMeans, DBSCAN, Agglomerative
- **Trực quan**: seaborn, matplotlib, plotly
- **App**: Streamlit

---

## 📄 License

Dự án phát hành dưới giấy phép **Apache License 2.0**. Chi tiết xem trong file `LICENSE`.

---

## 👨‍💻 Tác giả

**Bùi Duy Tuấn Anh**  
[GitHub Profile](https://github.com/tuananhhhbuiiduyudu)
