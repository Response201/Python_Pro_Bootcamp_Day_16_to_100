import smtplib
import datetime as dt
import os
from dotenv import load_dotenv
load_dotenv()



def send_mail(input_message=""):
    with   smtplib.SMTP("smtp.gmail.com", 587) as con:
        con.starttls()
        con.login(user=os.getenv("EMAIL"), password=os.getenv("EMAIL_KEY"))
        time = dt.datetime.now().strftime("%Y-%m-%d")
        create_message = (f"\n{input_message}\n"
                          f" Date: {time} \n")
        message = (
                f"Subject: Price tracker \n\n"
                f"{create_message}"
            ).encode("utf-8")
        con.sendmail(from_addr=f"{os.getenv("EMAIL")}", to_addrs=os.getenv("EMAIL_TO"),
                         msg=message)
        con.close()



