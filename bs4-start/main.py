from bs4 import BeautifulSoup
import lxml
with open("website.html",encoding="utf8") as file:
    data = file.read()

soup = BeautifulSoup(data, "lxml")
# print(soup.prettify())
# print(soup.title.text)
# print(soup.title.string)
#
# print(soup.p.text)

# a_tags = soup.find_all("a")
# print(a_tags)
# for a_tags in soup.find_all("a"):
#     print(a_tags.get("href"))
#
# x = soup.find_all(name="h1", id="name")
# print(x)

x = soup.find(name="h3", class_="heading")
# print(x)
print(x.getText())
print(x.name)

a = soup.select("p a")
print(a)

id = soup.select("#name")
for x in id:
    print(x.getText())

clas = soup.select(".heading")
print(clas)
for x in clas:
    print(x.getText())

print(soup.find_all("a"))
