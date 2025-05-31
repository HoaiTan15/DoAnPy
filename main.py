enable_cli = False   # Đổi thành True nếu muốn bật lại CLI

from tkinter import Tk
from LoginGUI import LoginApp

# Chạy chương trình: chọn CLI hoặc GUI

if __name__ == "__main__":
    # Nếu enable_cli = True, chạy giao diện dòng lệnh (CLI)
    if enable_cli:
        from your_cli_module import main_cli  # Import hàm main_cli từ module CLI
        main_cli()                            # Chạy chương trình CLI
    else:
        # Nếu enable_cli = False, chạy giao diện đồ họa (GUI)
        root = Tk()                           # Tạo cửa sổ Tkinter
        app = LoginApp(root)                  # Khởi tạo giao diện đăng nhập
        root.iconbitmap("icon_ban_hang.ico")  # Đặt icon cho cửa sổ
        root.mainloop()                       # Bắt đầu vòng lặp giao diện

# pyinstaller --onefile --windowed --icon=icon_ban_hang.ico main.py
