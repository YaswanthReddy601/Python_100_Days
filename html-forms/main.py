from flask import Flask, render_template, request

ap = Flask(__name__)

@ap.route("/")
def home():
    return render_template("index.html")

@ap.route("/login", methods=["POST"])
def login():
    name = request.form['name']
    passsword = request.form['password']
    return f"<h2><b>name is {name} and password is {passsword}</b></h2>"

if __name__ == "__main__":
    ap.run()