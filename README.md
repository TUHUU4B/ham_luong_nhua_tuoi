# Hàm lượng nhựa tưới – TCVN 8863:2011

Ứng dụng Streamlit giúp kỹ sư hiện trường xác định lưu lượng tưới nhựa nóng bằng khay cân theo tiêu chuẩn **TCVN 8863:2011 – Mặt đường láng nhựa nóng**. Ứng dụng cho phép:

- Nhập khối lượng khay rỗng và khay + nhựa, tự động suy ra khối lượng nhựa thực tế.
- Tính diện tích khay hình chữ nhật từ chiều dài và chiều rộng để tránh sai số đo đạc.
- Quy đổi hàm lượng nhựa từ g/cm² sang kg/m², hiển thị tức thì.
- So sánh với giới hạn tối thiểu của thiết kế/tiêu chuẩn và đưa ra thông báo “đạt” hoặc “thiếu”.
- Hiển thị hướng dẫn nhanh ngay trên sidebar để thao tác thống nhất ngoài hiện trường.

## Yêu cầu hệ thống

- Python 3.10+
- Các thư viện trong `requirements.txt`

## Cài đặt

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Chạy ứng dụng

```bash
streamlit run app.py
```

Ứng dụng sẽ mở trên trình duyệt tại địa chỉ `http://localhost:8501`.

## Các hàm tính toán chính

- `format_number()`: chuẩn hóa cách hiển thị số theo định dạng Việt Nam.
- `compute_binder_rate()`: nhận khối lượng nhựa (g) và diện tích khay (cm²) rồi trả về hàm lượng tương ứng (g/cm² và kg/m²).
- `compute_tray_area()`: tính diện tích khay hình chữ nhật dựa trên chiều dài/rộng.
- `evaluate_spec()`: đối chiếu kết quả với giới hạn tối thiểu của TCVN 8863:2011 và trả về thông báo trạng thái.

## Tùy biến

- Thay logo bằng cách cập nhật `logo.png` trong thư mục gốc.
- Điều chỉnh nội dung, ngôn ngữ hiển thị trong `app.py` tùy nhu cầu dự án.

## Góp ý

Liên hệ: **MR Tuấn – 0946 135 156** (Công ty Tứ Hữu).

