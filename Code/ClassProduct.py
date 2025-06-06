class Product:
    # Lớp sản phẩm: lưu thông tin sản phẩm

    def __init__(self, id_product, name_product, cost, description, quantity, catalogue):
        # Khởi tạo sản phẩm mới
        self.id_product = id_product
        self.name_product = name_product
        self.cost = cost
        self.description = description
        self.quantity = quantity
        self.catalogue = catalogue

    def show_product_infor(self):
        # Hiển thị thông tin sản phẩm
        print(f"Product's ID: {self.id_product}")
        print(f"Product's name: {self.name_product}")
        print(f"Cost: {self.cost} VND")
        print(f"Description: {self.description}")
        print(f"Quantity: {self.quantity}")
        print("=" * 30)
    
    def update_cost(self, new_cost):
        # Cập nhật giá sản phẩm
        self.cost = new_cost
    
    def update_quantity(self, new_quantity):
        # Cập nhật số lượng sản phẩm
        self.quantity = new_quantity
    
    def convert_to_dict(self):
        # Chuyển đối tượng thành dict để lưu file
        return {
            "id_product": self.id_product,
            "name_product": self.name_product,
            "cost": self.cost,
            "description": self.description,
            "quantity": self.quantity,
            "catalogue": self.catalogue
        }

    @staticmethod
    def from_dict(data):
        # Tạo Product từ dict (khi đọc file)
        return Product(
            data["id_product"],
            data["name_product"],
            data["cost"],
            data["description"],
            data["quantity"],
            data["catalogue"]
        )
    
    def __repr__(self):
        # Chuỗi đại diện sản phẩm
        return f"Product({self.id_product}, {self.name_product}, {self.cost} VND)"
    
    def is_in_stock(self):
        # Kiểm tra còn hàng không
        return self.quantity > 0



