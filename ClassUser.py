class User:
    # Lớp User lưu thông tin người dùng

    def __init__(self, username, password, role):
        # Khởi tạo User mới
        self.username = username
        self.password = password
        self.role = role

    def convert_to_dict(self):
        # Chuyển User thành dict để lưu file
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

    @staticmethod
    def from_dict(data):
        # Tạo User từ dict (khi đọc file)
        return User(data["username"], data["password"], data["role"])

