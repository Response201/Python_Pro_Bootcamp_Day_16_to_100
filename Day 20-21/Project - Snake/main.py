import time
from turtle import *
from food import Food
from game import Game

# Skapa och konfigurera spelrutan
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")

screen.setup(600,600)
screen.tracer(0)

game = Game()
snake = game
food = game


# Aktivera tangentlyssning
screen.listen()

# Visa startpoäng
game.create_score_text()

# Registrera kontroller för ormen
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")
screen.onkey(snake.go_down, "Down")


game_active = True

while game_active:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Game over - träffar en vägg eller ormen kolliderar med sig själv
    game_active = game.game_over()


    # +1 poäng om ormen fångar maten
    game.check_food_eaten()


# När spelet är slut - while-loopen stoppas, visas Game Over-text
game.game_over_text()

screen.mainloop()
