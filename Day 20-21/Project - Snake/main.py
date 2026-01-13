import time
from turtle import *
from snake import Snake
from food import Food
from game import Game

# Skapa och konfigurera spelrutan
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.tracer(0)

game = Game()
snake = Snake()
food = Food()


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
    time.sleep(0.2)
    snake.move_snake()

    # Game over - träffar en vägg eller ormen kolliderar med sig själv
    game_active = game.game_over(snake.snake, snake.snake_head_x, snake.snake_head_y)


    # +1 poäng om ormen fångar maten
    if food.food_position_x == snake.snake_head_x and food.food_position_y == snake.snake_head_y :
        food.new_position_food()
        snake.add_snake_part()
        game.score +=1
        game.write_score()


# När spelet är slut, visa Game Over-text
game.game_over_text()

screen.mainloop()
