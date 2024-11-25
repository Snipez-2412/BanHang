from pymongo import MongoClient

uri = "mongodb+srv://tnchau23823:abc13579@cluster0.fs6jd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

db = client['my_database']
phone = db['phone']

db.phone.insert_one({
    "ten":"Redmi 13C",
    "hang":"Redmi",
    "title":"(Starfrost White, 6GB RAM, 128GB Storage) | Powered by 4G MediaTek Helio G85 | 90Hz Display | 50MP AI Triple Camera",
    "gia":"8.000.000 đồng",
    "url_image":"https://m.media-amazon.com/images/I/71scmEdSC2L._AC_UY218_.jpg",
})

docs = phone.find({"hang":"Redmi"})
for doc in docs:
    print(doc)
# redmi realme iphone oneplus