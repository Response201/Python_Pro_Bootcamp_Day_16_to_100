
from selenium.webdriver.common.by import By
from safe_click import safe_click
from check_if_tomorow import check_if_tomorow
import time


# Bokar ett specifikt träningspass utifrån dag, typ av träning och index
def book_class(driver,training, this_day, selected_class_index=0, stats=None):
    time.sleep(1)

    day = check_if_tomorow(driver, this_day)

    all_class_cards = driver.find_element(By.CSS_SELECTOR, f'[id*="day-group-{day}"]')
    card = all_class_cards.find_elements(By.CSS_SELECTOR, f"[id*='class-card-{training}' ]")

    # Kontrollerar så valt kort finns
    if not card or selected_class_index >= len(card):
        print(f"Not found: {training.title()} Class")
        stats["not_found"] +=1
        return stats

    selected_card = card[selected_class_index]

    # Knapp för att boka träningspass
    book_btn = selected_card.find_element(By.CSS_SELECTOR, '[id*="book-button"]')


    # Namn på aktuellt träningspass
    name_class = selected_card.find_element(By.CSS_SELECTOR, '[id*="class-name"]').text

    # Tid för träningspass
    time_class_full = selected_card.find_element(By.CSS_SELECTOR, '[id*="class-time"]').text
    time_class = time_class_full.split(" ")

    book_verification_text=""
    day = day.title()


    # Kolla om klass går att boka

    if book_btn.text == "Booked":
        book_verification_text = "Already booked"
        stats["bookedORwaitlisted"] += 1

    elif book_btn.text == "Waitlisted":
        book_verification_text = "Already on waitlist"
        stats["bookedORwaitlisted"] += 1

    elif book_btn.text == "Book Class":
        safe_click(driver, book_btn)
        book_verification_text = "Booked"
        stats["booked"] += 1
        stats["booking_list"].append(f"[New Booking] {name_class} {time_class[1]} {day}")

    elif book_btn.text == "Join Waitlist":
        safe_click(driver, book_btn)
        book_verification_text = "Joined waitlist"
        stats["waitlist"] += 1
        stats["booking_list"].append(f"[New Waitlist] {name_class} {time_class[1]} {day}")

    print(f"{book_verification_text}: {name_class} {time_class[1]} {day}")

    return stats
