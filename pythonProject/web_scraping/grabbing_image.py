import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.facebook.com/")
data  = BeautifulSoup(req.content, "html.parser")

# print(data.text)

x = data.select("img")[0]
print(x["src"])

image = requests.get("https://static.xx.fbcdn.net/rsrc.php/y8/r/dF5SId3UHWd.svg")

file = open("Facebook_Logo", "wb")
file.write(image.content)
file.close()