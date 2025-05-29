class User:
    """
    Lớp User đại diện cho một người dùng trong hệ thống.
    Lưu trữ thông tin về tên đăng nhập, mật khẩu và vai trò (user/admin).
    """

    def __init__(self, username, password, role):
        """
        Khởi tạo một đối tượng User mới.
        Args:
            username (str): Tên đăng nhập.
            password (str): Mật khẩu.
            role (str): Vai trò của người dùng (user hoặc admin).
        """
        self.username = username
        self.password = password
        self.role = role

    def convert_to_dict(self):
        """
        Chuyển đối tượng User thành dictionary để lưu file JSON.
        Returns:
            dict: Dữ liệu người dùng ở dạng dictionary.
        """
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

    @staticmethod
    def from_dict(data):
        """
        Khởi tạo đối tượng User từ dữ liệu dictionary (thường dùng khi đọc từ file JSON).
        Args:
            data (dict): Dữ liệu người dùng ở dạng dictionary.
        Returns:
            User: Đối tượng User đã khởi tạo.
        """
        return User(data["username"], data["password"], data["role"])

