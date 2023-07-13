from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>"+ function() +"</b>"
    return wrapper
def make_italic(function):
    def wrapper():
        return "<i>"+function()+"</i>"
    return wrapper
def make_underline(function):
    def wrapper():
        return "<u>"+function()+"</u>"
    return wrapper

def center(function):
    def wrapper():
        return "<center>"+function()+"</center>"
    return wrapper
@app.route("/hai")
@make_bold
@make_italic
@make_underline
@center
def hello():
    return "hai " \
           "hello"

if __name__ == "__main__":
    app.run()



