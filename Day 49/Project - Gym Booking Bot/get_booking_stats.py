from selenium.webdriver.common.by import By
from safe_click import safe_click
import time


# Sammanfattning av bokningar: bokade, väntelista, redan bokade, ej hittade och antal hanterade klasser
def get_booking_stats(driver,stats):
    go_to_bookings_page = driver.find_element(By.ID, value="my-bookings-link")
    safe_click(driver, go_to_bookings_page)

    all_bookings = len(driver.find_elements(By.CSS_SELECTOR, '[id*="booking-card-booking"]' ))
    all_waitlist = len(driver.find_elements(By.CSS_SELECTOR, '[id*="waitlist-card-waitlist"]' ))

    confirm_all_bookings = "✅" if all_bookings == stats["booked"] else "❌"
    confirm_all_waitlist = "✅" if all_waitlist == stats["waitlist"] else "❌"






    all_booking_actions = stats["bookedORwaitlisted"] + stats["booked"] + stats["waitlist"] + stats["not_found"]

    print(f"\n--- BOOKING SUMMARY --- \n"
          f"Classes booked: {stats['booked']}\n"
          f"Waitlists joined: {stats['waitlist']}\n"
          f"Already booked or waitlisted: {stats['bookedORwaitlisted']}\n"
          f"Classes not found: {stats['not_found']}\n"
          f"Total classes processed: {all_booking_actions} \n"

         )
    if len(stats["booking_list"]) > 0:
        print(
              f"\n--- DETAILED CLASS LIST ---"
              )
        for item in stats["booking_list"]:
            print(f"•{item}")


    print(f"\n--- CONFIRMATION SUMMARY ---\n"
          f"Bookings status: {confirm_all_bookings} ({stats['booked']} of {all_bookings} booked)\n"
          f"Waitlist status: {confirm_all_waitlist} ({stats['waitlist']} of {all_waitlist} joined)\n"
          )