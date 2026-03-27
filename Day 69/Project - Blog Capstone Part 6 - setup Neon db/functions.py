import smtplib
import os
import werkzeug
from dotenv import load_dotenv
import json
from datetime import datetime as dt
from sqlalchemy import select
load_dotenv()




def send_mail(from_email="", input_message=""):
    with smtplib.SMTP("smtp.gmail.com", 587) as con:
        con.starttls()
        con.login(user=os.getenv("EMAIL"), password=os.getenv("EMAIL_KEY"))
        timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        create_message = (
            f"\n{input_message}\n"
            f"Skickat: {timestamp}\n"
        )
        message = (
            f"Subject: Fråga från blogg!\n\n"
            f"{create_message}"
        ).encode("utf-8")
        con.sendmail(from_addr=from_email, to_addrs=os.getenv("EMAIL"), msg=message)





def create_default_posts_database(session, Blog):

        if session.query(Blog).count() == 0:
            try:
                with open("data.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
            except FileNotFoundError:
                print("data.json hittades inte – inga default posts skapade.")
                return

            for item in data:
                post = session.execute(
                    select(Blog).where(Blog.title == item["title"])
                ).scalar_one_or_none()

                if not post:
                    new_post = Blog(
                        title=item["title"],
                        subject=item["subject"],
                        body=item["body"],
                        image=item["image"],
                        date=dt.now().strftime("%Y-%m-%d %H:%M:%S"),
                        author_id=item["author_id"]
                    )
                    session.add(new_post)
                    print(f"Inlägg '{item['title']}' skapat!")

            session.commit()




def create_default_users_database(session, User):

    if session.query(User).count() == 0:
            hashed_password = werkzeug.security.generate_password_hash(
                "123456", method="scrypt", salt_length=8
            )

            admin = User(
                email="admin@hej.com",
                name="Admin",
                password=hashed_password
            )
            molly = User(
                email="molly@hej.com",
                name="molly",
                password=hashed_password
            )
            anna = User(
                email="anna@hej.com",
                name="anna",
                password=hashed_password
            )

            session.add(admin)
            session.add(molly)
            session.add(anna)
            session.commit()