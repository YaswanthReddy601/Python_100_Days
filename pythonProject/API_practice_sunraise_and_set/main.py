import requests
import datetime

parameteres={
    "lat" : 13.642765,
    "lng" : 78.809944
}

response = requests.get("https://api.sunrise-sunset.org/json")
response.raise_for_status()
data =response.json()
sunset = data["results"]["sunset"]
sunrise = data["results"]["sunrise"]

timee = datetime.datetime.now()
print(sunset)

print(timee)

