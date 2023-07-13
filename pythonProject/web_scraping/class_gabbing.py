import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.javatpoint.com/")

soup = BeautifulSoup(req.text,"html.parser")



print(soup.select(".points")[0].text)
for x in soup.select(".points"):
    print(x.text)
