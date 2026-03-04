from add_to_form import AddToForm
import time

bot = AddToForm()

# Hämtar alla bostäder
bot.scrape_properties()

# fyller i form och skickar svar
bot.add_to_google_form()



# Väntar 10 sekunder innan webbläsaren stängs
time.sleep(10)
bot.driver.quit()
