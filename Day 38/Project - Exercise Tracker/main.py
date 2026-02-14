import os
from dotenv import load_dotenv
load_dotenv()
import requests
import datetime as dt

BASE_URL = os.getenv("BASE_URL")
EXCEL_URL = os.getenv("EXCEL_URL")
APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
EXCEL_KEY = os.getenv("EXCEL_KEY")

TODAY = dt.datetime.now().strftime("%d/%m/%Y")
TIME = dt.datetime.now().strftime("%H:%M:%S")

WEIGHT = 80
HEIGHT=185
AGE=30
GENDER= "male"



# Hämtar data från API
def post_data(url, headers=None, params=None):
    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()



# Sparar träningsdata i Google Sheets(Sheety API)
def save_exercise_to_sheet(exercise_data):
    headers = {
        "Authorization": EXCEL_KEY
    }

    params ={
    "page1": {
        "date": TODAY,
        "time": TIME,
        "exercise":exercise_data["user_input"] ,
        "duration": exercise_data["duration_min"],
        "calories": exercise_data["nf_calories"] }


}

    res = post_data(EXCEL_URL,headers=headers,params=params)
    print(res["page1"])


# Tar emot användarinput, anropar nutrition-api för att beräkna pass och få träningsdetaljer
def track_exercise():
    """
     Running/Jogging - "ran for 30 minutes", "jogged 2 miles"
     Swimming - "swam for 1 hour", "swimming laps"
     Walking - "walked 3 miles", "brisk walk 45 min"
     Cycling - "biked for 1 hour", "rode bike 10 miles"
     Weightlifting - "lifted weights 45 min", "weight training"
    """

    exercise_text = input("Tell me which exercises you did: ")


    headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY
    }
    params = {
    "query": exercise_text,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER
    }

    response = post_data(BASE_URL,headers=headers, params=params)
    exercise_data =  response["exercises"][0]
    save_exercise_to_sheet(exercise_data)

track_exercise()


