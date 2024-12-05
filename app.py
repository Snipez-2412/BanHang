from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Kết nối đến MongoDB
client = MongoClient("mongodb+srv://tnchau23823:abc13579@cluster0.fs6jd.mongodb.net/?retryWrites=true&w=majority")
db = client['my_database']
phone_collection = db['phone']

# Route để hiển thị danh sách sản phẩm
@app.route('/')
def index():
    # Lấy danh sách sản phẩm từ MongoDB
    products = phone_collection.find()
    return render_template('product_list.html', products=products)

# Route để thêm sản phẩm mới
@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Lấy thông tin từ form
        name = request.form.get('name')
        price = request.form.get('price')
        description = request.form.get('description')
        
        # Thêm vào MongoDB
        phone_collection.insert_one({
            "name": name,
            "price": float(price),
            "description": description
        })
        return redirect(url_for('index'))  # Quay lại trang danh sách sản phẩm
    
    return render_template('add_product.html')  # Hiển thị form thêm sản phẩm

# Route để xóa sản phẩm
@app.route('/delete/<product_id>', methods=['POST'])
def delete_product(product_id):
    # Xóa sản phẩm dựa trên ID
    phone_collection.delete_one({"_id": ObjectId(product_id)})
    return redirect(url_for('index'))  # Quay lại trang danh sách sản phẩm

# Route để cập nhật sản phẩm
@app.route('/edit/<product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = phone_collection.find_one({"_id": ObjectId(product_id)})  # Tìm sản phẩm theo ID
    
    if request.method == 'POST':
        # Lấy thông tin chỉnh sửa từ form
        name = request.form.get('name')
        price = request.form.get('price')
        description = request.form.get('description')
        
        # Cập nhật sản phẩm trong MongoDB
        phone_collection.update_one(
            {"_id": ObjectId(product_id)},
            {"$set": {"name": name, "price": float(price), "description": description}}
        )
        return redirect(url_for('index'))  # Quay lại trang danh sách sản phẩm
    
    return render_template('edit_product.html', product=product)  # Hiển thị form chỉnh sửa sản phẩm

if __name__ == '__main__':
    app.run(debug=True)
