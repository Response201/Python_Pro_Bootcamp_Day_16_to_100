from turtle import Turtle
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Scoreboard):

    def __init__(self):
        super().__init__()
        self.player = Turtle()
        self.player.shape("turtle")
        self.player.left(90)
        self.player.color("green")
        self.player.penup()
        self.player.goto(STARTING_POSITION)
        self.player_positon_x=0
        self.player_positon_y = -280


    # Uppdatera spelarens position
    def new_player_position(self):
       self.player_positon_x = self.player.xcor()
       self.player_positon_y = self.player.ycor()


    def forward(self):
        self.player.goto(self.player.xcor(), self.player.ycor() + MOVE_DISTANCE)
        self.new_player_position()

    def left(self):
        if self.player.xcor() >=-280:
            self.player.goto(self.player.xcor() - MOVE_DISTANCE, self.player.ycor())
            self.new_player_position()

    def right(self):
        if self.player.xcor() <= 270:
            self.player.goto(self.player.xcor() + MOVE_DISTANCE, self.player.ycor())
            self.new_player_position()

    # Kontrollerar om spelare når nästa level -> flyttar spelaren till start position, rensar scoreboard och skriver ut ny nådd level
    def next_level(self):
        if self.player.ycor() >= FINISH_LINE_Y:
            self.player.goto(STARTING_POSITION)
            self.clear_scoreboard()
            self.write_scoreboard()


