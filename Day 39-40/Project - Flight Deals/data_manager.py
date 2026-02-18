import os
import requests
from dotenv import load_dotenv
load_dotenv()
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import json
from fallback_data import users_fallback, price_fallback

EXCEL_URL = os.getenv("EXCEL_URL")
EXCEL_KEY = os.getenv("EXCEL_KEY")


class DataManager(FlightSearch, FlightData, NotificationManager):
    def __init__(self):
        super().__init__()

        self.data_prices = self.get_exel_data( key="prices", fallback=price_fallback)
        self.data_users = self.get_exel_data(key="users", fallback=users_fallback)


    # Hämtar data från Google Sheet, fallback till defaultdata, sparar till self.data
    def get_data_google_sheet(self,key, fallback):
        try:
            response = requests.get(f"{EXCEL_URL}/{key}")
            response.raise_for_status()
            get_data = response.json()
            data = get_data[key]

        except requests.RequestException:
            data = fallback

        with open(f"{key}_data.txt", mode="w") as file:
            json.dump(data, file, indent=4)

        return data


    # Läser lokal excel-fil, skapar fil om den saknas
    def get_exel_data(self,  key, fallback):
        try:
            with open(f"{key}_data.txt", mode="r") as file:
               data =  json.load(file)

        except FileNotFoundError:
              data =  self.get_data_google_sheet(key, fallback)

        return data



    # Uppdaterar pris för en rad i Google Sheet och synkroniserar lokalt
    def update_exel(self, key="prices", row_id=None, new_price=None):
        try:
            body = {
                "price": {
                    "lowestPrice": new_price,
                }
            }

            response = requests.put(f"{EXCEL_URL}/{key}/{row_id}", json=body)
            response.raise_for_status()
        except requests.RequestException:
            print(f"Failed to update Google Sheet")

        # Uppdaterar alltid den lokala filen
        self.update_local_exel(key, row_id, new_price)



    # Uppdaterar pris för en rad i den lokala filen
    def update_local_exel(self , key="prices" , row_id=None, new_price=None):

        data = self.get_exel_data(key, price_fallback)

        for row in data:
            if row["id"] == row_id:
                row["lowestPrice"] = new_price


        with open(f"{key}_data.txt", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        self.data_prices = data
        print(f"Local file updated: id: {row_id}, new price: {new_price}\n")







