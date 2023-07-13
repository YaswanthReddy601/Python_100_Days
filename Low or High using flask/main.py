import random
from flask import Flask

app = Flask(__name__)

rand_number = random.randint(0, 9)
print(rand_number)
@app.route("/")
def home():
    return "<h2> <b> guess a number between 0-9 and enter at the end of the url </b> </h2> " \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:number>")
def guess(number):
    if number > rand_number:
        return "<h2> <b> Your Guess in higher </b> </h2> " \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif number < rand_number:
        return "<h2> <b> Your Guess in lower </b> </h2> " \
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h2> <b> Your Guess is correct </b> </h2> " \
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run()


