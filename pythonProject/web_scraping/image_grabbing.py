import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.javatpoint.com/hadoop-tutorial")

soup = BeautifulSoup(res.text,"html.parser")

x = soup.select("img")[0]

print(x["src"])

image = requests.get("https://static.javatpoint.com/images/logo/jtp_logo.png")

print(image.content)

file = open("java_point_image.jpg", "wb")
file.write(image.content)
file.close()


