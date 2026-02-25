from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
BASE_URL ="https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(BASE_URL)


first_name= driver.find_element(By.NAME, value="fName")
first_name.send_keys("Molly")

last_name= driver.find_element(By.NAME, value="lName")
last_name.send_keys("Hope")

email = driver.find_element(By.NAME, value="email")
email.send_keys("test@test.com")

button = driver.find_element(By.CLASS_NAME, value="btn")
button.send_keys(Keys.ENTER)

time.sleep(3)
driver.quit()