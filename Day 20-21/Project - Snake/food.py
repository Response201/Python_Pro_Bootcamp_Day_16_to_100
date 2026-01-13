from turtle import *
import random



class Food:
    def __init__(self):
        self.food_item = []
        self.food_position_x= 0
        self.food_position_y = 0
        self.create_food()
        self.new_position_food()


 # Skapar Turtle för maten
    def create_food(self):

        food = Turtle()
        food.shape("square")
        food.color("green")
        food.shapesize(0.5)
        food.penup()
        self.food_item.append(food)
        self.new_position_food()

    # Flyttar maten till en slumpmässig position
    def new_position_food(self):
        self.food_position_x = random.randrange(-290, 291, 10)
        self.food_position_y = random.randrange(-290, 291, 10)

        if self.food_item:
            self.food_item[0].goto(self.food_position_x, self.food_position_y)


