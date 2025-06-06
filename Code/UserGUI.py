from tkinter import ttk, messagebox
import tkinter as tk
from ClassFile import File
 

def setup_style():
    # Thiết lập style cho các widget giao diện
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

class UserGUI:
    def __init__(self, root, icon_path):
        # Khởi tạo giao diện người dùng, hiển thị sản phẩm và các chức năng mua hàng
        setup_style()
        self.root = root
        self.icon_path = icon_path
        self.root.title("Danh sách sản phẩm (User)")
        self.root.geometry("900x520")
        self.root.iconbitmap(self.icon_path)
        self.file_manager = File("products.json")
        self.cart = []  # Danh sách các sản phẩm trong giỏ hàng

        main_frame = tk.Frame(self.root, bg="white", bd=2, relief="groove")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Nút Đăng xuất ở góc phải trên của main_frame
        logout_btn = ttk.Button(main_frame, text="Đăng xuất", command=self.logout_to_login)
        logout_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)  # Căn phải trên, cách mép 10px

        tk.Label(main_frame, text="DANH SÁCH SẢN PHẨM", font=("Segoe UI", 16, "bold"),
                 bg="white", fg="#1976d2").pack(pady=(18, 8))

        columns = ("id", "name", "cost", "description", "quantity", "catalogue")
        self.tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=10)
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=120)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=8)

        action_frame = tk.Frame(main_frame, bg="white")
        action_frame.pack(fill=tk.X, pady=10)

        tk.Label(action_frame, text="Số lượng:", bg="white", font=("Segoe UI", 11)).grid(row=0, column=0, padx=5)
        self.quantity_var = tk.IntVar(value=1)
        tk.Entry(action_frame, textvariable=self.quantity_var, width=5, font=("Segoe UI", 11)).grid(row=0, column=1, padx=5)

        btn_frame = tk.Frame(action_frame, bg="white")
        btn_frame.grid(row=0, column=2, padx=10, sticky="ew")
        action_frame.grid_columnconfigure(2, weight=1)
        ttk.Button(btn_frame, text="Thêm vào giỏ", command=self.add_to_cart).pack(side=tk.LEFT, padx=10, ipadx=8)
        ttk.Button(btn_frame, text="Thanh toán", command=self.checkout).pack(side=tk.LEFT, padx=10, ipadx=8)
        ttk.Button(btn_frame, text="Xem giỏ hàng", command=self.view_cart).pack(side=tk.LEFT, padx=10, ipadx=8)

        self.load_products()

    def logout_to_login(self):
        # Đăng xuất về giao diện đăng nhập
        self.root.destroy()
        import tkinter as tk
        from LoginGUI import LoginApp  # Import ngay trong hàm để tránh vòng lặp import
        root = tk.Tk()
        LoginApp(root, self.icon_path)  # Truyền icon_path vào đây
        root.iconbitmap(self.icon_path)
        root.mainloop()

    def load_products(self):
        # Đọc sản phẩm từ file và hiển thị lên bảng
        for sp in self.file_manager.products:
            self.tree.insert('', tk.END, values=(
                sp.id_product,
                sp.name_product,
                sp.cost,
                sp.description,
                sp.quantity,
                sp.catalogue
            ))
            
    def buy_product(self):
        # Hiển thị hóa đơn cho sản phẩm được chọn (không dùng trong giao diện này)
        selected = self.tree.selection()
        if not selected:
            tk.messagebox.showwarning("Chưa chọn sản phẩm", "Vui lòng chọn sản phẩm muốn mua!")
            return
        try:
            quantity = int(self.quantity_var.get())
            if quantity <= 0:
                raise ValueError
        except ValueError:
            tk.messagebox.showwarning("Số lượng không hợp lệ", "Vui lòng nhập số lượng hợp lệ!")
            return

        item = self.tree.item(selected[0])
        values = item['values']
        name = values[1]
        price = int(values[2])
        total = price * quantity

        bill = f"HÓA ĐƠN THANH TOÁN\n----------------------\n"
        bill += f"Sản phẩm: {name}\n"
        bill += f"Đơn giá: {price:,} VNĐ\n"
        bill += f"Số lượng: {quantity}\n"
        bill += f"Thành tiền: {total:,} VNĐ\n"
        tk.messagebox.showinfo("Hóa đơn", bill)

    def add_to_cart(self):
        # Thêm sản phẩm vào giỏ hàng, cộng dồn số lượng nếu đã có
        selected = self.tree.selection()
        if not selected:
            tk.messagebox.showwarning("Chưa chọn sản phẩm", "Vui lòng chọn sản phẩm muốn mua!")
            return
        try:
            quantity = int(self.quantity_var.get())
            if quantity <= 0:
                raise ValueError
        except ValueError:
            tk.messagebox.showwarning("Số lượng không hợp lệ", "Vui lòng nhập số lượng hợp lệ!")
            return

        item = self.tree.item(selected[0])
        values = item['values']
        product_id = values[0]
        name = values[1]
        price = int(values[2])
        available = int(values[4])

        if quantity > available:
            tk.messagebox.showwarning("Không đủ hàng", f"Chỉ còn {available} sản phẩm!")
            return

        for cart_item in self.cart:
            if cart_item["id"] == product_id:
                cart_item["quantity"] += quantity
                break
        else:
            self.cart.append({
                "id": product_id,
                "name": name,
                "price": price,
                "quantity": quantity
            })
        tk.messagebox.showinfo("Thành công", f"Đã thêm {quantity} {name} vào giỏ hàng!")

    def checkout(self):
        # Thanh toán toàn bộ sản phẩm trong giỏ, trừ số lượng và lưu file
        if not self.cart:
            tk.messagebox.showwarning("Giỏ hàng trống", "Bạn chưa chọn sản phẩm nào!")
            return

        total = 0
        bill = "HÓA ĐƠN THANH TOÁN\n----------------------\n"
        for item in self.cart:
            line_total = item["price"] * item["quantity"]
            bill += f"{item['name']} x {item['quantity']} = {line_total:,} VNĐ\n"
            total += line_total
            for sp in self.file_manager.products:
                if sp.id_product == item["id"]:
                    sp.quantity -= item["quantity"]
                    if sp.quantity < 0:
                        sp.quantity = 0

        bill += "----------------------\n"
        bill += f"TỔNG CỘNG: {total:,} VNĐ\n"
        tk.messagebox.showinfo("Hóa đơn", bill)

        self.file_manager.save_data()
        self.cart.clear()
        self.tree.delete(*self.tree.get_children())
        self.load_products()

    def view_cart(self):
        # Hiển thị thông tin các sản phẩm trong giỏ hàng và tổng tiền
        if not self.cart:
            tk.messagebox.showinfo("Giỏ hàng", "Giỏ hàng của bạn đang trống!")
            return
        bill = "GIỎ HÀNG CỦA BẠN\n----------------------\n"
        total = 0
        for item in self.cart:
            line_total = item["price"] * item["quantity"]
            bill += f"{item['name']} x {item['quantity']} = {line_total:,} VNĐ\n"
            total += line_total
        bill += "----------------------\n"
        bill += f"TỔNG CỘNG: {total:,} VNĐ"
        tk.messagebox.showinfo("Giỏ hàng", bill)
