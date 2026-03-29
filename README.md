# 🏦 Dự Báo Mặc Định Thẻ Tín Dụng (UCI Credit Card Default Prediction)

## 📋 Tổng Quan Dự Án

Đây là một project **Phân Tích Rủi Ro Tín Dụng** sử dụng Machine Learning để dự báo khả năng mặc định (không trả nợ) của khách hàng thẻ tín dụng. 

**Mục tiêu chính:**
- Xây dựng mô hình ML dự báo khách hàng sẽ mặc định lần trả nợ tiếp theo
- Phân tích đặc điểm nhân khẩu học, lịch sử thanh toán, và mô hình chi tiêu
- So sánh hiệu suất của nhiều mô hình (Logistic Regression, Random Forest, XGBoost)

**Biến mục tiêu:** `IS_DEFAULT` 
- 0: Không mặc định (Good Customer)
- 1: Mặc định (Default Customer)

**Dataset:** UCI Credit Card Dataset - 30,000 khách hàng, 50 features

---

## 🎯 Các Tính Năng Chính

✅ **Xử Lý Dữ Liệu (ETL):**
- Làm sạch dữ liệu, kiểm tra giá trị thiếu
- Chuẩn hóa dữ liệu theo tỷ lệ
- Xử lý các biến categorical

✅ **Phân Tích Khám Phá (EDA):**
- Phân tích nhân khẩu học (giới tính, tuổi, học vấn, tình trạng hôn nhân)
- Phân tích phân phối dữ liệu (KDE plots, box plots)
- Phân tích tương quan giữa các biến

✅ **Phân Tích Tài Chính:**
- Tỷ lệ sử dụng hạn mức, mô hình thanh toán
- Xu hướng hóa đơn theo từng tháng
- Tương quan với mặc định

✅ **Kỹ Thuật Đặc Trưng (Feature Engineering):**
- Chỉ báo thanh toán trễ hạn
- Tỷ lệ sử dụng (Bill/Limit)
- Tỷ lệ thanh toán

✅ **Mô Hình Machine Learning:**
- Logistic Regression (Baseline)
- Random Forest (Ensemble)
- XGBoost (Optimized with GridSearchCV)

✅ **Đánh Giá Mô Hình:**
- Confusion Matrix, Classification Report
- ROC-AUC Score, Precision-Recall Curves
- So sánh hiệu suất giữa các mô Hình

---

## 📁 Cấu Trúc Dự Án

```
Finance/
├── JupyterNotebook/                    # Các notebook phân tích chính
│   ├── 1_DataCleaning.ipynb           # Làm sạch & chuẩn hóa dữ liệu
│   ├── 2_demograhics.ipynb            # Phân tích nhân khẩu học
│   ├── 3_Distribution.ipynb           # Phân tích phân phối & tương quan
│   ├── 4_Analyst.ipynb                # Phân tích chỉ số tài chính
│   └── 5_ModelTraining.ipynb          # Huấn luyện & đánh giá mô hình
│
├── data/                               # Thư mục dữ liệu
│   ├── raw/
│   │   └── UCI_Credit_Card.csv        # Dataset gốc (30,000 records)
│   ├── processed/
│   │   ├── UCI_Credit_Card_Cleaned.csv    # CSV đã làm sạch
│   │   ├── UCI_Credit_Card_Cleaned.parquet # Parquet đã làm sạch
│   │   └── UCI_Credit_Card.parquet         # Parquet gốc
│   └── DatasetExplain.md               # Từ điển dữ liệu (Vietnamese)
│
├── src/                                # Mã nguồn hỗ trợ
│   ├── helper_function.py             # Các hàm vẽ biểu đồ (Seaborn/Matplotlib)
│   └── __pycache__/                   # Python cache (git-ignored)
│
├── models/                             # Thư mục mô hình
│   └── credit_default_model.pkl       # Mô hình XGBoost được huấn luyện
│
├── Visualization/                      # Kết quả trực quan hóa (Generated)
│   ├── Proportion/                     # 6 biểu đồ tỷ lệ nhân khẩu học
│   ├── Distribution/                   # 3 biểu đồ phân tích phân phối
│   └── Analyst/                        # Biểu đồ từ phân tích
│   
│   ⚠️ **Note:** Folder này được generate tự động khi chạy notebooks
│              Không được track trong Git (.gitignore)
│
├── requirements.txt                    # Python dependencies
├── .vscode/settings.json              # Cấu hình VS Code
├── 4Test.ipynb                        # Notebook kiểm thử
└── README.md                          # Tệp này

```

