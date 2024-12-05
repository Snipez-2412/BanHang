from pymongo import MongoClient

uri = "mongodb+srv://tnchau23823:abc13579@cluster0.fs6jd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

db = client['my_database']
phone = db['phone']

db.phone.insert_one({
    "ten":"Oneplus Nord CE4",
    "hang":"OnePlus",
    "title":"Oneplus Nord CE4 (Celadon Marble, 8GB RAM, 128Gb Storage)",
    "gia":"10.500.000 đồng",
    "url_image":"https://m.media-amazon.com/images/I/61nxQ62qglL._AC_UY218_.jpg",
})
print("Thanh công")

# docs = phone.find({"hang":"Realme"})
# for doc in docs:
#     print(doc)
# redmi realme iphone oneplus