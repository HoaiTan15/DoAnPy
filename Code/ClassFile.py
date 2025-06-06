from ClassProduct import Product
import json

class File:
    # Quản lý đọc, ghi, cập nhật, xóa sản phẩm trong file JSON

    def __init__(self, filename):
        # Khởi tạo với tên file và load dữ liệu
        self.filename = filename
        self.products = []
        self.load_data()

    def load_data(self):
        # Đọc dữ liệu sản phẩm từ file JSON
        try:
            with open(self.filename, "r", encoding="utf8") as f:
                data = json.load(f)
                self.products = [Product(**item) for item in data]
        except Exception:
            self.products = []

    def save_data(self):
        # Ghi danh sách sản phẩm vào file JSON
        with open(self.filename, "w", encoding="utf8") as f:
            json.dump([sp.__dict__ for sp in self.products], f, ensure_ascii=False, indent=4)

    def add_product_to_file(self, product):
        # Thêm sản phẩm mới và lưu file
        self.products.append(product)
        self.save_data()

    def remove_product_from_file(self, id_product):
        # Xóa sản phẩm theo ID và lưu file
        self.products = [sp for sp in self.products if sp.id_product != id_product]
        self.save_data()

    def update_product_in_file(self, new_id, new_name, new_cost, new_description, new_quantity, new_catalogue):
        # Cập nhật thông tin sản phẩm theo ID và lưu file
        for sp in self.products:
            if sp.id_product == new_id:
                sp.name_product = new_name
                sp.cost = new_cost
                sp.description = new_description
                sp.quantity = new_quantity
                sp.catalogue = new_catalogue
                self.save_data()
                break

    def find_product_by_id(self, id_product):
        # Tìm sản phẩm theo ID
        for sp in self.products:
            if sp.id_product == id_product:
                return sp
        return None

