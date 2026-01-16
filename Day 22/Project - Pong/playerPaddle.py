from turtle import Turtle
from ball import Ball


class PlayerPaddle(Ball):

    def __init__(self,startposition,ball, scoreboard):

        # Skapa paddel
        self.board=Turtle()
        self.board_length = 5
        self.board.penup()
        self.board.shape("square")
        self.board.color("white")
        self.board.goto(startposition)
        self.board.shapesize(stretch_wid=self.board_length, stretch_len=1)
        self.board_space= [self.board.xcor(), self.board.ycor()  ]

        # Bollen och poängtavlan
        self.ball = ball
        self.scoreboard = scoreboard


        # Kontroller
        self.moving_up = False
        self.moving_down = False


    # start_* körs när spelaren trycker ner en tangent,
    # stop_* körs när spelaren släpper tangenten
    def start_up(self):
        self.moving_up = True

    def stop_up(self):
        self.moving_up = False

    def start_down(self):
        self.moving_down = True

    def stop_down(self):
        self.moving_down = False



    # Uppdaterar paddlens position och hindrar den från att lämna spelområdet
    def update(self):
        y = self.board.ycor()

        if self.moving_up and y < 350:
            self.board.sety(y + 10)

        if self.moving_down and y > -340:
            self.board.sety(y - 10)

        self.board_space = [self.board.xcor(), self.board.ycor() ]


    # Kontrollerar om paddeln träffar bollen -> isf ge poäng och studsa tillbaka bollen
    def check_hit_ball(self):
      if ( self.ball.x >= self.board.xcor() - 20 and
         self.ball.x <= self.board.xcor() + 20 and
         self.ball.y >= self.board.ycor() - 50 and
        self.ball.y <= self.board.ycor() + 50):

          self.ball.bounce_paddle()
          self.scoreboard.add_point()
