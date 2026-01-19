from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard:

    def __init__(self):
        self.level = 1
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(-245,270)
        self.write_scoreboard()

    # Rensa poängskärmen och öka level
    def clear_scoreboard(self):
        self.scoreboard.clear()
        self.level += 1

    # Skriver ut level
    def write_scoreboard(self):

        self.scoreboard.write(f"Level: {self.level}", align="center", font=FONT)





