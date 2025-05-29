from ClassProduct import Product
import json

class File:
    """
    Lớp File quản lý việc đọc, ghi, cập nhật, xóa sản phẩm trong file JSON.
    Dùng để thao tác với danh sách sản phẩm lưu trữ trên ổ đĩa.
    """

    def __init__(self, filename):
        """
        Khởi tạo đối tượng File với tên file dữ liệu.
        Args:
            filename (str): Đường dẫn file JSON lưu sản phẩm.
        """
        self.filename = filename
        self.products = []
        self.load_data()

    def load_data(self):
        """
        Đọc dữ liệu sản phẩm từ file JSON và khởi tạo danh sách Product.
        Nếu file không tồn tại hoặc lỗi, danh sách sản phẩm sẽ rỗng.
        """
        try:
            with open(self.filename, "r", encoding="utf8") as f:
                data = json.load(f)
                self.products = [Product(**item) for item in data]
        except Exception:
            self.products = []

    def save_data(self):
        """
        Ghi toàn bộ danh sách sản phẩm hiện tại vào file JSON.
        """
        with open(self.filename, "w", encoding="utf8") as f:
            json.dump([sp.__dict__ for sp in self.products], f, ensure_ascii=False, indent=4)

    def add_product_to_file(self, product):
        """
        Thêm một sản phẩm mới vào danh sách và lưu lại file.
        Args:
            product (Product): Đối tượng sản phẩm cần thêm.
        """
        self.products.append(product)
        self.save_data()

    def remove_product_from_file(self, id_product):
        """
        Xóa sản phẩm khỏi danh sách theo ID và lưu lại file.
        Args:
            id_product (str): ID sản phẩm cần xóa.
        """
        self.products = [sp for sp in self.products if sp.id_product != id_product]
        self.save_data()

    def update_product_in_file(self, new_id, new_name, new_cost, new_description, new_quantity, new_catalogue):
        """
        Cập nhật thông tin sản phẩm theo ID và lưu lại file.
        Args:
            new_id (str): ID sản phẩm cần cập nhật.
            new_name (str): Tên mới.
            new_cost (int/str): Giá mới.
            new_description (str): Mô tả mới.
            new_quantity (int): Số lượng mới.
            new_catalogue (str): Danh mục mới.
        """
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
        """
        Tìm sản phẩm trong danh sách theo ID.
        Args:
            id_product (str): ID sản phẩm cần tìm.
        Returns:
            Product hoặc None nếu không tìm thấy.
        """
        for sp in self.products:
            if sp.id_product == id_product:
                return sp
        return None

