from ClassUser import User
import json

class UserManager:
    """
    Lớp UserManager quản lý danh sách người dùng, cho phép thêm, xóa, tìm kiếm,
    xác thực đăng nhập và lưu/đọc dữ liệu người dùng từ file JSON.
    """

    def __init__(self, filename):
        """
        Khởi tạo UserManager với tên file dữ liệu.
        Args:
            filename (str): Đường dẫn file JSON lưu thông tin người dùng.
        """
        self.filename = filename
        self.users = self.load_users()
    
    def load_users(self):
        """
        Đọc danh sách người dùng từ file JSON.
        Returns:
            list: Danh sách các đối tượng User.
        """
        try:
            with open(self.filename, "r", encoding="utf8") as file:
                data = json.load(file)
                return [User.from_dict(u) for u in data]
        except (FileNotFoundError, json.JSONDecodeError): 
            return []
    
    def save_users(self):
        """
        Ghi danh sách người dùng hiện tại vào file JSON.
        """
        with open(self.filename, "w", encoding="utf8") as file:
            json.dump([u.convert_to_dict() for u in self.users], file)
            
    def new_user(self, username, password, role):
        """
        Thêm người dùng mới vào hệ thống.
        Args:
            username (str): Tên đăng nhập.
            password (str): Mật khẩu.
            role (str): Vai trò (user/admin).
        """
        for user in self.users:
            if user.username == username:
                print("Tài khoản đã tồn tại!")
                return
        
        new_user = User(username, password, role)
        self.users.append(new_user)
        self.save_users()
        print("Tạo tài khoản thành công!")
        
    def delete_user(self, username):
        """
        Xóa người dùng khỏi hệ thống theo tên đăng nhập.
        Args:
            username (str): Tên đăng nhập cần xóa.
        """
        self.users = [u for u in self.users if u.username != username]
        self.save_users()

    def get_user(self, username):
        """
        Tìm và trả về đối tượng User theo tên đăng nhập.
        Args:
            username (str): Tên đăng nhập cần tìm.
        Returns:
            User hoặc None nếu không tìm thấy.
        """
        for user in self.users:
            if user.username == username:
                return user
        return None

    def authenticate(self, username, password):
        """
        Kiểm tra thông tin đăng nhập.
        Args:
            username (str): Tên đăng nhập.
            password (str): Mật khẩu.
        Returns:
            User nếu đăng nhập đúng, None nếu sai.
        """
        for user in self.users:
            if user.username == username and user.password == password:
                return user 
        return None
