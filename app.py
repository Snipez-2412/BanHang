from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'key'  # Required for session management

# Mock user database
users = {
    "huy": "huy1234"  # username: password
}

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
        if username in users and users[username] == password:
            session['user'] = username  # Store the username in session
            flash('Login successful!', 'success')
            return redirect(url_for('home'))  # Redirect to the home page
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template("Login.html")

@app.route('/signup')
def signup():
    return render_template("SignUp.html")

@app.route('/logout')
def logout():
    session.pop('user', None)  # Clear the session
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))  # Redirect to login page

if __name__ == "__main__":
    app.run(debug=True)
