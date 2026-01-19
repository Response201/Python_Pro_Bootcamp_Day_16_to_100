from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.create_car()
        self.cars=[]

    # Skapa en bil slumpmässigt
    def create_car(self):
        random_gen_car = random.randrange(1,6)
        if random_gen_car == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.goto(300,random.randrange(-250,250, 10) )
            self.cars.append(car)

    # Flytta alla bilar
    def move_cars(self):

        for car in self.cars:
            car.goto(car.xcor() - MOVE_INCREMENT, car.ycor())



