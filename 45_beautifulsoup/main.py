import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/").text
soup = BeautifulSoup(response, "html.parser")

# movies_raw = soup.select(selector="#__next > main > article > div.article_article-content__3auQJ.false")
# movies = [movie.get_text() for movie in movies_raw[0].select(selector="span h2 strong")]

selection = soup.find_all(name="h2")[1:]
movies = [movie.get_text() for movie in selection]

try:
    open("movies.txt", 'r')
except FileNotFoundError:
    with open("movies.txt", 'w') as file:
        file.write("\n".join(movies[::-1]))
