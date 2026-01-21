from turtle import Turtle


class State_label:
    def __init__(self):
        self.data = [{"state":"","x": 0,"y": 0}]

    # Skapar och placerar en text med delstatens namn på kartan
    def create_label(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(int(self.data["x"].item()), int(self.data["y"].item()))
        self.turtle.write(
            f"{self.data["state"].item()}",
            align="center",
            font=("Courier", 8, "normal")
        )