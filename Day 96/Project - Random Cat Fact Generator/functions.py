import requests


def get_data(url=""):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:

        print("Request error:", e)
        return None


