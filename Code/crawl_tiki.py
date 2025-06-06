import requests
import json

def crawl_tiki_products():
    # Lấy danh sách sản phẩm từ API Tiki và lưu vào file JSON
    url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=50&category=1789"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    products = []
    for idx, item in enumerate(data.get("data", []), start=1):
        name_full = item["name"]
        # Tách tên và mô tả nếu có dấu " - "
        if " - " in name_full:
            name_product, description = name_full.split(" - ", 1)
        else:
            name_product = name_full
            description = item.get("short_description", "") or "Hàng chính hãng"
        # Lấy 2 từ đầu làm danh mục
        name_words = name_product.split()
        if len(name_words) >= 2:
            catalogue = " ".join(name_words[:2])
        elif name_words:
            catalogue = name_words[0]
        else:
            catalogue = "Chưa rõ"
        # Tạo ID sản phẩm
        id_product = f"SP{idx:02d}"
        # Thêm sản phẩm vào danh sách
        products.append({
            "id_product": id_product,
            "name_product": name_product.strip(),
            "cost": item["price"],
            "description": description.strip() if description else "Hàng chính hãng",
            "quantity": 100,
            "catalogue": catalogue
        })
    # Ghi danh sách sản phẩm ra file JSON
    with open("products.json", "w", encoding="utf8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    crawl_tiki_products()