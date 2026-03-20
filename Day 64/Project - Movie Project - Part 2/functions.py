import requests
import os
from dotenv import load_dotenv
load_dotenv()


def get_data(url, params=None):
    headers = {
        "accept": "application/json",
        "Authorization": os.getenv("MOVIE_KEY")
    }
    get_url = f"{os.getenv('BASE_URL')}/{url}"
    response = requests.get(get_url, headers=headers, params=params)
    return response.json()

