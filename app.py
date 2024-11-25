from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello<h1>"

@app.route('/<name>')
def user(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run()