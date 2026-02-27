import os
from  selenium import webdriver
from create_account import create_account
from login_account import login_account
from book_class import book_class
from book_all_classes_for_day import book_all_classes_for_day
from get_booking_stats import get_booking_stats
import time

BASE_URL = "https://appbrewery.github.io/gym/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(BASE_URL)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


stats = {"booked": 0,
"waitlist":  0,
"not_found": 0,
"bookedORwaitlisted": 0,
"booking_list":[]
         }
time.sleep(1)



# Skapar konto
create_account(driver)

# Logga in med det skapade kontot
login_account(driver)


# Bokar ett specifikt träningspass utifrån dag, typ av träning och index
stats = book_class(driver,"spin","wed",1, stats=stats)

stats = book_class(driver,"yoga", "fri", 1, stats=stats)

stats = book_class(driver,"yoga", "thu", 1, stats=stats)



# Bokar alla tillgängliga träningspass för en dag
stats=book_all_classes_for_day(driver, "wed",stats)
stats=book_all_classes_for_day(driver, "thu",stats)

# Sammanfattning av bokningar: bokade, väntelista, redan bokade, ej hittade och antal hanterade klasser
get_booking_stats(driver,stats)



time.sleep(10)
driver.quit()