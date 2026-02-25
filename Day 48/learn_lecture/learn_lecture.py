from selenium import webdriver
from selenium.webdriver.common.by import By

#BASE_URL = "https://www.aftonbladet.se/"
#BASE_URL = "https://www.python.org/"
BASE_URL = "https://en.wikipedia.org/wiki/Main_Page"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(BASE_URL)


# Aftonbladet
#text = driver.find_element(By.CLASS_NAME, value="_dynamic-segment_1vp2k_235")
#print(text.text)

# Python.org

# XPath
#bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
#print(bug_link.text)

# Skriva in text i sökfält och trycka på knapp för att göra sökning
#search_bar = driver.find_element(By.NAME, value="q")
#search_bar.clear()
#search = "documentation"
#search_bar.send_keys(search)
#print(search_bar.get_attribute("placeholder"))

#search_bar_button = driver.find_element(By.ID, value="submit")
#search_bar_button.click()
#print(search_bar_button)



# Wikipedia

#text = driver.find_element(By.CSS_SELECTOR, '[title="Special:Statistics"]').text
#text_two = driver.find_element(By.CSS_SELECTOR, value="#articlecount a").text

#portals_link = driver.find_element(By.LINK_TEXT, value="Content portals")
#portals_link.click()


#driver.quit()

