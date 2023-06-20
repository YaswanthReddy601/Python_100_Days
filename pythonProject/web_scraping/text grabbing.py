import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.javatpoint.com/")

soup = BeautifulSoup(data.text,"html.parser")

# x = soup.p
#returns only first indexed element
# print(x)

# print(soup.select("title"))
# print(soup.select("p"))
# print(soup.select("p")[5].get_text())
# print(len(soup.select("a")))

print(soup.select("a")[100])
