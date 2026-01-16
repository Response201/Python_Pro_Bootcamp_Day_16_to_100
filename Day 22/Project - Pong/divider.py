from turtle import Turtle

class Divider:
    def __init__(self):
        self.divider_line = Turtle()
        self.divider_line.shape("square")
        self.divider_line.color("white")
        self.divider_line.penup()
        self.divider_line.hideturtle()
        self.divider_line.shapesize(stretch_wid=0.4, stretch_len=1.2)
        self.divider_line.goto(0, -355)
        self.divider_line.setheading(90)
        self.create_line_divider()

    # Skapar streckad linje i mitten av spelplanen
    def create_line_divider(self):
        for _ in range(19):
            self.divider_line.stamp()
            self.divider_line.forward(40)
