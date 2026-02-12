import os
from dotenv import load_dotenv
load_dotenv()
import datetime as dt
import request_handler as req

BASE_URL = os.getenv("BASE_URL")
PIXE_TOKEN = os.getenv("PIXE_TOKEN")
PIXE_USERNAME=os.getenv("PIXE_USERNAME")
PIXE_GRAPH = os.getenv("PIXE_GRAPH")
GRAPH_ENDPOINT = f"{BASE_URL}/{PIXE_USERNAME}/graphs/{PIXE_GRAPH}"
TODAY = dt.datetime.now().strftime("%Y%m%d")
HEADERS = {"X-USER-TOKEN": PIXE_TOKEN}




# Skapa användare
def create_user():
    params = {
        "token": PIXE_TOKEN,
        "username": PIXE_USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    req.post_data(BASE_URL,None, params)




# Skapa graf
def create_graph():
    params = {
        "id": PIXE_GRAPH,
        "name": "My Happy Graph",
        "unit": "commit",
        "type": "int",
        "color": "ichou"
    }
    url = f"{BASE_URL}/{PIXE_USERNAME}/graphs"

    req.post_data(url,headers=HEADERS,params=params)




# Hämta statistik för graf
def get_graph_stats():
    url =f"{GRAPH_ENDPOINT}/stats"
    response = req.get_data(url)
    print(response.text)

#get_graph_stats()




# Skapa pixel i graf
def create_pixel_graph():
    params = {
        "date": TODAY,
         "quantity" : input("On a scale from 1 to 10, how happy are you today? 😊\n")
    }
    url = f"{GRAPH_ENDPOINT}"

    req.post_data(url,headers=HEADERS,params=params)

#create_pixel_graph()




# Uppdatera pixel i graf
def update_pixel_graph():
    params = {
        "quantity":input(f"Would you like to update your happiness rating? Enter a number (1–10): 😊\n")
    }
    url = f"{GRAPH_ENDPOINT}/{TODAY}"

    req.put_data(url,headers=HEADERS,params=params)

#update_pixel_graph()




# Ta bort pixel i graf
def delete_pixel_graph():
    url = f"{GRAPH_ENDPOINT}/{TODAY}"

    req.delete_data(url, headers=HEADERS)

#delete_pixel_graph()