import random
from turtle import Turtle




class Ball:

    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.shapesize(1)
        self.ball.color("blue")
        self.ball.penup()
        self.ball.goto(0,0)
        self.y=0
        self.x=0
        self.move =0
        self.dir_y=random.choice([-3, 3])
        self.dir_x=random.choice([-3, 3])
        self.move_ball()
        self.bounce_wall()
        self.bounce_paddle()

    # Återställ bollens position till mitten av spelplanen
    def restart(self):
        self.ball.goto(0,0)

    # Byt riktning i y-led (studsa mot övre/nedre vägg)
    def bounce_wall(self, ):
           self.dir_y *= -1

    # Byt riktning i x-led (studsa mot paddel)
    def bounce_paddle(self):
        self.dir_x *= -1.2

    # Uppdatera bollens position baserat på riktning
    def move_ball(self):

        x = self.ball.xcor() + self.dir_x
        y = self.ball.ycor() + self.dir_y
        self.x = x
        self.y = y


        self.ball.goto(x,y)






