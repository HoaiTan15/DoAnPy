from ClassUserManager import UserManager
from ClassFile import File
from ClassProduct import Product

def main_cli():
    # CLI cho phép đăng nhập, đăng ký, quên mật khẩu, phân quyền admin/user
    user_manager = UserManager("users.json")
    file_manager = File("products.json")

    def admin_menu():
        # Menu cho admin: quản lý sản phẩm
        while True:
            print("\n==== ADMIN MENU ====")
            print("1. Xem danh sách sản phẩm")
            print("2. Thêm sản phẩm mới")
            print("3. Xóa sản phẩm")
            print("4. Tìm kiếm sản phẩm theo ID")
            print("0. Đăng xuất")
            choice = input("Chọn chức năng: ").strip()
            if choice == "1":
                for sp in file_manager.products:
                    print(f"{sp.id_product} | {sp.name_product} | {sp.cost} | {sp.quantity} | {sp.catalogue}")
            elif choice == "2":
                id_product = input("ID sản phẩm: ").strip()
                name_product = input("Tên sản phẩm: ").strip()
                try:
                    cost = int(input("Giá: ").strip())
                    quantity = int(input("Số lượng: ").strip())
                except ValueError:
                    print("Giá và số lượng phải là số!")
                    continue
                description = input("Mô tả: ").strip()
                catalogue = input("Danh mục: ").strip()
                sp = Product(id_product, name_product, cost, description, quantity, catalogue)
                file_manager.add_product_to_file(sp)
                print("Đã thêm sản phẩm.")
            elif choice == "3":
                id_product = input("Nhập ID sản phẩm cần xóa: ").strip()
                file_manager.remove_product_from_file(id_product)
                print("Đã xóa sản phẩm (nếu tồn tại).")
            elif choice == "4":
                id_product = input("Nhập ID sản phẩm cần tìm: ").strip()
                sp = file_manager.find_product_by_id(id_product)
                if sp:
                    print(f"ID: {sp.id_product} | Tên: {sp.name_product} | Giá: {sp.cost} | SL: {sp.quantity} | Danh mục: {sp.catalogue}")
                else:
                    print("Không tìm thấy sản phẩm.")
            elif choice == "0":
                print("Đăng xuất.")
                break
            else:
                print("Lựa chọn không hợp lệ.")

    def user_menu():
        # Menu cho user: mua hàng, xem giỏ, thanh toán
        cart = []
        while True:
            print("\n==== USER MENU ====")
            print("1. Xem danh sách sản phẩm")
            print("2. Thêm vào giỏ hàng")
            print("3. Xem giỏ hàng")
            print("4. Thanh toán")
            print("0. Đăng xuất")
            choice = input("Chọn chức năng: ").strip()
            if choice == "1":
                for sp in file_manager.products:
                    print(f"{sp.id_product} | {sp.name_product} | {sp.cost} | {sp.quantity} | {sp.catalogue}")
            elif choice == "2":
                id_product = input("Nhập ID sản phẩm muốn mua: ").strip()
                sp = file_manager.find_product_by_id(id_product)
                if not sp:
                    print("Không tìm thấy sản phẩm.")
                    continue
                try:
                    quantity = int(input("Nhập số lượng: ").strip())
                except ValueError:
                    print("Số lượng không hợp lệ!")
                    continue
                if quantity <= 0 or quantity > sp.quantity:
                    print(f"Số lượng không hợp lệ! Hiện còn {sp.quantity}")
                    continue
                for item in cart:
                    if item["id"] == id_product:
                        item["quantity"] += quantity
                        break
                else:
                    cart.append({"id": id_product, "name": sp.name_product, "price": int(sp.cost), "quantity": quantity})
                print("Đã thêm vào giỏ hàng.")
            elif choice == "3":
                if not cart:
                    print("Giỏ hàng trống.")
                else:
                    print("Giỏ hàng:")
                    total = 0
                    for item in cart:
                        line_total = item["price"] * item["quantity"]
                        print(f"{item['name']} x {item['quantity']} = {line_total:,} VNĐ")
                        total += line_total
                    print(f"Tổng cộng: {total:,} VNĐ")
            elif choice == "4":
                if not cart:
                    print("Giỏ hàng trống.")
                    continue
                total = 0
                for item in cart:
                    sp = file_manager.find_product_by_id(item["id"])
                    if sp:
                        sp.quantity -= item["quantity"]
                        if sp.quantity < 0:
                            sp.quantity = 0
                    total += item["price"] * item["quantity"]
                file_manager.save_data()
                print(f"Thanh toán thành công! Tổng tiền: {total:,} VNĐ")
                cart.clear()
            elif choice == "0":
                print("Đăng xuất.")
                break
            else:
                print("Lựa chọn không hợp lệ.")

    def forgot_password():
        # Đặt lại mật khẩu cho tài khoản
        username = input("Nhập tài khoản cần đặt lại mật khẩu: ").strip()
        user = user_manager.get_user(username)
        if not user:
            print("Không tìm thấy tài khoản!")
            return
        new_pass = input("Nhập mật khẩu mới: ").strip()
        if not new_pass:
            print("Mật khẩu không được để trống!")
            return
        user.password = new_pass
        user_manager.save_users()
        print("Đã cập nhật mật khẩu mới.")

    # Vòng lặp chính CLI: đăng nhập, đăng ký, quên mật khẩu
    while True:
        print("\n==== ĐĂNG NHẬP HỆ THỐNG ====")
        print("1. Đăng nhập")
        print("2. Đăng ký")
        print("3. Quên mật khẩu")
        print("0. Thoát")
        choice = input("Chọn chức năng: ").strip()
        if choice == "1":
            username = input("Tài khoản: ").strip()
            password = input("Mật khẩu: ").strip()
            user = user_manager.authenticate(username, password)
            if user:
                print(f"Đăng nhập thành công! Xin chào {user.username} ({user.role})")
                if user.role == "admin":
                    admin_menu()
                else:
                    user_menu()
            else:
                print("Sai tài khoản hoặc mật khẩu!")
        elif choice == "2":
            username = input("Tài khoản mới: ").strip()
            password = input("Mật khẩu mới: ").strip()
            role = input("Vai trò (user/admin): ").strip().lower()
            if role not in ("user", "admin"):
                print("Vai trò chỉ được là 'user' hoặc 'admin'.")
                continue
            if not username or not password:
                print("Không được để trống tài khoản hoặc mật khẩu!")
                continue
            if user_manager.get_user(username):
                print("Tài khoản đã tồn tại!")
                continue
            user_manager.new_user(username, password, role)
            print("Đăng ký thành công!")
        elif choice == "3":
            forgot_password()
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")