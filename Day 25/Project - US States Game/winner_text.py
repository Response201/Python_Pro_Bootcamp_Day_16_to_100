from turtle import Turtle

class Winner_text:
    def __init__(self):
        super().__init__()
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.color("black")
        self.turtle.goto(20,0)
        self.turtle.write(
            "You found all states!",
            align="center",
            font=("Courier", 32, "bold")
        )




