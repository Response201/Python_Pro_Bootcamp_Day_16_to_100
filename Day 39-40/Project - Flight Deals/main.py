import os
from pprint import pprint
import requests
from dotenv import load_dotenv
from flight_search import FlightSearch
from flight_data import FlightData
import json
load_dotenv()
EXCEL_URL = os.getenv("EXCEL_URL")
EXCEL_KEY = os.getenv("EXCEL_KEY")

def get_data(url, headers=None, params=None):
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_data_google_sheet():
    data = get_data(EXCEL_URL)
    with open("sheet_data", mode="w") as file:
        json.dump(data["prices"], file, indent=4)
    return data



def get_exel_data():
    try:
        with open("sheet_data", mode="r") as file:
            # Hämtar fil
            find_data = json.load(file)

        # Om filen inte finns skapas en ny fil och en post med infon
    except FileNotFoundError:
       get_data_google_sheet()

    else:
        return find_data



flight_data = FlightData()
flight_data.find_cheapest_flight()


def update_exel():

    data = get_exel_data()

    for row in data:
        city = row["city"].upper()

        iataCode = flight_data.get_destination_info(city)

        body = {
            "price": {
                "iataCode":iataCode["data"][0]["iataCode"],
            }
        }

        requests.put(f"{EXCEL_URL}/{row["id"]}",  json=body)
        get_data_google_sheet()


#update_exel()



