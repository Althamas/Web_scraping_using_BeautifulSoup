from bs4 import BeautifulSoup
import requests
import re
responds = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web = responds.text

soup = BeautifulSoup(web, "html.parser")

top_100 = soup.find_all(name="h3", class_="title")
movies = [movie.getText() for movie in top_100]

movies = movies[::-1]
print(movies)

with open("top_100.txt", "w") as file:
    for i in movies:
        i_2 = re.sub('[^a-zA-Z0-9 \n\.]', '', i)
        file.write(f"{i_2}\n")
