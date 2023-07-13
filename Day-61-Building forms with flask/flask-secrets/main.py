from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from formswtf import MyForm

#creating flask
app = Flask(__name__)

#using bootsstrap flask as an inherited template
bootstrap = Bootstrap5(app)
app.config["SECRET_KEY"] = 'HELLO'
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/form", methods=['GET', 'POST'])
def login():
    form = MyForm()
    #receiving form data
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form )


if __name__ == '__main__':
    app.run(debug=True)
