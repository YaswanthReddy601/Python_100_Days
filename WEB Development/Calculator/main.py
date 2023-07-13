from flask import Flask, render_template

app = Flask(__name__)

app.route("/")
def home():

    return render_template("templates/calculator.html")

app.route("/abc")
def al():
    print("x")
    return render_template("calculator.html")



if __name__ == '__main__':
    app.run()

