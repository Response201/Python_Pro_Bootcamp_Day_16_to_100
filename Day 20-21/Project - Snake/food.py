from turtle import Turtle
import random

class Food:
    def __init__(self):
        self.food_item = Turtle()
        self.food_item.shape("square")
        self.food_item.shapesize(0.5)
        self.food_item.penup()
        self.food_position_x = 0
        self.food_position_y = 0
        self.colors ="green"
        self.new_position_food()
        self.random_color()


    # Skapar en slumpad RGB-färg
    def random_color(self):
            colors = []
            for _ in range(3):
                colors.append(random.randint(20, 245))

            return colors

    # Flyttar maten till en slumpmässig position
    def new_position_food(self):
        self.food_position_x = random.randrange(-280, 281, 10)
        self.food_position_y = random.randrange(-280, 281, 10)
        self.colors = self.random_color()
        self.food_item.color(self.colors)
        self.food_item.goto(self.food_position_x, self.food_position_y)
