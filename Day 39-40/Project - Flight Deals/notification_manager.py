import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
NUMBER_TO=os.getenv("NUMBER_TO")
NUMBER_FROM=os.getenv("NUMBER_FROM")



class NotificationManager():

    def __init__(self):
       super().__init__()
       self.client = Client(TWILIO_SID,TWILIO_TOKEN)

    # Skapar och skickar SMS
    def send_sms(self):
        create_message = f"✈️ {self.origin_airport} → {self.destination_airport} \n| Price: {self.price} EUR |\n| Departure: {self.departure_date} {self.departure_time} |"

        #message = self.client.messages.create(
        #    body=f"{message}",
        #    from_=NUMBER_FROM,
        #    to=NUMBER_TO,
        #)
        #print(message.body)
        print(create_message)
