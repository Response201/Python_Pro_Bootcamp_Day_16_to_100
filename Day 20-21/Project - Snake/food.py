from turtle import Turtle
import random

class Food:
    def __init__(self):
        self.food_item = Turtle()
        self.food_item.shape("square")
        self.food_item.color("green")
        self.food_item.shapesize(0.5)
        self.food_item.penup()
        self.food_position_x = 0
        self.food_position_y = 0
        self.new_position_food()

    # Flyttar maten till en slumpmässig position
    def new_position_food(self):
        self.food_position_x = random.randrange(-290, 291, 10)
        self.food_position_y = random.randrange(-290, 291, 10)
        self.food_item.goto(self.food_position_x, self.food_position_y)
