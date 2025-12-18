from turtle import *

screen = Screen()
new_turtle = Turtle()

def move_forward():
    new_turtle.forward(40)

def turn_left():
    new_turtle.left(90)
    move_forward()

def turn_right():
    new_turtle.right(90)
    move_forward()

def clear():
    new_turtle.penup()
    new_turtle.clear()
    new_turtle.home()

    new_turtle.pendown()


screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c", )

screen.mainloop()