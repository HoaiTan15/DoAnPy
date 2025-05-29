class Product:
    """
    Lớp Product đại diện cho một sản phẩm trong hệ thống.
    Lưu trữ thông tin về ID, tên, giá, mô tả, số lượng và danh mục sản phẩm.
    """

    def __init__(self, id_product, name_product, cost, description, quantity, catalogue):
        """
        Khởi tạo một đối tượng Product mới.
        Args:
            id_product (str): Mã sản phẩm.
            name_product (str): Tên sản phẩm.
            cost (int/str): Giá sản phẩm.
            description (str): Mô tả sản phẩm.
            quantity (int): Số lượng sản phẩm.
            catalogue (str): Danh mục sản phẩm.
        """
        self.id_product = id_product
        self.name_product = name_product
        self.cost = cost
        self.description = description
        self.quantity = quantity
        self.catalogue = catalogue

    #Hiển thị thông tin sản phẩm    
    def show_product_infor(self):
        """
        Hiển thị thông tin chi tiết của sản phẩm ra màn hình console.
        """
        print(f"Product's ID: {self.id_product}")
        print(f"Product's name: {self.name_product}")
        print(f"Cost: {self.cost} VND")
        print(f"Description: {self.description}")
        print(f"Quantity: {self.quantity}")
        print("=" * 30)
    
    #Cập nhật giá bán  
    def update_cost(self, new_cost):
        """
        Cập nhật giá bán mới cho sản phẩm.
        Args:
            new_cost (int/str): Giá mới.
        """
        self.cost = new_cost
    
    #Cập nhật số lượng của sản phẩm 
    def update_quantity(self, new_quantity):
        """
        Cập nhật số lượng mới cho sản phẩm.
        Args:
            new_quantity (int): Số lượng mới.
        """
        self.quantity = new_quantity
    
    #Chuyển các object thành dạng dictionary 
    def convert_to_dict(self):
        """
        Chuyển đối tượng Product thành dictionary để lưu file JSON.
        Returns:
            dict: Dữ liệu sản phẩm ở dạng dictionary.
        """
        return {
            "id_product": self.id_product,
            "name_product": self.name_product,
            "cost": self.cost,
            "description": self.description,
            "quantity": self.quantity,
            "catalogue": self.catalogue
        }

    #Lấy dữ liệu dạng dictionary(đọc từ file JSON)
    @staticmethod
    def from_dict(data):
        """
        Khởi tạo đối tượng Product từ dữ liệu dictionary (thường dùng khi đọc từ file JSON).
        Args:
            data (dict): Dữ liệu sản phẩm ở dạng dictionary.
        Returns:
            Product: Đối tượng Product đã khởi tạo.
        """
        return Product(
            data["id_product"],
            data["name_product"],
            data["cost"],
            data["description"],
            data["quantity"],
            data["catalogue"]
        )
    
    def __repr__(self):
        return f"Product({self.id_product}, {self.name_product}, {self.cost} VND)"
    def is_in_stock(self):
        return self.quantity > 0



