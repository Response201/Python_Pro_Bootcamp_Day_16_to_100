import os
import requests
from dotenv import load_dotenv
load_dotenv()
from flight_data import FlightData

BASE_FLIGHT_URL= os.getenv("BASE_FLIGHT_URL")
FLIGHT_KEY= os.getenv("FLIGHT_KEY")
FLIGHT_SECRET= os.getenv("FLIGHT_SECRET")
OFFERS_FLIGHT_URL = os.getenv("OFFERS_FLIGHT_URL")

class FlightSearch(FlightData):
    def __init__(self):
        super().__init__()
        self._api_key = FLIGHT_KEY
        self._api_secret = FLIGHT_SECRET
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            'client_id': FLIGHT_KEY,
            'client_secret': FLIGHT_SECRET
        }
        response = requests.post(f"{BASE_FLIGHT_URL}/security/oauth2/token", headers=header, data=body)
        response.raise_for_status()
        data = response.json()
        return  data["access_token"]

    # Hämtar detaljerad information om en stad från API: namn, IATA-kod och land
    def get_destination_info(self, city):
        header = {"Authorization": f"Bearer {self._token}"}
        params = {
            "keyword": city,
        }

        response = requests.get(
            f"{BASE_FLIGHT_URL}/reference-data/locations/cities",
            headers=header,
            params=params,
        )
        response.raise_for_status()
        data = response.json()
        return data




    # Hittar flygresor
    def check_flights(self):

       token = self._token
       from_date = self.departure_date
       to_date = self.return_date

       params = {
            "originLocationCode": self.origin_airport,
            "destinationLocationCode": self.destination_airport,
            "departureDate": from_date,
            "returnDate": to_date,
            "adults": 1,
            "nonStop": "true" if self.is_direct else "false",
            "max": 7
        }
       headers = {
           "Authorization": f"Bearer {token}"
       }
       try:
            response = requests.get(OFFERS_FLIGHT_URL, headers=headers, params=params)
            data = response.json()
            response.raise_for_status()
       except requests.RequestException as e:
            print(f" error:{e}")
       else:
            self.find_cheapest_flight(data["data"])




























