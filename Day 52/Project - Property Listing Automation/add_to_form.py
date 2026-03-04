from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from property_to_rent import PropertyScraper
import time
import os
from dotenv import load_dotenv
load_dotenv()


class AddToForm(PropertyScraper):

    def __init__(self):
        super().__init__()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 30)

    # Registrerar varje annons i Google formuläret
    def add_to_google_form(self):
      self.driver.get(os.getenv("FORM_LINK"))

      for rental in self.properties:
        time.sleep(1)

        input_fields = self.wait.until( EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[role="listitem"]'))
        )
        time.sleep(1)
        for question in input_fields:
            label_text = question.find_element(By.CSS_SELECTOR, "span").text.lower()
            input_field = question.find_element(By.CSS_SELECTOR, "input, textarea")
            # Fyll i varje fält baserat på etikett
            if label_text == "adress":
                input_field.send_keys(rental["adress"])

            elif label_text == "price per month":
                input_field.send_keys(rental["rent"])

            elif label_text == "link to property":
                input_field.send_keys(rental["link"])

        # Skicka svar
        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'uArJ5e'))
        )
        submit_button.click()

        time.sleep(0.5)
        # Länken för att fylla i ett nytt formulär
        go_to_new_form = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a")))
        go_to_new_form.click()




