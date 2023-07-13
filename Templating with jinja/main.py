import datetime
import random

from flask import Flask, render_template

app = Flask(__name__)

now = datetime.datetime.now().year
rand = random.randint(0, 9)

@app.route('/')
def home():
    return render_template("index.html", year = now, number = rand)


if __name__ == "__main__":
    app.run(debug=True)