---

## 🚀 Hướng Dẫn Nhanh

### 1. Cài Đặt Môi Trường

```bash
# Tạo conda environment (tùy chọn)
conda create -n finance python=3.10
conda activate finance

# Cài đặt dependencies
pip install -r requirements.txt
```

### 2. Chạy Pipeline Để Generate Visualizations và Mô Hình

**⚠️ Important:** Folder `Visualization/` được **generate tự động** khi chạy các notebooks. Nó không được commit lên Git. Để lấy được các figures, bạn cần chạy các notebooks theo thứ tự dưới đây:

```bash
# 1. Làm sạch dữ liệu & tạo dữ liệu xử lý
jupyter notebook JupyterNotebook/1_DataCleaning.ipynb

# 2. Phân tích nhân khẩu học → Tạo 6 biểu đồ
jupyter notebook JupyterNotebook/2_demograhics.ipynb
# Output: Visualization/Proportion/*.png

# 3. Phân tích phân phối → Tạo 3 biểu đồ
jupyter notebook JupyterNotebook/3_Distribution.ipynb
# Output: Visualization/Distribution/*.png

# 4. Phân tích tài chính → Tạo visualizations (nếu có)
jupyter notebook JupyterNotebook/4_Analyst.ipynb
# Output: Visualization/Analyst/*.png

# 5. Huấn luyện mô hình → Tạo ROC curves & so sánh mô hình
jupyter notebook JupyterNotebook/5_ModelTraining.ipynb
# Output: Trained model + comparison plots
```

### 3. Kết Quả Sau Khi Chạy

**Generated Outputs:**
- 📊 **Visualizations** → `Visualization/` (Generated locally, không tracked in Git)
  - `Proportion/`: 6 biểu đồ phân tích nhân khẩu học
  - `Distribution/`: 3 biểu đồ phân tích phân phối
  - `Analyst/`: Biểu đồ phân tích tài chính

- 🤖 **Trained Model** → `models/credit_default_model.pkl`
- 📁 **Processed Data** → `data/processed/`

---

## 📊 Công Nghệ & Thư Viện

| Danh Mục | Thư Viện |
|----------|----------|
| **Xử lý Dữ Liệu** | pandas==2.3.3, numpy==2.2.6, pyarrow==23.0.1 |
| **Machine Learning** | scikit-learn==1.7.2, xgboost, joblib==1.5.3 |
| **Trực quan Hóa** | matplotlib==3.10.8, seaborn==0.13.2, pillow==12.1.1 |
| **Jupyter** | jupyter_client==8.8.0, ipykernel==7.2.0, ipython==8.38.0 |
| **Thống Kê** | scipy==1.15.3 |

---

## 📚 Từ Điển Dữ Liệu

Xem chi tiết tại: [data/DatasetExplain.md](data/DatasetExplain.md)

### Các Biến Chính:

**Nhân Khẩu Học (6 cột):**
- `ID`: Mã khách hàng
- `LIMIT_BAL`: Hạn mức tín dụng (NT Đô la)
- `SEX`: Giới tính (1=Nam, 2=Nữ)
- `EDUCATION`: Học vấn (1=Tốt nghiệp, 2=Đại học, 3=Trung học, 4=Khác)
- `MARRIAGE`: Tình trạng hôn nhân (1=Đã kết hôn, 2=Độc thân, 3=Khác)
- `AGE`: Tuổi (năm)

**Lịch Sử Thanh Toán (6 cột):**
- `PAY_1 to PAY_6`: Trạng thái thanh toán 6 tháng trước
  - -1: Thanh toán đúng hạn
  - 0/-2: Không có tiêu thụ
  - 1-9: Số tháng trễ hạn

