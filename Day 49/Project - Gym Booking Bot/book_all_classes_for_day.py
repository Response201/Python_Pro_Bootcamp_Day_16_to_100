from selenium.webdriver.common.by import By
from book_class import book_class
from check_if_tomorow import check_if_tomorow
import time

# Bokar alla tillgängliga träningspass för en dag
def book_all_classes_for_day(driver, this_day, stats):
    time.sleep(1)
    day = check_if_tomorow(driver, this_day)


    # Tar ut alla träningspass för vald dag
    all_class_cards = driver.find_element(By.CSS_SELECTOR, f'[id*="day-group-{day}"]')

    # Tar ut alla namn på träningspass för vald dag
    class_titles = all_class_cards.find_elements(By.CSS_SELECTOR, "h3[id*='class-name']")

    # Tar ut unika träningspass
    uniq_classes = set([title.text for title in class_titles])

    for title in uniq_classes:
        time.sleep(0.5)
        training_name = title.replace("Class", "").replace(" ", "").lower()
        cards = all_class_cards.find_elements(By.CSS_SELECTOR, f"[id*='class-card-{training_name}']")

        for index in range(len(cards)):
            time.sleep(1)
            stats = book_class(driver, training_name, this_day=day, selected_class_index=index, stats=stats)

    return stats