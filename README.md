# World_wide

# My Flask Project

## 1. Giới thiệu

Đây là Flask project backend được xây dựng với Flask, cung cấp các API cho việc đăng nhập / đăng ký người dùng, tra thông tin tọa độ, thêm/sửa/xóa tọa độ cho ứng dụng World_Wide về chuyến đi

## 2. Cài Đặt

Để chạy được project này trên máy của bạn, làm theo các bước dưới đây:

### Yêu Cầu

- **Python** phiên bản >= 3.8
- **Virtual Environment** (khuyến nghị)

### Các Bước Cài Đặt

1. Clone repository này:

```bash
git clone https://github.com/ZanhNe/World_wide.git
cd world_wide

```

2. Tạo virtual enviroment

```bash
python3 -m venv venv
source venv/bin/activate  # Kích hoạt venv trên macOS và Linux
venv\Scripts\activate     # Kích hoạt venv trên Windows
```

3. Cài đặt các gói cần thiết từ requirements.txt:

```bash
pip install -r requirements.txt
```

4. Tạo file .env và thêm các biến môi trường cần thiết, VD:

```bash
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///site.db
```

5. Khởi chạy ứng dụng:

```bash
flask run
```
