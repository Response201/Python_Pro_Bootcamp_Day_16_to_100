import random
import turtle
from turtle import *
from colors import color_from_img_array
screen = Screen()
turtle.colormode(255)
new_turtle = Turtle()
new_turtle.speed(0)

def one_full_dotted_line():

    for number in range(10):
        new_turtle.forward(50)
        new_turtle.dot(20,random.choice(color_from_img_array))


start_position = -275
new_turtle.penup()
new_turtle.hideturtle()


for number in range(10):
    start_position +=50
    new_turtle.goto(-275,start_position)
    one_full_dotted_line()



screen.exitonclick()
















