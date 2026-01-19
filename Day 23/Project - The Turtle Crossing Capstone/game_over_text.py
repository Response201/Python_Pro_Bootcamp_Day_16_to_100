from turtle import Turtle

class Game_over_text:
    def __init__(self):
        super().__init__()
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.color("black")
        self.turtle.goto(20,0)
        self.turtle.write(
            "GAME OVER",
            align="center",
            font=("Courier", 32, "bold")
        )




