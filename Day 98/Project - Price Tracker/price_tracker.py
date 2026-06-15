from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from functions import send_mail
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


games = [
    "https://steamdb.info/app/1611580/",
    "https://steamdb.info/app/1091500/",
    "https://steamdb.info/app/570/",
    "https://steamdb.info/app/271590/",
    "https://steamdb.info/app/292030/"
]

results = []

try:
    for url in games:
        try:
            driver.get(url)
            time.sleep(3)

            get_titel = driver.find_element(By.CSS_SELECTOR, "h1").text
            titel = get_titel if get_titel else ""

            price_element = driver.find_element(By.CLASS_NAME, "table-prices-current")
            price_text = price_element.text

            parts = price_text.replace(",", ".").split()
            prices = []

            for part in parts:
                try:
                    prices.append(float(part.replace("€", "")))
                except:
                    pass

            current_price = prices[0]
            lowest_price = prices[-1]

            icon = "🎉" if current_price <= lowest_price else "⛔"

            results.append(
                f"{icon} {titel}\n"
                f"Current: {current_price} € | Lowest: {lowest_price} €\n"
            )

        except NoSuchElementException:

            titel = driver.find_element(By.CSS_SELECTOR, "h1").text
            create_message = f"⚠️ "

            if titel != "Checking your browser…":
                create_message += f"{titel} \nFailed to read price \n"
            else:
                create_message += f"Something went wrong \n"

            results.append(create_message)
            continue

except Exception as e:

    results.append(f"❌ Unexpected error \n")

finally:
    driver.quit()


message = "Steam Price Summary:\n\n" + "\n".join(results)
send_mail(message)