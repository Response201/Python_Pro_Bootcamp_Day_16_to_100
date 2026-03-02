from internet_speed_bot import InternetSpeedTwitterBot
import time


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

# Om hastigheten är lägre än det utlovade, posta ett meddelande
if bot.up < bot.promised_up or bot.promised_down < bot.down:
    bot.post_message()

# Vänta 30 sekunder innan webbläsaren stängs
time.sleep(30)
bot.driver.quit()
