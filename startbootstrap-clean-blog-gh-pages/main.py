import smtplib

from flask import Flask, render_template, request
import requests
app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route("/")
def home():
    return render_template("index.html", data = response)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/index/<int:id>")
def show_req_data(id):
    req_data = None
    for record in response:
        if record["id"] == id:
            req_data = record
    return render_template("post.html", data = req_data)

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        ph_number = request.form["phone"]
        message = request.form["message"]
        send_mail(name,email)

        return f"Hey {name} !, your details are received.\n you will get frequest mails to '{email}' about our blogs."
    return render_template("contact.html")

def send_mail(name,email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, "ads132dsfasdfeqre23")
        message = f"Hey {name} ! your details are received.\n you will get frequest mails to '{email}' about our blogs."
        connection.sendmail(from_addr=email, to_addrs=email, msg="Subject= From MyBlogs.com\n message")
if __name__ == "__main__":
    app.run(debug=True)