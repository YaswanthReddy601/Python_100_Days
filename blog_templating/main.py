import requests
from flask import Flask, render_template


app = Flask(__name__)
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
code = response.json()
@app.route('/')
def home():
    return render_template("index.html", code = code)

@app.route("/data/<int:index>")
def get_all_data(index):
    data = None
    for record in code:
       if record["id"] == index:
            data = record
    return render_template("post.html", data = data)

if __name__ == "__main__":
    app.run(debug=True)


