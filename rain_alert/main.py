import smtplib
import time

import requests

owm_url = "https://api.openweathermap.org/data/2.5/weather"
key = "4c1c6013aa0f6302deef4eaf56517924"
parameters= {
    "lat": 13.642765,
    "lon": 78.809944,
    "appid": key,
    # "exclude": "current,minutely,dailt"
}
# for x in range(1,12):
response = requests.get(owm_url, params= parameters)
status = response.status_code
data = response.json()
weather_code = data["weather"][0]["id"]
# time.sleep(3600)
if weather_code < 500:
    email= "yaswanthreddy600@gmail.com"
    password="xjopskwqdorfbqnw"
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(email,password)
        message ="Subject: Weather Forcast\n\n Its raining out side."
        conn.sendmail(from_addr=email, to_addrs=email, msg= message)



