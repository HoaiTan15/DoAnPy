from ClassProduct import Product

class Cart:
    """
    Lớp Cart quản lý giỏ hàng của người dùng, cho phép thêm, xóa, cập nhật sản phẩm,
    tính tổng tiền và hiển thị thông tin giỏ hàng.
    """

    def __init__(self):
        """
        Khởi tạo giỏ hàng rỗng dưới dạng dictionary.
        Key: id_product, Value: tuple (Product, quantity)
        """
        self.products = {}
        
    def add_product_to_cart(self, product, quantity=1):
        """
        Thêm sản phẩm vào giỏ hàng.
        Nếu sản phẩm đã có thì tăng số lượng.
        Args:
            product (Product): Đối tượng sản phẩm cần thêm.
            quantity (int): Số lượng muốn thêm (mặc định là 1).
        """
        if not isinstance(product, Product):
            print("Đối tượng thêm vào không phải Product!")
            return
        if product.id_product not in self.products: 
            self.products[product.id_product] = (product, quantity)
        else: 
            current_quantity = self.products[product.id_product][1]
            self.products[product.id_product] = (product, current_quantity + quantity)
    
    def remove_product(self, product_id):
        """
        Xóa sản phẩm khỏi giỏ hàng theo ID.
        Args:
            product_id (str): ID sản phẩm cần xóa.
        """
        if product_id in self.products:
            self.products.pop(product_id)
        else:
            print(f"Sản phẩm có ID là {product_id} không có trong giỏ hàng!")
            
    def update_quantity(self, product_id, quantity):
        """
        Cập nhật số lượng sản phẩm trong giỏ hàng.
        Nếu quantity <= 0 thì xóa sản phẩm khỏi giỏ.
        Args:
            product_id (str): ID sản phẩm cần cập nhật.
            quantity (int): Số lượng mới.
        """
        if product_id in self.products:
            if quantity > 0:
                self.products[product_id] = (self.products[product_id][0], quantity)
            else:
                self.remove_product(product_id)
        else:
            print(f"Sản phẩm có ID là {product_id} không có trong giỏ hàng!")
            
    def bill(self):
        """
        Tính tổng tiền của toàn bộ sản phẩm trong giỏ hàng.
        Returns:
            int: Tổng tiền.
        """
        total = 0
        for product, quantity in self.products.values():
            # Kiểm tra kiểu dữ liệu cost
            try:
                total += int(product.cost) * quantity
            except Exception:
                print(f"Lỗi giá sản phẩm {product.id_product}")
        return total

    def clear_cart(self):
        """
        Xóa toàn bộ sản phẩm trong giỏ hàng (dùng khi thanh toán hoặc hủy).
        """
        self.products.clear()
        
    def show_cart_infor(self):
        """
        Hiển thị thông tin chi tiết các sản phẩm trong giỏ hàng ra màn hình console.
        """
        if not self.products:
            print("Giỏ hàng trống!")
        else:
            print("$$$ GIỎ HÀNG $$$")
            print("="*30)
            for product, quantity in self.products.values():
                print(f"ID: {product.id_product}")
                print(f"Tên sản phẩm: {product.name_product}")
                print(f"Số lượng: {quantity}")
                print(f"Giá 1 sản phẩm: {product.cost} VND")
                print(f"Tổng: {int(product.cost) * quantity} VND")
                print("=" * 30)
            print(f"Thành tiền: {self.bill()} VND")
