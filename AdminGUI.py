import tkinter as tk
from tkinter import ttk, messagebox
from ClassFile import File
from ClassProduct import Product
import crawl_tiki  # Thêm dòng này để import hàm crawl_tiki_products

def setup_style():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview",
                    background="#f8fafc",
                    foreground="#222",
                    rowheight=28,
                    fieldbackground="#f8fafc",
                    font=("Segoe UI", 11))
    style.configure("Treeview.Heading",
                    background="#1976d2",
                    foreground="white",
                    font=("Segoe UI", 12, "bold"))
    style.configure("TButton",
                    font=("Segoe UI", 11),
                    padding=6)

class AdminGUI:
    def __init__(self, root=None):
        setup_style()
        if root is None:
            root = tk.Tk()
        self.root = root
        self.root.iconbitmap("icon_ban_hang.ico")
        self.root.title("Quản Lý Sản Phẩm Cửa Hàng (ADMIN)")
        self.root.geometry("950x700")
        self.file_manager = File("products.json")

        # Main frame
        main_frame = tk.Frame(self.root, bg="white", bd=2, relief="groove")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Frame chứa tiêu đề và nút đăng xuất
        title_frame = tk.Frame(main_frame, bg="white")
        title_frame.pack(fill=tk.X, pady=(10, 0))

        title_frame.grid_columnconfigure(0, weight=1)
        title_label = tk.Label(
            title_frame,
            text="QUẢN LÝ SẢN PHẨM",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            fg="#1976d2"
        )
        title_label.grid(row=0, column=0, pady=(0, 8), sticky="nsew")

        logout_btn = ttk.Button(title_frame, text="Đăng xuất", command=self.logout_to_login)
        logout_btn.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        # Treeview frame
        tree_frame = tk.Frame(main_frame, bg="white")
        tree_frame.pack(fill=tk.BOTH, expand=True)

        columns = ("id", "name", "cost", "description", "quantity", "catalogue")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=120)

        tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=tree_scroll.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Form nhập và nút chức năng (dưới cùng)
        form_btn_frame = tk.Frame(main_frame, bg="white")
        form_btn_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        self.entries = {}
        labels = ["ID", "Name", "Cost", "Description", "Quantity", "Catalogue"]
        for i, label in enumerate(labels):
            tk.Label(form_btn_frame, text=label, bg="white", font=("Segoe UI", 11)).grid(row=0, column=i, padx=5, pady=2, sticky="ew")
            entry = tk.Entry(form_btn_frame, width=15, font=("Segoe UI", 11))
            entry.grid(row=1, column=i, padx=5, pady=2, sticky="ew")
            self.entries[label.lower()] = entry
            form_btn_frame.grid_columnconfigure(i, weight=1)  # Cho phép các cột co giãn đều

        # Căn giữa 5 nút chức năng (thêm nút Get API)
        btn_frame = tk.Frame(form_btn_frame, bg="white")
        btn_frame.grid(row=2, column=0, columnspan=6, pady=10, sticky="ew")
        for i in range(6):
            btn_frame.grid_columnconfigure(i, weight=1)  # Đảm bảo nút căn giữa khi phóng to

        ttk.Button(btn_frame, text="Thêm", command=self.add_product).grid(row=0, column=1, padx=10, ipadx=10)
        ttk.Button(btn_frame, text="Xóa", command=self.delete_product).grid(row=0, column=2, padx=10, ipadx=10)
        ttk.Button(btn_frame, text="Cập nhật", command=self.update_product).grid(row=0, column=3, padx=10, ipadx=10)
        ttk.Button(btn_frame, text="Làm mới", command=self.load_products).grid(row=0, column=4, padx=10, ipadx=10)
        ttk.Button(btn_frame, text="Get API", command=self.get_api_products).grid(row=0, column=5, padx=10, ipadx=10)  # Nút mới

        self.load_products()

    def load_products(self):
        # Hiển thị danh sách sản phẩm lên bảng
        for i in self.tree.get_children():
            self.tree.delete(i)
        for sp in self.file_manager.products:
            self.tree.insert('', tk.END, values=(
                sp.id_product,
                sp.name_product,
                sp.cost,
                sp.description,
                sp.quantity,
                sp.catalogue
            ))
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def add_product(self):
        # Thêm sản phẩm mới từ form vào file
        data = self.get_entry_data()
        if not data:
            return
        if self.file_manager.find_product_by_id(data['new_id']):
            messagebox.showwarning("Lỗi", "ID đã tồn tại!")
            return
        sp = Product(
            data["new_id"],
            data["new_name"],
            data["new_cost"],
            data["new_description"],
            data["new_quantity"],
            data["new_catalogue"]
        )
        self.file_manager.add_product_to_file(sp)
        self.load_products()
        messagebox.showinfo("Thành công", "Đã thêm sản phẩm!")

    def delete_product(self):
        # Xóa sản phẩm được chọn khỏi file
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Chưa chọn", "Vui lòng chọn sản phẩm để xóa!")
            return
        item = self.tree.item(selected)
        self.file_manager.remove_product_from_file(item["values"][0])
        self.load_products()
        messagebox.showinfo("Thành công", "Đã xóa sản phẩm!")

    def update_product(self):
        # Cập nhật sản phẩm được chọn bằng dữ liệu mới từ form
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Chưa chọn", "Vui lòng chọn sản phẩm để cập nhật!")
            return
        data = self.get_entry_data()
        if not data:
            return
        self.file_manager.update_product_in_file(**data)
        self.load_products()
        messagebox.showinfo("Thành công", "Đã cập nhật sản phẩm!")

    def get_entry_data(self):
        # Lấy dữ liệu từ form, trả về dict hoặc None nếu nhập sai
        try:
            return {
                "new_id": self.entries["id"].get().strip(),
                "new_name": self.entries["name"].get().strip(),
                "new_cost": int(self.entries["cost"].get().strip()),
                "new_description": self.entries["description"].get().strip(),
                "new_quantity": int(self.entries["quantity"].get().strip()),
                "new_catalogue": self.entries["catalogue"].get().strip()
            }
        except ValueError:
            messagebox.showerror("Lỗi nhập liệu", "Giá và Số lượng phải là số và không được để trống!")
            return None

    def on_tree_select(self, event):
        # Đổ dữ liệu sản phẩm được chọn lên form
        selected = self.tree.focus()
        if not selected:
            return
        values = self.tree.item(selected, "values")
        keys = ["id", "name", "cost", "description", "quantity", "catalogue"]
        for i, key in enumerate(keys):
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, values[i])

    def get_api_products(self):
        # Lấy dữ liệu sản phẩm từ API và cập nhật bảng
        try:
            crawl_tiki.crawl_tiki_products()
            self.file_manager.load_data()
            self.load_products()
            messagebox.showinfo("Thành công", "Đã lấy dữ liệu sản phẩm từ API!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lấy dữ liệu API thất bại!\n{e}")

    def logout_to_login(self):
        # Đăng xuất về giao diện đăng nhập
        self.root.destroy()
        import tkinter as tk
        from LoginGUI import LoginApp  # Import trong hàm để tránh vòng lặp import
        root = tk.Tk()
        LoginApp(root)
        root.mainloop()


