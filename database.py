from pymongo import MongoClient

# Hàm kết nối tới MongoDB
def get_db():
    client = MongoClient("mongodb+srv://tnchau23823:abc13579@cluster0.fs6jd.mongodb.net/?retryWrites=true&w=majority")
    db = client['my_database']
    return db

# Thêm sản phẩm vào MongoDB (chạy khi cần thêm sản phẩm mẫu)
def insert_sample_product():
    db = get_db()
    phone_collection = db['phone']
    phone_collection.insert_one({
        "ten": "Redmi Note 13 Pro+",
        "hang": "Redmi",
        "title": "Redmi Note 13 Pro+ (Fusion Black, 8GB RAM, 256GB Storage) | World's First Mediatek 7200 Ultra 5G | 200MP Hi-Res Camera | 1.5K Curved AMOLED | 120W HyperCharge",
        "gia": "10.000.000 đồng",
        "url_image": "https://m.media-amazon.com/images/I/71nrf4zgq5L._AC_UY218_.jpg",
    })
