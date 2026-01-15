from turtle import Screen
import time
from playerPaddle import PlayerPaddle

screen = Screen()
screen.setup(1000,800)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()



# Player 1 (höger sida)
player_one = PlayerPaddle((400,0))

screen.onkeypress(player_one.start_up, "Up")
screen.onkeyrelease(player_one.stop_up, "Up")

screen.onkeypress(player_one.start_down, "Down")
screen.onkeyrelease(player_one.stop_down, "Down")

# Player 2 (vänster sida)
player_two = PlayerPaddle((-400,0))

screen.onkeypress(player_two.start_up, "w")
screen.onkeyrelease(player_two.stop_up, "w")

screen.onkeypress(player_two.start_down, "s")
screen.onkeyrelease(player_two.stop_down, "s")


game_on = True

while game_on:


    # Uppdaterar spelarnas paddlar
    player_one.update()
    player_two.update()



    screen.update()
    time.sleep(0.016)





# Skapa spelbräde
# Skapa poäng-klass
# Skapa boll-klass
# Hantera när bollen:
# - träffar en paddel
# - lämnar spelområdet (ge poäng och starta ny boll från mitten)


screen.mainloop()