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
       self.price = "N/A"
       self.origin_airport = "N/A"
       self.destination_airport = "N/A"
       self.departure_time="N/A"
       self.departure_date = (dt.datetime.now() + dt.timedelta(days=7)).strftime("%Y-%m-%d")
       self.return_date = (dt.datetime.now() + dt.timedelta(days=30)).strftime("%Y-%m-%d")



    # Hittar den billigaste flygresan och uppdaterar pris och avgångstid
    def find_cheapest_flight(self):

       token = self._token
       from_date = self.departure_date
       to_date = self.return_date

       params = {
            "originLocationCode": self.origin_airport,
            "destinationLocationCode": self.destination_airport,
            "departureDate": from_date,
            "returnDate": to_date,
            "adults": 1,
            "max": 5
        }
       headers = {
           "Authorization": f"Bearer {token}"
       }

       response = requests.get(OFFERS_FLIGHT_URL, headers=headers, params=params)
       data = response.json()

       if len(data["data"]) >= 1:
             for item in range(len(data)):
                 if  self.price == "N/A" or float(data["data"][item]["price"]["total"]) and float(data["data"][item]["price"]["total"]) < self.price:
                         self.price = float(data["data"][item]["price"]["total"])
                         date = data["data"][item]["itineraries"][0]["segments"][0]["departure"]["at"]
                         self.departure_time = date.split("T")[1][:5]

       else:
                print(f"No flights: {self.origin_airport} - {self.destination_airport} ")








