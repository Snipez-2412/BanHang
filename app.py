from flask import Flask, render_template, request, redirect, url_for, flash, session
from pymongo import MongoClient


app = Flask(__name__)
uri = "mongodb+srv://tnchau23823:abc13579@cluster0.fs6jd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
app.secret_key = 'key'  # Required for session management
db = client['my_database']
accounts = db['account']

@app.route('/')
def home():
    if 'user' in session:  # Check if a user is logged in
        return f"<h1>Hello, {session['user']}!<h1>"
    return "<h1>Hello! Please <a href='/login'>login</a>.<h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Authenticate user
        user = accounts.find_one({'username': username, 'password': password})
        if user:
            session['user'] = username  # Store the username in session
            flash('Login successful!', 'success')
            return redirect(url_for('home'))  # Redirect to the home page
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template("Login.html")

@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Thêm người dùng mới vào MongoDB
        if accounts.find_one({'username': username}):
            return render_template('SignUp.html', message='Tài khoản đã tồn tại')
        else:
            new_user = {'username': username,'email':email, 'password': password}
            accounts.insert_one(new_user)
            return render_template('SignUp.html', message='Đăng ký thành công!')
    return render_template('SignUp.html')
    

@app.route('/logout')
def logout():
    session.pop('user', None)  # Clear the session
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))  # Redirect to login page

if __name__ == "__main__":
    app.run(debug=True)
