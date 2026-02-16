import os
import requests
from dotenv import load_dotenv
import datetime as dt
from flight_search import FlightSearch
load_dotenv()
OFFERS_FLIGHT_URL = os.getenv("OFFERS_FLIGHT_URL")


class FlightData(FlightSearch):
    def __init__(self):
       super().__init__()
       self.price = 0
       self.price = "N/A"
       self.origin_airport = "N/A"
       self.destination_airport = "N/A"
       self.out_date = "N/A"


    def find_cheapest_flight(self):
        token = self._token


        params = {
            "originLocationCode": "MAD",
            "destinationLocationCode": "PAR",
            "departureDate": (dt.date.today() + dt.timedelta(days=7)).isoformat(),
            "adults": 1,
            "max": 5
        }

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(OFFERS_FLIGHT_URL, headers=headers, params=params)
        response.raise_for_status()
        print(response.json())
        data = response.json()
        if len(data) >= 1:




            self.price = data["data"][0]["price"]["total"]
            self.origin_airport = "departure"
            self.destination_airport = "destination"
            self.out_date = data["data"][0]["itineraries"][0]["segments"][0]["departure"]["at"]

            print(  self.price ,
            self.origin_airport,
            self.destination_airport,
            self.out_date )






