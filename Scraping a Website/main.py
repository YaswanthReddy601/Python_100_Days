import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://news.ycombinator.com/")
code = response.text

soup = BeautifulSoup(code, "lxml")
attributes = soup.select(".titleline")
# for x in attributes:
#     print(x.text)
# print(attributes)
# for x in attributes:
#     print(x.get("a"))\
text = []
data = soup.find_all(name="span", class_="titleline")
for x in data:
    text.append(x.text)
lin = []
links = soup.select("a")
for link in links:
    lin.append(link.get("href"))
vote = []
votes = soup.find_all(name="span", class_="score")
for x in votes:
    vote.append(int(x.getText().split()[0]))
# print(text)
# print(lin)
# print(vote)

max = max(vote)
ind = vote.index(max)
print(text[ind])





