import requests
from operator import itemgetter
import json
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Hämtar filmlistan från webbsidan och returnerar den som en sorterad lista med rank och titel
def get_film_list():

    try:
        response = requests.get(URL)
        response.raise_for_status()

    except requests.RequestException as e:
        print("Error", e)

    else:
        soup = BeautifulSoup(response.text,  "html.parser")
        film_list = soup.find_all("div", class_="article-title-description__text")

        raw_film_list =[]
        for film in film_list:
            rank = film.select_one("h3", class_="title").getText()

            film_rank = int(rank.split(" ")[0].replace(")","").replace(":",""))
            film_title = " ".join(rank.split(" ")[1:])

            raw_film_list.append({"rank": film_rank, "film": film_title})

        sorted_film_list = sorted(raw_film_list, key=itemgetter("rank"))
        return sorted_film_list



# Laddar den sorterade filmlistan från fil om den finns, annars skapas och spara den
def get_sorted_film_list():

    try:
        with open("sorted_film_list.txt", mode="r") as file:
            film_list = json.load(file)
    except FileNotFoundError:
        film_list = get_film_list()
        with open("sorted_film_list.txt", "w") as file:
            json.dump(film_list, file, indent=4)

    print(film_list)


get_sorted_film_list()

