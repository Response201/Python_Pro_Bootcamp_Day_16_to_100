import smtplib
import requests
import datetime as dt
import os
from dotenv import load_dotenv
load_dotenv()



def send_mail(from_email="", input_message=""):
    with   smtplib.SMTP("smtp.gmail.com", 587) as con:
        con.starttls()
        con.login(user=os.getenv("EMAIL"), password=os.getenv("EMAIL_KEY"))
        time = dt.datetime.now().strftime("%Y-%m-%d")
        create_message = (f"\n{input_message}\n"
                          f" Skickat: {time} \n")
        message = (
                f"Subject: Fråga från blogg !\n\n"
                f"{create_message}"
            ).encode("utf-8")
        con.sendmail(from_addr=f"{from_email}", to_addrs=os.getenv("EMAIL"),
                         msg=message)
        con.close()


def get_data(url):
    res = requests.get(url)
    res.raise_for_status()
    return res.json()
