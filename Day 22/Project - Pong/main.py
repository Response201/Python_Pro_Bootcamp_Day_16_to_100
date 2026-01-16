from turtle import Screen
import time
from text import *
from playerPaddle import PlayerPaddle
from ball import Ball
from scoarBoard import ScoreBoard
from divider import Divider

screen = Screen()
screen.setup(1000,800)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# Skapar linje i mitten av spelbrädet
line_Divider = Divider()

# Skapar boll
ball = Ball()

# Spelare 1 (höger sida)
player_one = PlayerPaddle((-400, 0), ball,  ScoreBoard((-100, 300)))

screen.onkeypress(player_one.start_up, "w")
screen.onkeyrelease(player_one.stop_up, "w")

screen.onkeypress(player_one.start_down, "s")
screen.onkeyrelease(player_one.stop_down, "s")

# Spelare 2 (vänster sida)
player_two =  PlayerPaddle((400, 0), ball,  ScoreBoard((100, 300)))


screen.onkeypress(player_two.start_up, "Up")
screen.onkeyrelease(player_two.stop_up, "Up")

screen.onkeypress(player_two.start_down, "Down")
screen.onkeyrelease(player_two.stop_down, "Down")




game_on = True
ball.move_ball()

while game_on:


    # Uppdaterar spelarnas paddlar
    player_one.update()
    player_two.update()

    # Kollar om spelare träffat boll med paddle
    player_one.check_hit_ball()
    player_two.check_hit_ball()


    # Kollar om någon av spelarna fått 3 poäng = vinner
    if player_one.scoreboard.score >= 3 or player_two.scoreboard.score >= 3:
        winner = "Player 2"
        if player_one.scoreboard.score >  player_two.scoreboard.score:
            winner ="Player 1"

        # Skriver ut vilken spelare som vunnit
        game_on = False
        text = TextWriter()
        text.write_text(
            text=f"Winner: {winner}",
            position=(20,0),
            font_size=32,
            font_style="bold",
            color="red"
        )


    # Kontrollera om bollen passerat vänster eller höger vägg
    # Om så är fallet, ge poäng till motståndaren och återställ bollen till mitten
    elif ball.x <= -490 or ball.x >= 490 :

            if -1 <= ball.x:
                player_one.scoreboard.add_point()
            else:
                player_two.scoreboard.add_point()

            ball.restart()

    # Kontrollera om bollen träffar övre eller nedre vägg
    # Om den gör det, vänd y-riktningen så att bollen studsar tillbaka
    elif ball.y <= -390 or ball.y >= 390 :
                ball.bounce_wall()



    ball.move_ball()
    screen.update()
    time.sleep(0.016)



screen.mainloop()