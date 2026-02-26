from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = "https://ozh.github.io/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(BASE_URL)

time.sleep(3)

# Väljer svenska
select_lang = driver.find_element(By.ID, value="langSelect-SV")
select_lang.click()

time.sleep(3)
# Acceptera cookies
check_cookies = driver.find_element(By.XPATH, value='/html/body/div[1]/div/a[1]')
check_cookies.click()



time.sleep(3)

cookie = driver.find_element(By.ID, value="bigCookie")
products_list = [f"product{i}" for i in range(20)]

# Timer
start = time.time()

# Hur länge spelet ska köras (sekunder)
run_time = 35

while time.time() - start < run_time:

    cookie.click()

    # Kollar uppgraderingar var 15:e sekund
    if int(time.time() - start) % 15 == 0:
        for product in reversed(products_list):
            try:
                best_product = driver.find_element(By.ID, product)
                element_class = best_product.get_attribute("class")

                if "enabled" in element_class:
                    best_product.click()
                    break
            except:
                pass

driver.quit()