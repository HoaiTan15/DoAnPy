from ClassProduct import Product

class Cart:
    # Lớp quản lý giỏ hàng: thêm, xóa, cập nhật, tính tiền, hiển thị

    def __init__(self):
        # Khởi tạo giỏ hàng rỗng
        self.products = {}
        
    def add_product_to_cart(self, product, quantity=1):
        # Thêm sản phẩm vào giỏ, nếu có rồi thì tăng số lượng
        if not isinstance(product, Product):
            print("Đối tượng thêm vào không phải Product!")
            return
        if product.id_product not in self.products: 
            self.products[product.id_product] = (product, quantity)
        else: 
            current_quantity = self.products[product.id_product][1]
            self.products[product.id_product] = (product, current_quantity + quantity)
    
    def remove_product(self, product_id):
        # Xóa sản phẩm khỏi giỏ theo ID
        if product_id in self.products:
            self.products.pop(product_id)
        else:
            print(f"Sản phẩm có ID là {product_id} không có trong giỏ hàng!")
            
    def update_quantity(self, product_id, quantity):
        # Cập nhật số lượng sản phẩm, nếu <=0 thì xóa khỏi giỏ
        if product_id in self.products:
            if quantity > 0:
                self.products[product_id] = (self.products[product_id][0], quantity)
            else:
                self.remove_product(product_id)
        else:
            print(f"Sản phẩm có ID là {product_id} không có trong giỏ hàng!")
            
    def bill(self):
        # Tính tổng tiền các sản phẩm trong giỏ
        total = 0
        for product, quantity in self.products.values():
            try:
                total += int(product.cost) * quantity
            except Exception:
                print(f"Lỗi giá sản phẩm {product.id_product}")
        return total

    def clear_cart(self):
        # Xóa toàn bộ sản phẩm trong giỏ
        self.products.clear()
        
    def show_cart_infor(self):
        # In thông tin chi tiết các sản phẩm trong giỏ ra màn hình
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
