import smtplib
import random
import datetime as dt
from dotenv import load_dotenv
import os

#Laddar in variabler från env-fil
load_dotenv()
my_test_password = os.getenv("PASSWORD", "my_test_password")
my_test_email =  os.getenv("EMAIL", "my_test_email")
to_email =  os.getenv("TO_EMAIL", "to_email")

# Hämtar aktuell veckodag
current_date = dt.datetime.now()
weekday = current_date.weekday()

# Skickar ett motiverande citat via e-post om det är måndag
if weekday == 0:

    with open("quotes.txt") as file:
            # Väljer ett slumpmässigt citat
            all_quotes = file.readlines()
            quote = random.choice(all_quotes)

            # SMTP-anslutning
            connection = smtplib.SMTP("smtp.gmail.com", 587)
            connection.starttls()
            connection.login(user=my_test_email, password=my_test_password)

            connection.sendmail(
                from_addr=my_test_email,
                to_addrs=to_email,
                msg=f" Monday Motivation: \n{quote}")

            connection.close()




