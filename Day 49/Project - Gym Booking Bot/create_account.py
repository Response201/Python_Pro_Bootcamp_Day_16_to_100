from selenium.webdriver.common.by import By
import time

# Skapar ett nytt användarkonto: navigerar till registreringssidan, fyller i namn-, mail- och lösenord fälten, och klickar på submit-knappen
def create_account(driver):

    go_to_login_page = driver.find_element(By.CLASS_NAME, value="Home_heroButton__3eeI3")
    go_to_login_page.click()

    time.sleep(1)
    go_to_reg_account_page = driver.find_element(By.ID, value="toggle-login-register")
    go_to_reg_account_page.click()
    time.sleep(1)


    input_name = driver.find_element(By.NAME, value="name")
    input_name.send_keys("Molly")

    input_email = driver.find_element(By.NAME, value="email")
    input_email.send_keys("molly@hej.com")

    input_password = driver.find_element(By.NAME, value="password")
    input_password.send_keys("Testaettpassword")

    create_account_btn = driver.find_element(By.ID, value="submit-button")
    create_account_btn.click()

    time.sleep(1)

    log_out = driver.find_element(By.ID, value="logout-button")
    log_out.click()

    time.sleep(1)