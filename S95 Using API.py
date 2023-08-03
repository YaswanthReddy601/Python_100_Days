import smtplib

import requests
from flask import Flask

app= Flask(__name__)
bars_info=""
@app.route("/get_data")
def get_data():
    response = requests.get("https://api.openbrewerydb.org/v1/breweries?by_name=cooper&per_page=3")
    data = response.json()
    bars_info= data[0]
    # print(response.text)
    print(data)
    return "data received"

@app.route("/send_mail")
def send_data():
    email="yaswanthreddy601@gmail.com"
    password="xjopskwqdorfbqnw"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, password)
        message="This is one of the top brewery in the town \n\n bars_info"
        connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject: Brewery\n\n {message}")
    return "Mail Sent"

if __name__ == "__main__":
    app.run()
