"""
from bs4 import BeautifulSoup
import  requests
from operator import itemgetter
from pprint import pprint
import lxml

with open("index.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.string)

all_links = soup.find_all("a")

for item in all_links:
    print(item.getText())
    print(item.get("href"))
heading = soup.find(name="h1", id="name")
print(heading.string)
heading = soup.find(name="h3", class_="heading")
print(heading.getText())
spec_link = soup.select_one(selector="p em a")
print(spec_link)
name = soup.select_one(selector="h3.heading")
print(name)
 Scraping a Live Website

try:
    url = "https://news.ycombinator.com/news"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

except requests.RequestException as e:
    print("Error", e)
else:

    titel = soup.find_all("span", class_="titleline")

    rank_list = soup.find_all("span", class_="rank")

    score_list = soup.find_all("span", class_="score")

    array = []

    for item in range(len(rank_list)):

        rank = rank_list[item].getText()
        link = titel[item].select_one("a").getText()
        href = titel[item].select_one("a").get("href")
        score = score_list[item].getText()
        array.append({"rank": rank, "title":link,"link":href, "points": int(score.split(" ")[0])})

    print(array)
    array.sort(key=itemgetter("points"), reverse=True)
    max_score = array[0]
    print(f"Max score: {max_score}")

"""