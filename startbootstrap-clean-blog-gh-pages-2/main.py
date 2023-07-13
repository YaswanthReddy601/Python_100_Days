from flask import Flask, render_template
import requests
app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route("/")
def home():
    return render_template("index.html", data = response)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/index/<int:id>")
def show_req_data(id):
    req_data = None
    for record in response:
        if record["id"] == id:
            req_data = record
    return render_template("post.html", data = req_data)


if __name__ == "__main__":
    app.run(debug=True)