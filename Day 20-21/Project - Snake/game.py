from turtle import *

class Game:
   def __init__(self):
       self.score= 0
       self.score_item =[]

# Skapar Turtle som används för att visa poängen
   def create_score_text(self):

        display_score = Turtle()
        display_score.hideturtle()
        display_score.penup()
        display_score.color("white")
        display_score.goto(0, 260)
        self.score_item.append(display_score)
        self.write_score()

# Uppdaterar och skriver poängen på skärmen
   def write_score(self):
            if self.score_item[0]:
                self.score_item[0].clear()
            self.score_item[0].write(
                f"Score: {self.score}",
                align="center",
                font=("Arial", 16, "normal")
            )

# Visar "game over" på skärmen med en Turtle
   def game_over_text(self):
       display_text = Turtle()
       display_text.hideturtle()
       display_text.penup()
       display_text.color("white")
       display_text.goto(0, 0)  # placera först

       display_text.write(
           "GAME OVER",
           align="center",
           font=("Arial", 24, "bold")
       )


# Kontrollerar om spelet är över. Ormen träffar en vägg eller sig själv
   def game_over(self, snake,snake_head_x, snake_head_y):

       neg_screen = -300
       pos_screen = 300

       # Kontrollera om ormens huvud har gått utanför spelområdet
       if (snake_head_x <= neg_screen or
           snake_head_x >= pos_screen or
           snake_head_y  <= neg_screen or
           snake_head_y >= pos_screen) :
           return False

       # Kontrollera om ormens huvud kolliderar med någon del av kroppen
       for item in snake[1:]:
                    x = item.xcor()
                    y = item.ycor()
                    if x == snake_head_x and y == snake_head_y:

                        return False

       return True

