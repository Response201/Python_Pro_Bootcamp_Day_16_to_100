from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import os
from dotenv import load_dotenv
load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
URL = os.getenv("BASE_URL")

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 30)

    # Loggar in
    def login(self):

        self.driver.get(f"{URL}/accounts/login")

        # Neka cookies
        cookies_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")))

        cookies_btn.click()

        # Fyller i användarnamn och lösenord
        email_input = self.wait.until((
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name="email"]'))
        ))
        email_input.send_keys(os.getenv("INSTA_USER"))

        password_input = self.wait.until((
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name="pass"]'))
        ))
        password_input.send_keys(os.getenv("INSTA_PASSWORD"))

        # Klicka på logga in
        login_btn = self.wait.until((
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Logga in"]'))
        ))
        login_btn.click()

        # Neka att spara inloggningsuppgifter
        save_user = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div')))
        save_user.click()



    # Går till en profil och öppnar listan med följare
    def find_followers(self):

        # Gå till profil-sida
        page = os.getenv("SIMILAR_ACCOUNT")
        self.driver.get(f"{URL}/{page}")

        # Öppna lista med följare
        find_followers_popup = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/section/main/div/div/header/div/section[2]/div/div[3]/div[2]/a')))
        find_followers_popup.click()
        time.sleep(3)



    # Följ användare från lista
    def follow(self):

        # Hitta pop-up-fönstret med följare
        followers_popup = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']"))
        )

        time.sleep(1)
        # Hämta alla följare i pop-up
        rows = followers_popup.find_elements(By.CLASS_NAME, "x1qnrgzn" )

        for row in rows:
            try:
                # Hämta användarnamn och följa-knapp(text)
                user = row.find_element(By.XPATH, ".//a/div/div/span").text
                button = row.find_element(By.XPATH, ".//button")

                if button.text == "Följ":
                    button.click()
                    if user:
                        print(f"Following request sent to {user}")
                    time.sleep(1)
                elif "Förfrågan" in button.text:
                    print(f"Follow request already sent to {user}")
                else:
                    if user:
                        print(f"Already following {user}")

            except:
                pass

            # Scrolla för att ladda fler användare
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
            time.sleep(1)

