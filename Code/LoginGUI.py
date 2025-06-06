import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from ClassUserManager import UserManager
from AdminGUI import AdminGUI
from UserGUI import UserGUI
import os

class LoginApp:
    # Giao diện đăng nhập, đăng ký, quên mật khẩu

    def __init__(self, root, icon_path):
        # Khởi tạo giao diện và các thành phần
        self.root = root
        self.icon_path = icon_path
        self.root.iconbitmap(self.icon_path)
        self.root.title("Đăng nhập hệ thống")
        self.root.geometry("370x400")
        self.root.configure(bg="#f0f4f8")

        self.user_manager = UserManager("users.json")

        frame = tk.Frame(root, bg="white", bd=2, relief="groove")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=320, height=340)

        tk.Label(frame, text="ĐĂNG NHẬP", font=("Arial", 16, "bold"), bg="white", fg="#1976d2").pack(pady=(15, 10))
        tk.Label(frame, text="Tài khoản", bg="white", anchor="w").pack(fill="x", padx=30)
        self.entry_user = ttk.Entry(frame, font=("Arial", 11))
        self.entry_user.pack(padx=30, pady=5, fill="x")
        tk.Label(frame, text="Mật khẩu", bg="white", anchor="w").pack(fill="x", padx=30)
        pass_frame = tk.Frame(frame, bg="white")
        pass_frame.pack(fill="x", padx=30)
        self.entry_pass = ttk.Entry(pass_frame, show="*", font=("Arial", 11))
        self.entry_pass.pack(side="left", fill="x", expand=True)

        lbl_forgot = tk.Label(
            frame,
            text="Quên mật khẩu?",
            fg="#1976d2",
            bg="white",
            cursor="hand2",
            font=("Arial", 9, "underline"),
            anchor="e",
            justify="right"
        )
        lbl_forgot.pack(fill="x", padx=30, pady=(0, 5))
        lbl_forgot.bind("<Button-1>", lambda e: self.reset_password())

        ttk.Button(frame, text="Đăng nhập", command=self.login).pack(pady=(15, 5), padx=30, fill="x")
        ttk.Button(frame, text="Đăng ký", command=self.register).pack(pady=2, padx=30, fill="x")

        self.root.bind('<Return>', lambda event: self.login())

        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws // 2) - (w // 2)
        y = (hs // 2) - (h // 2)
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    def login(self):
        # Xử lý đăng nhập, mở giao diện theo vai trò
        username = self.entry_user.get().strip()
        password = self.entry_pass.get().strip()
        # Nếu là admin đặc biệt
        if username == "admin" and password == "admin":
            self.root.destroy()
            import tkinter as tk
            from AdminGUI import AdminGUI
            root_admin = tk.Tk()
            AdminGUI(root_admin, self.icon_path)  # TRUYỀN icon_path vào đây!
            root_admin.mainloop()
            return
        # Còn lại kiểm tra file json như bình thường
        user = self.user_manager.authenticate(username, password)
        if user:
            self.root.destroy()
            import tkinter as tk
            from UserGUI import UserGUI
            root = tk.Tk()
            UserGUI(root, self.icon_path)  # SỬA LẠI: truyền icon_path vào đây!
            root.iconbitmap(self.icon_path)
            root.mainloop()
        else:
            messagebox.showerror("Lỗi", "Tài khoản hoặc mật khẩu sai!")

    def register(self):
        # Hiển thị cửa sổ đăng ký tài khoản mới
        self.root.withdraw()
        reg_win = tk.Toplevel(self.root)
        reg_win.title("Đăng ký tài khoản")
        reg_win.geometry("320x270")
        reg_win.resizable(False, False)
        reg_win.configure(bg="white")
        reg_win.grab_set()
        reg_win.iconbitmap(self.icon_path)  # SỬA DÒNG NÀY

        tk.Label(reg_win, text="ĐĂNG KÝ", font=("Arial", 15, "bold"), bg="white", fg="#1976d2").pack(pady=(15, 10))
        tk.Label(reg_win, text="Tài khoản", bg="white", anchor="w").pack(fill="x", padx=30)
        entry_user = ttk.Entry(reg_win, font=("Arial", 11))
        entry_user.pack(padx=30, pady=5, fill="x")
        tk.Label(reg_win, text="Mật khẩu", bg="white", anchor="w").pack(fill="x", padx=30)
        entry_pass = ttk.Entry(reg_win, show="*", font=("Arial", 11))
        entry_pass.pack(padx=30, pady=5, fill="x")

        def do_register():
            username = entry_user.get().strip()
            password = entry_pass.get().strip()
            role = "user"
            if not username or not password:
                messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ tài khoản và mật khẩu!", parent=reg_win)
                return
            if username == "admin":
                messagebox.showerror("Lỗi", "Không thể đăng ký tài khoản admin!", parent=reg_win)
                return
            # Nếu chưa có file json thì tạo file mới
            if not os.path.exists("users.json"):
                with open("users.json", "w", encoding="utf8") as f:
                    f.write("[]")
            if self.user_manager.get_user(username):
                messagebox.showerror("Lỗi", "Tài khoản đã tồn tại!", parent=reg_win)
                return
            self.user_manager.new_user(username, password, role)
            messagebox.showinfo("Thành công", "Đăng ký thành công!", parent=reg_win)
            reg_win.destroy()
            self.root.deiconify()

        def on_close():
            self.root.deiconify()
            reg_win.destroy()

        btn_register = ttk.Button(reg_win, text="Đăng ký", command=do_register)
        btn_register.pack(pady=15, padx=30, fill="x")
        reg_win.protocol("WM_DELETE_WINDOW", on_close)

    def reset_password(self):
        # Xử lý chức năng quên mật khẩu
        self.root.withdraw()
        username = self.custom_askstring("Quên mật khẩu", "Nhập tài khoản:")
        if username is None:
            self.root.deiconify()
            return

        user = self.user_manager.get_user(username)
        if not user:
            messagebox.showerror("Lỗi", "Không tìm thấy tài khoản!", parent=self.root)
            self.root.deiconify()
            return

        new_pass = self.custom_askstring("Quên mật khẩu", "Nhập mật khẩu mới:", show="*")
        if new_pass:
            user.password = new_pass
            self.user_manager.save_users()
            messagebox.showinfo("Thành công", "Mật khẩu đã được cập nhật.", parent=self.root)
        self.root.deiconify()

    def custom_askstring(self, title, prompt, show=None):
        dialog = tk.Toplevel()
        dialog.title(title)
        dialog.iconbitmap(self.icon_path)  # SỬA DÒNG NÀY
        dialog.resizable(False, False)
        dialog.grab_set()
        dialog.geometry("320x140")

        tk.Label(dialog, text=prompt, font=("Arial", 12)).pack(pady=(15, 5))
        entry = ttk.Entry(dialog, font=("Arial", 12), show=show)
        entry.pack(padx=20, pady=5, fill="x")
        entry.focus_set()

        result = {"value": None}

        def on_ok():
            result["value"] = entry.get()
            dialog.destroy()

        def on_cancel():
            dialog.destroy()

        btn_frame = tk.Frame(dialog)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="OK", width=10, command=on_ok).pack(side="left", padx=10)
        ttk.Button(btn_frame, text="Cancel", width=10, command=on_cancel).pack(side="left", padx=10)

        dialog.bind('<Return>', lambda e: on_ok())
        dialog.bind('<Escape>', lambda e: on_cancel())

        dialog.update_idletasks()
        w = dialog.winfo_width()
        h = dialog.winfo_height()
        ws = dialog.winfo_screenwidth()
        hs = dialog.winfo_screenheight()
        x = (ws // 2) - (w // 2)
        y = (hs // 2) - (h // 2)
        dialog.geometry(f"{w}x{h}+{x}+{y}")

        dialog.wait_window()
        return result["value"]

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root, "icon_ban_hang.ico")
    root.mainloop()
