import os
import requests
from dotenv import load_dotenv
load_dotenv()
BASE_FLIGHT_URL= os.getenv("BASE_FLIGHT_URL")
FLIGHT_KEY= os.getenv("FLIGHT_KEY")
FLIGHT_SECRET= os.getenv("FLIGHT_SECRET")

class FlightSearch:
    def __init__(self):
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






















