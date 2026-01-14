from turtle import *
from snake import *
from food import *
from scoreboard import *
from text import *

class Game(ScoreBoard,TextWriter,Snake, Food):
   def __init__(self):
       super().__init__()



# Kollar om maten tagits
   def check_food_eaten(self):
       if self.snake_head_x == self.food_item.xcor() and self.snake_head_y == self.food_item.ycor():
           self.add_snake_part()
           self.new_position_food()
           self.increment_score()


# Visar "game over" på skärmen med en Turtle
   def game_over_text(self):
       self.write_text("GAME OVER", 0, 0, 24, "bold")


# Kontrollerar om spelet är över. Ormen träffar en vägg eller sig själv
   def game_over(self):
       neg_screen = -300
       pos_screen = 300

       # Kontrollera om ormens huvud har gått utanför spelområdet
       if (self.snake_head_x <= neg_screen or
           self.snake_head_x >= pos_screen or
           self.snake_head_y  <= neg_screen or
           self.snake_head_y >= pos_screen) :
           return False

       # Kontrollera om ormens huvud kolliderar med någon del av kroppen
       for item in self.snake[1:]:
                    x = item.xcor()
                    y = item.ycor()
                    if x == self.snake_head_x and y == self.snake_head_y:

                        return False

       return True