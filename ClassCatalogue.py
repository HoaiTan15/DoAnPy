from ClassProduct import Product 

class Catalogue:
    """
    Lớp Catalogue quản lý một danh mục sản phẩm, cho phép thêm, xóa, tìm kiếm sản phẩm,
    hiển thị thông tin danh mục, chuyển đổi sang dict để lưu file, và khởi tạo từ dict.
    """
    
    def __init__(self, id_catalogue, name_catalogue):
        """
        Khởi tạo một danh mục mới.
        Args:
            id_catalogue (str): Mã danh mục.
            name_catalogue (str): Tên danh mục.
        """
        self.id_catalogue = id_catalogue
        self.name_catalogue = name_catalogue
        self.product_list = []
        
    def add_product_to_catalogue(self, new_item):
        """
        Thêm sản phẩm mới vào danh mục.
        Args:
            new_item (Product): Đối tượng sản phẩm cần thêm.
        """
        self.product_list.append(new_item)
    
    def remove_product(self, id_product):
        """
        Xóa sản phẩm khỏi danh mục theo ID.
        Args:
            id_product (str): ID sản phẩm cần xóa.
        """
        self.product_list = [sp for sp in self.product_list if sp.id_product != id_product]
        
    def show_catalogue_infor(self):
        """
        Hiển thị thông tin danh mục và toàn bộ sản phẩm trong danh mục ra màn hình console.
        """
        print(f"\nCatalogue: {self.name_catalogue}")
        print("=" * 30)
        for sp in self.product_list:
            sp.show_ProductInfor()
            
    def convert_to_dict(self):
        """
        Chuyển danh mục và các sản phẩm thành dict để lưu file JSON.
        Returns:
            dict: Dữ liệu danh mục ở dạng dictionary.
        """
        return {
           "id_catalogue": self.id_catalogue,
           "name_catalogue": self.name_catalogue,   
           "product_list": [sp.convert_to_dict() for sp in self.product_list]
        }

    def find_product_by_id(self, id_product):
        """
        Tìm sản phẩm trong danh mục theo ID.
        Args:
            id_product (str): ID sản phẩm cần tìm.
        Returns:
            Product hoặc None nếu không tìm thấy.
        """
        for sp in self.product_list:
            if sp.id_product == id_product:
                return sp
        return None

    @staticmethod
    def from_dict(data):
        """
        Khởi tạo đối tượng Catalogue từ dữ liệu dictionary (thường dùng khi đọc từ file JSON).
        Args:
            data (dict): Dữ liệu danh mục ở dạng dictionary.
        Returns:
            Catalogue: Đối tượng Catalogue đã khởi tạo.
        """
        ct = Catalogue(data["id_catalogue"], data["name_catalogue"])
        for sp in data["product_list"]:
            ct.add_product_to_catalogue(Product.from_dict(sp))
        return ct
    
    def __repr__(self):
        """
        Trả về chuỗi biểu diễn đối tượng Catalogue.
        """
        return f"Catalogue({self.id_catalogue} - {self.name_catalogue}, {len(self.product_list)} products)"
