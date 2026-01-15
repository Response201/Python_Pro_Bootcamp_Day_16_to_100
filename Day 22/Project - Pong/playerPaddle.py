from turtle import Turtle


class PlayerPaddle:
    def __init__(self,startposition):

        # Skapa paddel
        self.board=Turtle()
        self.board_length = 5
        self.board.penup()
        self.board.shape("square")
        self.board.color("white")
        self.board.shapesize(1)
        self.board.goto(startposition)
        self.board.shapesize(stretch_wid=self.board_length, stretch_len=1)

        # Kontroll
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

        if self.moving_up and y < 330:
            self.board.sety(y + 10)

        if self.moving_down and y > -320:
            self.board.sety(y - 10)