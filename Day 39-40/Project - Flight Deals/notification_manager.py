import os
from twilio.rest import Client
import smtplib
from dotenv import load_dotenv
load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
NUMBER_TO=os.getenv("NUMBER_TO")
NUMBER_FROM=os.getenv("NUMBER_FROM")
EMAIL_KEY = os.getenv("PASSWORD", "my_test_password")
EMAIL_FROM =  os.getenv("EMAIL", "my_test_email")


class NotificationManager():

    def __init__(self):
       super().__init__()
       self.client = Client(TWILIO_SID,TWILIO_TOKEN)

    # Skapar och skickar SMS
    def send_sms(self):
        create_message = (f"\n✈️ {self.origin_airport} → {self.destination_airport} \n| Price: {self.price} EUR |\n"
                          f"| Stops: {self.stops}  |\n"
                          f"| Departure: {self.departure_date} {self.departure_time} |\n")

        #message = self.client.messages.create(
        #    body=f"{message}",
        #    from_=NUMBER_FROM,
        #    to=NUMBER_TO,
        #)
        #print(message.body)
        print(create_message)




    # Skapar och skickar email
    def send_mail(self):
        with   smtplib.SMTP("smtp.gmail.com", 587) as con:
            con.starttls()
            con.login(user=EMAIL_FROM, password=EMAIL_KEY)

            create_message = (f"\n{self.origin_airport} - {self.destination_airport} \n| Price: {self.price} EUR |\n"
                              f"| Stops: {self.stops}  |\n"
                              f"| Departure: {self.departure_date} {self.departure_time} |\n")

            for user in self.data_users:


                message = (
                    f"Subject: Flight Price Alert!\n\n"
                    f"Hey {user['firstname']}, price alert:{create_message}"
                )
                
                con.sendmail(from_addr=EMAIL_FROM, to_addrs=user["email"],
                            msg=message)

                print("Mail sent to:", user["email"])


            con.close()

