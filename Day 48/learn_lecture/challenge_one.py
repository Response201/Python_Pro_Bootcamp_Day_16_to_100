from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(BASE_URL)


date_list = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
event_text_list = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
print(list)
new=[{item: {"date": date_list[item].text, "text": event_text_list[item].text}} for item in range(len(date_list))]

#for item in range(len(date_list)):
#
#    new.append({item: {"date": date_list[item].text, "text": event_text_list[item].text}})


print(new)