import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()

API = os.getenv("API", "api")
URL = os.getenv("BASE_URL", "base")
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID","")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
TO = os.getenv("NUMBER_TO")
FROM = os.getenv("NUMBER_FROM")

LAT =  59.3286
LNG = 18.0553



# Skickar SMS via Twilio
def send_sms(message=""):
    client = Client(TWILIO_SID, TWILIO_TOKEN)

    message = client.messages.create(
        body=f"{message}",
        from_=FROM,
        to=TO,
    )
    print(message.body)



# Hämtar data från API
def get_api(url, params):
    response = requests.get(url, params)
    response.raise_for_status()
    data = response.json()
    return data



# Hämtar väderprognos och skickar SMS vid regn
def get_weather():
   params = {
        "lat":LAT,
        "lon":LNG,
        "cnt":4,
        "appid":API
    }

   weather = get_api(URL, params)
   rain_alert = [item for item in weather["list"] if int(item["weather"][0]["id"]) < 700 ]

   if len(rain_alert)>=1:
        send_sms(message="Its's going to rain today. Remember to bring an ☂️")
   else:

       print("No rain expected today. Enjoy your day! 🌤️")

get_weather()