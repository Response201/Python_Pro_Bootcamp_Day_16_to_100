from selenium.webdriver.common.by import By
from safe_click import safe_click
import os
from dotenv import load_dotenv
load_dotenv()
import time


USER_MAIL= os.getenv("USER_MAIL")
USER_PASSWORD= os.getenv("USER_PASSWORD")

# Loggar in användaren: navigerar till login-sidan, fyller i e-post och lösenord, och klickar på login-knappen
def login_account(driver, username=USER_MAIL, this_password=USER_PASSWORD):
    time.sleep(2)
    # Gå till sidan för att loga in och sedan vidare till sidan för att registrera konto
    go_to_login_page = driver.find_element(By.CLASS_NAME, value="Home_heroButton__3eeI3")
    go_to_login_page.click()

    time.sleep(1)

    email = driver.find_element(By.NAME, value="email")
    email.send_keys(username)

    password = driver.find_element(By.NAME, value="password")
    password.send_keys(this_password)

    login_btn = driver.find_element(By.ID, value="submit-button")
    safe_click(driver, login_btn)


