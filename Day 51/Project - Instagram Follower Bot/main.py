from insta_follower import InstaFollower
import time




bot = InstaFollower()

# Logar in användare
bot.login()

# Går till vald sida och öppnar listan med följare
bot.find_followers()

# Följer användare från listan
bot.follow()



# Väntar 30 sekunder innan webbläsaren stängs
time.sleep(30)
bot.driver.quit()