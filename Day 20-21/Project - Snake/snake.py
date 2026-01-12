from turtle import *
SNAKE_STARTING_POSITION= [(10,0), (0, 0), (-10,0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.dx = 10
        self.dy = 0
        self.move = [10, 0]
        self.create_snake()


    # skapar orm
    def create_snake(self):
        for body_part in SNAKE_STARTING_POSITION:
            snake_part = Turtle()
            snake_part.color("white")
            snake_part.shape("square")
            snake_part.shapesize(0.5)
            snake_part.penup()
            snake_part.goto(body_part[0], body_part[1])
            self.snake.append(snake_part)



    def move_snake(self):
        # Flytta varje i(index) till platsen för segmentet framför, så att kroppen följer huvudet
        for i in range(len(self.snake) - 1, 0, -1):
            x = self.snake[i-1].xcor()
            y = self.snake[i-1].ycor()
            self.snake[i].goto(x, y)

        # flyttar huvudet framåt i nuvarande riktning
        head = self.snake[0]
        head.goto(head.xcor() + self.dx, head.ycor() + self.dy)

    def go_up(self):
        if self.dy == 0:  # hindra 180° vändning
            self.dx = 0
            self.dy = 10

    def go_down(self):
        if self.dy == 0:
            self.dx = 0
            self.dy = -10

    def go_left(self):
        if self.dx == 0:
            self.dx = -10
            self.dy = 0

    def go_right(self):
        if self.dx == 0:
            self.dx = 10
            self.dy = 0


