import requests
import json

def crawl_tiki_products():
    """
    Hàm lấy danh sách sản phẩm từ API của Tiki và lưu vào file products.json.
    - Gửi request đến API của Tiki để lấy dữ liệu sản phẩm.
    - Xử lý dữ liệu từng sản phẩm: tách tên, mô tả, tạo danh mục, ID, số lượng mặc định.
    - Lưu danh sách sản phẩm vào file JSON.
    """
    url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=50&category=1789"  # API lấy 50 sản phẩm thuộc category 1789
    headers = {
        "User-Agent": "Mozilla/5.0"  # Đặt User-Agent để tránh bị chặn bởi Tiki
    }
    response = requests.get(url, headers=headers)  # Gửi GET request
    data = response.json()  # Chuyển kết quả trả về thành dict Python

    products = []
    for idx, item in enumerate(data.get("data", []), start=1):
        name_full = item["name"]  # Lấy tên đầy đủ của sản phẩm
        # Nếu tên có dấu " - ", tách ra làm tên và mô tả
        if " - " in name_full:
            name_product, description = name_full.split(" - ", 1)
        else:
            name_product = name_full
            # Nếu không có mô tả, lấy từ trường short_description hoặc mặc định
            description = item.get("short_description", "") or "Hàng chính hãng"
        # Lấy 2 từ đầu tiên của tên làm danh mục
        name_words = name_product.split()
        if len(name_words) >= 2:
            catalogue = " ".join(name_words[:2])
        elif name_words:
            catalogue = name_words[0]
        else:
            catalogue = "Chưa rõ"
        # Tạo ID sản phẩm dạng SP01, SP02, ...
        id_product = f"SP{idx:02d}"
        # Thêm sản phẩm vào danh sách
        products.append({
            "id_product": id_product,
            "name_product": name_product.strip(),
            "cost": item["price"],
            "description": description.strip() if description else "Hàng chính hãng",
            "quantity": 100,  # Số lượng mặc định
            "catalogue": catalogue
        })
    # Ghi danh sách sản phẩm ra file JSON
    with open("products.json", "w", encoding="utf8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    crawl_tiki_products()