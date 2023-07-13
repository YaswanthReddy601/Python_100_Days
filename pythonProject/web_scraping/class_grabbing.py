import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.geeksforgeeks.org/python-programming-language/")

soup = BeautifulSoup(req.text, "html.parser")

# print(soup.select(".Basics")[9].text)

# print(len(soup.select(".Basics")))
# x = soup.prettify()
# print(x)

for x in soup.select(".Basics"):
    print(x.text)

# print(soup.select(".Basics")[0].text)



