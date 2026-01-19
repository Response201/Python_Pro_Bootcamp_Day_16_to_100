import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from game_over_text import Game_over_text

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Skapa spelare och bilar
player = Player()
car_manager = CarManager()


# Lyssna på knapptryckningar
screen.listen()
screen.onkeypress(player.forward, "Up")
screen.onkeypress(player.left, "Left")
screen.onkeypress(player.right, "Right")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Om spelare och bil kolliderar stoppas spelet
    for car in car_manager.cars:
        if (player.player_positon_x == car.xcor() - 10 and
           car.ycor() >= player.player_positon_y - 10 and
           car.ycor() <= player.player_positon_y + 20):
                game_is_on = False

    # Kontrollera om spelaren når nästa level
    player.next_level()

Game_over_text()





screen.mainloop()