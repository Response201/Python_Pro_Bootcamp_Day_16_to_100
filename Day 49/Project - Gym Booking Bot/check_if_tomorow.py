from selenium.webdriver.common.by import By

# Kontrollerar dag och returnerar "today", "tomorrow" eller oförändrat värde
def check_if_tomorow(driver,day):

    get_today= driver.find_element(By.CSS_SELECTOR, f'[id*="day-title-today"]').text
    today = get_today.split("(")[1].split(",")[0].lower()

    get_tomorow = driver.find_element(By.CSS_SELECTOR, f'[id*="day-title-tomorrow"]').text
    tomorow = get_tomorow.split("(")[1].split(",")[0].lower()

    if tomorow == day:
        day = "tomorrow"
    if today == day:
        day = "today"

    return day