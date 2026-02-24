
from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL_KEY = os.getenv("EMAIL_KEY")
EMAIL_FROM = os.getenv("EMAIL")
EMAIL_TO = os.getenv("EMAIL_TO")
#BASE_URL = "https://www.amazon.se/Olaplex-Trattamento-Riparatore-H%C3%A5rbehandling-Unisex-Vuxen/dp/B08TWTQDCX?ref_=Oct_d_orecs_d_27983526031_2&pd_rd_w=sj03D&content-id=amzn1.sym.ec2473a4-34e3-4272-b3b9-785eb9f1c6ba&pf_rd_p=ec2473a4-34e3-4272-b3b9-785eb9f1c6ba&pf_rd_r=8XNEEK9TCBJFVN0TQ3PM&pd_rd_wg=fARLB&pd_rd_r=e2c31ea7-4c96-4a8f-ba9b-39ef43dcd32f&pd_rd_i=B08TWTQDCX"
BASE_URL = os.getenv("BASE_URL")
TARGET_PRICE = 200


# Skickar mail med prisinformation
def send_mail(message):
    with   smtplib.SMTP("smtp.gmail.com", 587) as con:
        con.starttls()
        con.login(user=EMAIL_FROM, password=EMAIL_KEY)
        con.sendmail(from_addr=EMAIL_FROM, to_addrs=EMAIL_TO, msg=message.encode("utf-8"))
        con.close()



# Hämtar innehåll från produktsidan
def scrape_html():
    try:
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Cookie": 'COOKIEINFO',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Site": "none",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15"
        }

        response = requests.get(BASE_URL, headers=header)
        response.raise_for_status()
        return response.text
    except requests.RequestException as error:
        print("fail:",error)




# Hämtar produkt pris och skickar mail om priset är mindre än TARGET_PRICE
def get_price():
    page = scrape_html()

    soup = BeautifulSoup(page, "html.parser")
    product_title = soup.find("span", id="productTitle").getText().strip()
    current_price =round( float(soup.find("span", class_="a-price-whole").getText().replace(".","").replace(",", ".")))
    price_symbol = soup.find("span", class_="a-price-symbol").getText()

    if TARGET_PRICE >  current_price:

        send_mail(f"Subject:Pris alarm!\n\n{product_title}\n\nNuvarande pris: {current_price}{price_symbol}")



get_price()






