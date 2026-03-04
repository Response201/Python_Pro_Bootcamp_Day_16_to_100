from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
load_dotenv()


class PropertyScraper:
    def __init__(self):
        self.soup = BeautifulSoup(self.fetch_html(), "html.parser")
        self.properties = []

    # Hämtar HTML från sidan
    def fetch_html(self):
        try:
            response = requests.get(os.getenv("RENT_LINK"))
            response.raise_for_status()
            return response.text

        except requests.RequestException as error:
            print("fail:", error)


    # Hämtar bostadsannonser från sidan och sparar de fem första
    def scrape_properties(self):

        properties = [{"rent":item.find("span", class_="PropertyCardWrapper__StyledPriceLine").getText().replace("$", "").replace("+", "").replace("/mo", "").split(" ")[0],
                          "adress":item.find("a", class_="StyledPropertyCardDataArea-anchor").getText().replace("  ","").replace("\n", ""),
                          "link": item.find("a", class_="StyledPropertyCardDataArea-anchor").get("href")}
                         for item in self.soup.find_all("article",role="presentation")]

        if len(properties) >= 1:
            self.properties = properties[:5]

