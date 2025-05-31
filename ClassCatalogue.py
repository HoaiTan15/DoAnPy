from ClassProduct import Product 

class Catalogue:
    # Lớp quản lý danh mục sản phẩm

    def __init__(self, id_catalogue, name_catalogue):
        # Khởi tạo danh mục mới
        self.id_catalogue = id_catalogue
        self.name_catalogue = name_catalogue
        self.product_list = []
        
    def add_product_to_catalogue(self, new_item):
        # Thêm sản phẩm vào danh mục
        self.product_list.append(new_item)
    
    def remove_product(self, id_product):
        # Xóa sản phẩm khỏi danh mục theo ID
        self.product_list = [sp for sp in self.product_list if sp.id_product != id_product]
        
    def show_catalogue_infor(self):
        # Hiển thị thông tin danh mục và sản phẩm
        print(f"\nCatalogue: {self.name_catalogue}")
        print("=" * 30)
        for sp in self.product_list:
            sp.show_ProductInfor()
            
    def convert_to_dict(self):
        # Chuyển danh mục và sản phẩm sang dict để lưu file
        return {
           "id_catalogue": self.id_catalogue,
           "name_catalogue": self.name_catalogue,   
           "product_list": [sp.convert_to_dict() for sp in self.product_list]
        }

    def find_product_by_id(self, id_product):
        # Tìm sản phẩm theo ID trong danh mục
        for sp in self.product_list:
            if sp.id_product == id_product:
                return sp
        return None

    @staticmethod
    def from_dict(data):
        # Tạo đối tượng Catalogue từ dict (dùng khi đọc file)
        ct = Catalogue(data["id_catalogue"], data["name_catalogue"])
        for sp in data["product_list"]:
            ct.add_product_to_catalogue(Product.from_dict(sp))
        return ct
    
    def __repr__(self):
        # Chuỗi biểu diễn đối tượng Catalogue
        return f"Catalogue({self.id_catalogue} - {self.name_catalogue}, {len(self.product_list)} products)"
