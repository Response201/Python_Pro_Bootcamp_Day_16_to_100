import time
from turtle import *
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.tracer(0)

snake = Snake()
screen.listen()


screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")
screen.onkey(snake.go_down, "Down")


game_active = True

while game_active:

    screen.update()
    time.sleep(0.15)
    snake.move_snake()


screen.mainloop()
