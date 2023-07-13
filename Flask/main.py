from flask import Flask

app = Flask(__name__)
# print(__name__)
@app.route("/")
def hello():
    return "Hello World"

@app.route("/name/<name>")
def hai(name):
    return f"hai {name}"



if __name__ == "__main__":
    app.run()
