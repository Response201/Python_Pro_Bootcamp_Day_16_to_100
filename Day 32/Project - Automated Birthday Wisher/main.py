import random
import smtplib
import datetime as dt
from dotenv import load_dotenv
import os
import pandas as pd


#Laddar in variabler från env-fil
load_dotenv()
my_test_password = os.getenv("PASSWORD", "my_test_password")
my_test_email =  os.getenv("EMAIL", "my_test_email")

# Hämtar nuvarande datum och tid
current_date = dt.datetime.now()

# Väljer ett slumpmässigt brev från mappen med mallar och returnerar texten
def pick_random_letter(template_dir="letter_templates/"):
    all_letters = os.listdir(f"{template_dir}")
    random_letter = random.choice(all_letters)
    with open(f"{template_dir}{random_letter}") as file:
        return file.read()


# Beräknar ålder baserat på födelsedatum
def calculate_age(birth_year, birth_month, birth_day):
    return str(current_date.year - birth_year - ((current_date.month, current_date.day) < (birth_month, birth_day)))



# Skapar SMTP-anslutning och skickar mail
def send_email(to_email, send_letter=""):

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_test_email, password=my_test_password)
        connection.sendmail(from_addr=my_test_email, to_addrs=to_email, msg=send_letter)
        print(f"Mail sent to {to_email}")
        connection.close()



try:
    # Läser in födelsedagsdata och konverterar till en lista av dictionaries
     all_birthday= pd.read_csv("birthdays.csv").to_dict(orient="records")


     for index in range(len(all_birthday)):

            row_info = all_birthday[index]
            birth_year = row_info["year"]
            birth_month = row_info["month"]
            birth_day = row_info["day"]
            birth_name = row_info["name"].title()


            # Kollar om personen fyller år idag (dag och månad)
            if (birth_day == current_date.day
                and birth_month == current_date.month):

                # Beräknar personens ålder
                age = calculate_age(birth_year, birth_month, birth_day)

                # Väljer ett slumpmässigt brev och ersätter [NAME] och [AGE]
                letter = pick_random_letter()
                update_letter_template = letter.replace("[NAME]", birth_name).replace("[AGE]", age)

                # Skickar det färdiga brevet via e-post
                send_email(row_info["email"], update_letter_template)





except FileNotFoundError:
    print("error")