**Số Tiền Hóa Đơn (6 cột):**
- `BILL_AMT1 to BILL_AMT6`: Số tiền hóa đơn 6 tháng trước

**Số Tiền Thanh Toán (6 cột):**
- `PAY_AMT1 to PAY_AMT6`: Số tiền thanh toán 6 tháng trước

**Mục Tiêu:**
- `IS_DEFAULT`: Mặc định (0=Không, 1=Có)

---

## 🔍 Quy Trình Phân Tích

### 1️⃣ DataCleaning (1_DataCleaning.ipynb)
- Kiểm tra giá trị NaN, trùng lặp
- Chuẩn hóa các biến categorical
- Xuất CSV/Parquet đã xử lý

### 2️⃣ Demographics (2_demograhics.ipynb)
- Phân tích tỷ lệ mặc định theo giới tính
- Phân tích theo học vấn, tình trạng hôn nhân
- Phân tích theo độ tuổi, hạn mức tín dụng
- Biểu đồ tỷ lệ cao độ phân chia

### 3️⃣ Distribution (3_Distribution.ipynb)
- KDE plots (Kernel Density Estimation)
- Box plots phân tích phân phối
- Heatmap tương quan Pearson
- Phân tích thống kê cơ bản

### 4️⃣ Analyst (4_Analyst.ipynb)
- Phân tích tỷ lệ sử dụng (Bill/Limit)
- Mô hình thanh toán và chi tiêu
- Xu hướng hóa đơn theo thời gian
- Tương quan với mặc định

### 5️⃣ ModelTraining (5_ModelTraining.ipynb)
- **Kỹ thuật đặc trưng:** Late payment indicators, utilization rates
- **Mô hình 1:** Logistic Regression
- **Mô hình 2:** Random Forest
- **Mô hình 3:** XGBoost (GridSearchCV)
- **Đánh giá:** ROC curves, Confusion Matrix, Classification Report
- **Output:** Mô hình tốt nhất lưu dưới dạng pickle

---

## 📈 Kết Quả Mô Hình

Sau khi chạy `5_ModelTraining.ipynb`:
- **XGBoost** được lựa chọn là mô hình tốt nhất
- Lưu tại: `models/credit_default_model.pkl`
- Hiệu suất được so sánh với các mô hình khác

---

## 🛠️ Các Hàm Hỗ Trợ

**File:** `src/helper_function.py`

```python
plot_kde(data, col, hue, title)          # Vẽ KDE plot
plot_hist(data, col, hue, title)         # Vẽ histogram
plot_count(data, col, hue, title)        # Vẽ count plot
plot_box(data, col, hue, title)          # Vẽ box plot
_save_figure_(plt, name)                 # Lưu figure (300 DPI PNG)
_set_name_(col, type)                    # Đặt tên chuẩn cho biểu đồ
```

---

## 📦 Yêu Cầu Hệ Thống

- Python >= 3.8
- Jupyter Notebook hoặc JupyterLab
- RAM >= 4GB (để xử lý 30K records)
- Không yêu cầu GPU

---

## 🔄 Quy Trình Làm Việc (Workflow)

```
Raw Data (data/raw/)
    ↓
1_DataCleaning
    ↓
Processed Data (data/processed/)
    ↓
2_Demographics + 3_Distribution + 4_Analyst (EDA)
    ↓
Visualizations (Visualization/)
    ↓
5_ModelTraining
    ↓
Trained Model (models/)
```

---

## 📝 Ghi Chú

- Tất cả các biểu đồ được lưu ở độ phân giải cao (300 DPI)
- Thứ tự thực hiện notebook là **rất quan trọng**
- Dữ liệu đã xử lý được sử dụng bởi các notebook phía sau
- Mô hình được huấn luyện trên toàn bộ tập dữ liệu

---

## 👤 Tác Giả

Created by: Tr Bình Minh

---

## 📄 License

This project is for educational and research purposes.

---

**Last Updated:** March 2026
