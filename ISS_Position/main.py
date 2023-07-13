import smtplib
import time

import requests as requests
import datetime

# import requests

my_lat = 13.642765
my_long = 78.809944

def is_Iss_ovehead():
    response = requests.get(url= "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    if my_lat-5 <= iss_lat <=my_lat+5 and my_long-5 <= iss_long <=my_long+5:
        return True


parameters = {
    "lat" : my_lat,
    "lng" : my_long,
    "formatted" : 0
}

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.datetime.now().hour

    if time_now >= sunset or time_now <sunrise:
        return True

while True:
    time.sleep(60)
    if is_Iss_ovehead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login("yaswanthreddy600", "aadsfa")
            connection.sendmail(
                from_addr="yaswanthreddy600@gmail.com",
                to_addrs="yaswanthreddy601@gmail.com",
                msg= "Subject: Its time Look Up\n\n ISS is above you in the sky."
            )











