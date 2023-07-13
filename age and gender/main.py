from flask import Flask, render_template
import requests

app = Flask(__name__)

# @app.route("/guess/<name>")
# def home(name):
#     response1 = requests.get(f"https://api.genderize.io/?name={name}")
#     code1 = response1.json()
#     gender = code1["gender"]
#     response2 = requests.get(f"https://api.agify.io/?name={name}")
#     code2 = response2.json()
#     age = code2["age"]
#     return render_template("index.html",name = name, gender = gender, age = age)

@app.route("/blogs")
def blogs():
    response = requests.get("https://api.npoint.io/fe6a06faa06d4210083f")
    data = response.json()
    return render_template("index.html", data= data)



if __name__ == "__main__":
    app.run()

