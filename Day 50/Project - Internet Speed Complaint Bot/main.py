from internet_speed_bot import InternetSpeedBot
import time


bot = InternetSpeedBot()
bot.get_internet_speed()

# Om hastigheten är lägre än det utlovade, posta ett meddelande
if bot.up < bot.promised_up or bot.promised_down < bot.down:
    bot.post_message()

# Vänta 30 sekunder innan webbläsaren stängs
time.sleep(30)
bot.driver.quit()
