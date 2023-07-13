from bs4 import BeautifulSoup
import requests


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text
soup = BeautifulSoup(data, "html.parser")
big_data = soup.find_all(name="h3", class_="title")
movies_100 = [data.getText() for data in big_data]
# for movie in movies_100[::-1]:
#     print(movie)

with open("Top 100 movies.txt","w", encoding="UTF-8") as file:
    for movie in movies_100[::-1]:
        file.write(f"{movie}\n")

