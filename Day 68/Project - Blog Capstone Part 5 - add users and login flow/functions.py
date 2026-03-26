import json
import smtplib
from datetime import datetime as dt
import os
from dotenv import load_dotenv
from sqlalchemy import select
load_dotenv()



def send_mail(from_email="", input_message=""):
    with   smtplib.SMTP("smtp.gmail.com", 587) as con:
        con.starttls()
        con.login(user=os.getenv("EMAIL"), password=os.getenv("EMAIL_KEY"))
        time = dt.now().strftime("%Y-%m-%d")
        create_message = (f"\n{input_message}\n"
                          f" Skickat: {time} \n")
        message = (
                f"Subject: Fråga från blogg !\n\n"
                f"{create_message}"
            ).encode("utf-8")
        con.sendmail(from_addr=f"{from_email}", to_addrs=os.getenv("EMAIL"),
                         msg=message)
        con.close()


# Skapar blogg-inlägg i databasen vid start
def create_default_posts_database(db, Blog):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        if data:
            for item in data:
                print(item)
                post = db.session.execute(select(Blog).where(Blog.title == item["title"])).first()

                if not post:
                    new_post = Blog(
                        id=item["id"],
                        title=item["title"],
                        subject=item["subject"],
                        body=item["body"],
                        image=item["image"],
                        date = dt.now(),
                        author_id=item["author_id"]

                    )
                    db.session.add(new_post)
                    db.session.commit()

