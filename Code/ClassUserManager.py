from ClassUser import User
import json

class UserManager:
    # Quản lý danh sách user, thêm/xóa/tìm kiếm/xác thực và lưu/đọc file

    def __init__(self, filename):
        # Khởi tạo với tên file và load user
        self.filename = filename
        self.users = self.load_users()
    
    def load_users(self):
        # Đọc danh sách user từ file JSON
        try:
            with open(self.filename, "r", encoding="utf8") as file:
                data = json.load(file)
                return [User.from_dict(u) for u in data]
        except (FileNotFoundError, json.JSONDecodeError): 
            return []
    
    def save_users(self):
        # Ghi danh sách user vào file JSON
        with open(self.filename, "w", encoding="utf8") as file:
            json.dump([u.convert_to_dict() for u in self.users], file)
            
    def new_user(self, username, password, role):
        # Thêm user mới
        for user in self.users:
            if user.username == username:
                print("Tài khoản đã tồn tại!")
                return
        
        new_user = User(username, password, role)
        self.users.append(new_user)
        self.save_users()
        print("Tạo tài khoản thành công!")
        
    def delete_user(self, username):
        # Xóa user theo tên đăng nhập
        self.users = [u for u in self.users if u.username != username]
        self.save_users()

    def get_user(self, username):
        # Tìm user theo tên đăng nhập
        for user in self.users:
            if user.username == username:
                return user
        return None

    def authenticate(self, username, password):
        # Kiểm tra đăng nhập
        for user in self.users:
            if user.username == username and user.password == password:
                return user 
        return None
