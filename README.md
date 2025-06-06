# Quản Lý Bán Hàng Python

## Mô tả
Phần mềm quản lý bán hàng đơn giản với giao diện Tkinter, cho phép:
- Đăng nhập, đăng ký tài khoản (user, admin)
- Quản lý sản phẩm (thêm, xóa, sửa, lấy API từ Tiki)
- Mua hàng, giỏ hàng, thanh toán
- Lưu dữ liệu vào file JSON

## Tính năng chính
- **Tài khoản admin duy nhất:**  
  - Tài khoản: `admin`  
  - Mật khẩu: `admin`
- **Đăng ký tài khoản user**
- **Quản lý sản phẩm:** Thêm, xóa, sửa, lấy dữ liệu từ API Tiki
- **Mua hàng:** Thêm vào giỏ, xem giỏ, thanh toán

## Hướng dẫn tải và sử dụng

### 1. Tải mã nguồn từ GitHub
- Truy cập [https://github.com/tanph/DoAnPy](https://github.com/tanph/DoAnPy) (hoặc repo của bạn).
- Nhấn nút **Code** > **Download ZIP** để tải về máy.
- Giải nén file ZIP ra một thư mục.

### 2. Cài đặt thư viện cần thiết
Mở terminal/cmd tại thư mục chứa mã nguồn và chạy:
```bash
pip install requests
```

### 3. Chạy chương trình
```bash
python Code/CuaHangTrucTuyen.py
```
> **Lưu ý:** Đảm bảo file `icon_ban_hang.ico` nằm cùng thư mục với file `CuaHangTrucTuyen.py`.

### 4. Đăng nhập
- **Admin:**  
  - Tài khoản: `admin`  
  - Mật khẩu: `admin`
- **User:**  
  - Đăng ký tài khoản mới

### 5. Cấu trúc thư mục
```
DoAnPy/
├── Code/
│   ├── AdminGUI.py
│   ├── UserGUI.py
│   ├── LoginGUI.py
│   ├── ClassUser.py
│   ├── ClassUserManager.py
│   ├── ClassProduct.py
│   ├── ClassFile.py
│   ├── crawl_tiki.py
│   ├── CuaHangTrucTuyen.py
│   ├── icon_ban_hang.ico
│   └── ...
├── users.json
├── products.json
└── README.md
```

### 6. Một số lưu ý
- Khi đăng ký, file `users.json` sẽ tự tạo nếu chưa có.
- Tài khoản `admin` là duy nhất, không thể đăng ký thêm.
- Dữ liệu sản phẩm lưu ở `products.json`.
- Nếu chạy file `.exe` đóng gói, hãy để file `icon_ban_hang.ico` cùng thư mục với file `.exe`.

---

## Đóng góp
Mọi đóng góp vui lòng gửi pull request hoặc liên hệ tác giả.

## License
MIT License
