from turtle import *
SNAKE_STARTING_POSITION= [(10,0), (0, 0), (-10,0), (-20,0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.dx = 10
        self.dy = 0
        self.move = [10, 0]
        self.create_snake()
        self.snake_head_x=10
        self.snake_head_y =0

    # Skapar orm
    def create_snake(self):
        for body_part in SNAKE_STARTING_POSITION:
            snake_part = Turtle()
            snake_part.color("white")
            snake_part.shape("square")
            snake_part.shapesize(0.5)
            snake_part.penup()
            snake_part.goto(body_part[0], body_part[1])
            self.snake.append(snake_part)

    # Lägger till nytt segment när ormen äter mat
    def add_snake_part(self):

                snake_part = Turtle()
                snake_part.color("white")
                snake_part.shape("square")
                snake_part.shapesize(0.5)
                snake_part.penup()
                snake_part.goto(self.snake[-1].xcor() , self.snake[-1].ycor() )
                self.snake.append(snake_part)


    # Flyttar ormen framåt
    def move_snake(self):
        # Flytta varje segment till platsen för segmentet framför
        for i in range(len(self.snake) - 1, 0, -1):
            x = self.snake[i-1].xcor()
            y = self.snake[i-1].ycor()
            self.snake[i].goto(x, y)

        # Flytta huvudet i aktuell riktning
        head = self.snake[0]
        self.snake_head_x = head.xcor() + self.dx
        self.snake_head_y = head.ycor() + self.dy
        head.goto(self.snake_head_x, self.snake_head_y)

    # kontroller för att styra orm
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


