enable_cli = False   # Đổi thành True nếu muốn bật lại CLI

from tkinter import Tk
from LoginGUI import LoginApp
import os
import sys

def resource_path(relative_path):
    """Lấy đường dẫn tuyệt đối đến resource, dùng cho cả khi chạy script và khi đóng gói exe."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), relative_path)

# Chạy chương trình: chọn CLI hoặc GUI

if __name__ == "__main__":
    root = Tk()
    icon_path = resource_path("icon_ban_hang.ico")
    app = LoginApp(root, icon_path)
    root.iconbitmap(icon_path)
    root.mainloop()                       

# pyinstaller --onefile --windowed --icon=icon_ban_hang.ico CuaHangTrucTuyen.py
