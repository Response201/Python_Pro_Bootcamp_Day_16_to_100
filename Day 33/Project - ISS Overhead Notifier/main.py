import datetime as dt
import smtplib
import requests
from dotenv import load_dotenv
import os
import time

#Laddar in variabler från env-fil
load_dotenv()
my_password = os.getenv("PASSWORD", "my_test_password")
my_email =  os.getenv("EMAIL", "my_test_email")
to_email =os.getenv("TO_EMAIL", "to_email")
api_url = os.getenv("API_URL", "api_url")
api_sunrise = os.getenv("API_URL_SUNRISE", "api_sunrise")

# Plats koordinater
LAT = 59.3286
LNG = 18.0553



# Skapar SMTP-anslutning och skickar mail
def send_mail():
    with   smtplib.SMTP("smtp.gmail.com", 587) as con:
        con.starttls()
        con.login(user=my_email, password=my_password)
        con.sendmail(from_addr=my_email,to_addrs=to_email, msg = " Look up! \n The satellite is passing over your location now")

        con.close()


# Hämtar data från API
def get_data(url, param=None):
    response = requests.get(url, params=param)
    response.raise_for_status()
    return response.json()


# Kollar om satelliten är över platsen
def satellit_over_location():
    # Hämtar satellitens position
    satellit_loc = get_data(api_url)
    satellit_lng = float(satellit_loc["iss_position"]["longitude"])
    satellit_lat = float(satellit_loc["iss_position"]["latitude"])

    # Returnerar True om satelliten är inom koordinatområdet(+/- 5) för platsen
    return  LAT - 5 <=  satellit_lat <=  LAT + 5 and LNG - 5 <= satellit_lng  <= LNG + 5



# Kollar om det är natt
def is_night():
    # Hämtar timme för soluppgång och solnedgång
    sun_data = get_data(api_sunrise, param={'lat': LAT, 'lng': LNG, 'formatted': 0})
    sunrise_hour = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    hour_now = dt.datetime.now().hour

    # Returnerar True om nuvarande timme är före soluppgång eller efter solnedgång
    return hour_now < sunrise_hour or hour_now > sunset_hour




while True:
    # Skicka mail om det är natt och satelliten passerar över området
    if is_night() and satellit_over_location():
        send_mail()

    # Vänta 5 minuter innan nästa kontroll
    time.sleep(300)