import os
import requests
from twilio.rest import Client
import test_data
from dotenv import load_dotenv
load_dotenv()


STOCK = os.getenv("STOCK")
STOCK_KEY = os.getenv("STOCK_KEY")
COMPANY_NAME = os.getenv("COMPANY_NAME")
STOCK_ENDPOINT =os.getenv("STOCK_ENDPOINT")
NEWS_ENDPOINT = os.getenv("NEWS_ENDPOINT")
NEWS_KEY = os.getenv("NEWS_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
FROM = os.getenv("NUMBER_FROM")
TO = os.getenv("NUMBER_TO")



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
def get_data(url, params):

    response = requests.get(url, params)
    response.raise_for_status()
    data = response.json()
    return data



# Hämtar nyheter och skapar meddelande
def get_stock_news(from_date, to_date, change_pct):

   params = {
    "q":COMPANY_NAME,
    "from":from_date,
    "to": to_date,
    "pageSize":3,
    "apiKey": NEWS_KEY,
    }

   # Hämtar nyhetsdata från testdata eller API
   articles = test_data.news_data
   # articles = get_data(NEWS_ENDPOINT, params)


   # Går igenom varje artikel och skickar sms
   for item in articles["articles"]:
       message = ""
       if item["title"] :
           message += f"Headline: {item['title']}\n"
       if item["description"]:
           message += f"Brief: {item['description']}"
       if message != "":
            emoji = "🔻" if change_pct < 0 else "🔺"
            send_sms(f"{COMPANY_NAME}: {abs(change_pct)}% {emoji}\n{message}")





# Beräknar procentuell förändring mellan senaste öppningspris och föregående dags stängningspris
def check_stock_change():
    params ={
        "function": "TIME_SERIES_DAILY",
        "symbol" : STOCK,
        "apikey" : STOCK_KEY
    }

    # Hämtar aktiedata från testdata eller API
    data = test_data.stock_data
    #data =  get_data(STOCK_ENDPOINT, params)

    # Tar de två senaste dagarnas aktiedata
    stock_data = list(data["Time Series (Daily)"].items())[:2]

    # Senaste datum och pris vid öppning
    open_stock_date = stock_data[0][0]
    open_stock_price = float(stock_data[0][1]["1. open"])

    # Föregående datum och pris vid stängning
    close_stock_date = stock_data[1][0]
    close_stock_price = float(stock_data[1][1][ "4. close"])

    # Räknar ut procentuell förändring mellan öppning och stängning
    change_pct = round((open_stock_price - close_stock_price) / close_stock_price * 100 )

    # Hämtar nyheter om förändringen är 1% eller mer
    if abs(change_pct) >= 1:
        get_stock_news(close_stock_date, open_stock_date, change_pct)




check_stock_change()
