# 📘 Dataset Documentation: UCI Credit Card Default

File này cung cấp chi tiết về ý nghĩa các trường dữ liệu (Features) trong bộ dữ liệu dự đoán nợ xấu thẻ tín dụng.

## 1. Thông tin tổng quan
* **Tên file:** `UCI_Credit_Card.csv`
* **Số lượng bản ghi:** 30,000 khách hàng.
* **Mục tiêu:** Dự đoán khả năng khách hàng không thể trả nợ (`default.payment.next.month`) dựa trên dữ liệu lịch sử.



## 2. Từ điển dữ liệu (Data Dictionary)

### A. Nhóm thông tin cá nhân (Demographic)
| Tên cột | Ý nghĩa | Chú thích mã hóa |
| :--- | :--- | :--- |
| **ID** | Mã định danh | Không có giá trị trong mô hình dự báo. |
| **LIMIT_BAL** | Hạn mức tín dụng | Số tiền tối đa (Tân Đài Tệ - NT dollar) khách hàng được tiêu. |
| **SEX** | Giới tính | 1 = Nam (Male); 2 = Nữ (Female). |
| **EDUCATION** | Trình độ học vấn | 1 = Sau đại học; 2 = Đại học; 3 = Phổ thông; 4 = Khác; 5,6 = Không xác định. |
| **MARRIAGE** | Tình trạng hôn nhân | 1 = Đã kết hôn; 2 = Độc thân; 3 = Khác. |
| **AGE** | Độ tuổi | Tính theo năm. |

### B. Nhóm lịch sử thanh toán (Payment History)
**Cột `PAY_0` đến `PAY_6`**: Trạng thái trả nợ của các tháng trước (từ tháng 9 đến tháng 4).
* *Lưu ý:* `PAY_0` là tháng gần nhất (Tháng 9), `PAY_2` là tháng 8... `PAY_6` là tháng 4.

**Ý nghĩa các con số trong cột PAY:**
- **-1**: Thanh toán đúng hạn (Pay duly).
- **1**: Trễ hạn 1 tháng (Payment delay for one month).
- **2**: Trễ hạn 2 tháng.
- ...(Tương tự cho đến 8, 9 tháng).
- **0, -2**: Các trạng thái khác (thường được hiểu là không có dư nợ hoặc thanh toán tối thiểu).



### C. Nhóm số dư hóa đơn (Bill Amount)
**Cột `BILL_AMT1` đến `BILL_AMT6`**: Số tiền ghi trên hóa đơn hàng tháng.
- `BILL_AMT1`: Hóa đơn tháng 9.
- `BILL_AMT6`: Hóa đơn tháng 4.

### D. Nhóm số tiền đã trả (Previous Payment)
**Cột `PAY_AMT1` đến `PAY_AMT6`**: Số tiền thực tế khách hàng đã trả trong tháng đó.
- `PAY_AMT1`: Số tiền trả trong tháng 9.
- `PAY_AMT6`: Số tiền trả trong tháng 4.

### E. Biến mục tiêu (Target Variable)
**Cột `default.payment.next.month`**:
- **1**: **Có nợ xấu** (Khách hàng sẽ không trả được nợ vào tháng tới).
- **0**: **Không nợ xấu** (Thanh toán bình thường).

*Tài liệu này được soạn thảo để phục vụ dự án Credit Risk Analysis.*