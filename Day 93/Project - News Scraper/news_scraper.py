import os
import csv
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

filename = "top_5_positive_news.csv"
data = []




def get_articels():
    get_new_articles()
    articles = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                articles.append(row)
        return articles
    except:
        return []






def save_articles(data):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["titel", "image", "date", "url"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)





def get_new_articles():
    steam_url = os.getenv("NEWS_URL")
    response = requests.get(steam_url)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("div", class_="gallery-item-container")

    for item in items:
        title_tag = item.find("h2")
        if not title_tag:
            continue

        title = title_tag.get_text(strip=True)

        if not title.startswith("Goda nyheter"):
            continue

        imgs = item.find_all("img")
        image = imgs[1]["src"] if len(imgs) > 1 else None

        time_tag = item.find(class_="time-ago")
        date = time_tag.get_text(strip=True).replace(".", "") if time_tag else None

        link_tag = item.find("a", href=True)
        url = link_tag["href"] if link_tag else None

        data.append({
            "titel": title,
            "image": image,
            "date": date,
            "url": url
        })
    if len(data) >= 6:
        save_articles(data[:6])




