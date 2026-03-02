from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)



class InternetSpeedBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up= 100
        self.down = 100
        self.promised_down = 100
        self.promised_up = 100
        self.test_id=""



    # Hämtar aktuell internet hastighet
    def get_internet_speed(self):
        wait = WebDriverWait(self.driver, 5)
        url = "https://www.speedtest.net/"
        self.driver.get(url)

        cookies_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))

        )
        cookies_btn.click()


        go_btn = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "start-text"))
        )
        go_btn.click()


        time.sleep(40)

        speed_down_elem = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "download-speed"))
        )
        speed_up_elem = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "upload-speed"))
        )

        self.down = float(speed_down_elem.text)
        self.up = float(speed_up_elem.text)

        # Hämta test-ID för att kunna ge resultatlänken
        self.test_id = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".result-data > a"))
        ).text


    # Postar internet-hastigheten och skriver ut resultatlänken
    def post_message(self):
        wait = WebDriverWait(self.driver, 20)
        url = "https://grabacoffee.netlify.app"
        self.driver.get(url)

        text_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="text"]'))
        )

        # Printa resultat länk
        print(f"www.speedtest.net/result/{self.test_id}")

        # Posta internet hastighet
        text_input.send_keys( f"Ahhh, grab a coffee… my internet speed is only {self.down}/{self.up} Mbps!")

        send_btn = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "buttonVaild"))
        )
        send_btn.click()



