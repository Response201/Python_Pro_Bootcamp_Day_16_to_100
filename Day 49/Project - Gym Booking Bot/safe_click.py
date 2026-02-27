import time

# Säkerställer att ett element scrollas till och klickas, för att undvika problem med osynliga element
def safe_click(driver, element):
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        element
    )
    time.sleep(0.4)
    element.click()