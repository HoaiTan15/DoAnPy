# Quản Lý Bán Hàng Python

## Mô tả
Phần mềm quản lý bán hàng đơn giản với giao diện Tkinter, cho phép:
- Đăng nhập, đăng ký tài khoản (user, admin)
- Quản lý sản phẩm (thêm, xóa, sửa, lấy API)
- Mua hàng, giỏ hàng, thanh toán
- Lưu dữ liệu vào file JSON

## Tính năng chính
- **Tài khoản admin duy nhất:**  
  - Tài khoản: `admin`  
  - Mật khẩu: `admin`
- **Đăng ký tài khoản user**
- **Quản lý sản phẩm:** Thêm, xóa, sửa, lấy dữ liệu từ API Tiki
- **Mua hàng:** Thêm vào giỏ, xem giỏ, thanh toán

## Hướng dẫn sử dụng

### 1. Cài đặt thư viện cần thiết
```bash
pip install requests
```

### 2. Chạy chương trình
```bash
python main.py
```

### 3. Đăng nhập
- **Admin:**  
  - Tài khoản: `admin`  
  - Mật khẩu: `admin`
- **User:**  
  - Đăng ký tài khoản mới

### 4. Cấu trúc thư mục
```
DoAnPy/
├── main.py
├── LoginGUI.py
├── UserGUI.py
├── AdminGUI.py
├── ClassUser.py
├── ClassUserManager.py
├── ClassProduct.py
├── ClassFile.py
├── crawl_tiki.py
├── users.json
├── products.json
└── ...
```

### 5. Một số lưu ý
- Khi đăng ký, file `users.json` sẽ tự tạo nếu chưa có.
- Tài khoản `admin` là duy nhất, không thể đăng ký thêm.
- Dữ liệu sản phẩm lưu ở `products.json`.
