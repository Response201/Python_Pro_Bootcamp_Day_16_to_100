from turtle import Turtle, Screen
import turtle
from Project import colors
new_turtle = Turtle()
screen = Screen()

# Challenge 1 Draw a square
#new_turtle.position()
#for item in range(4):
#    new_turtle.forward(200)
#    new_turtle.right(90)


# Challenge 2 Draw a dashed line
#for item in range(4):
#    for draw in range(10):
#        new_turtle.forward(10)
#        new_turtle.penup()
#        new_turtle.forward(10)
#        new_turtle.pendown()
#
#    new_turtle.right(90)





# Challenge 3 Drawing different shapes
#sides = 3
#
#def draw_shape(num_sides):
#    for i in range(sides):
#        angle = 360 / num_sides
#        new_turtle.forward(100)
#        new_turtle.right(angle)
#
#
#for item in range(7):
#    new_turtle.color(random.choice(colors.colorArray))
#    draw_shape(sides)
#    sides +=1




# Challenge 4 Draw a random walk
#turtle.colormode(255)
#new_turtle.shape("turtle")
#new_turtle.pensize(10)
#
#for item in range(50):
#    new_turtle.color(colors.random_color())
#    new_turtle.setheading(random.choice([0,90,180,270]))
#    new_turtle.forward(30)





# Challenge 5 Make a spirograph

turtle.colormode(255)
new_turtle.speed("fastest")

def shape():

  new_turtle.hideturtle()
  new_turtle.circle(100)
  new_turtle.showturtle()
  turtle.update()


def draw(gap):

     for item in range(int(360 / gap)):

        new_turtle.color(colors.random_color())
        shape()
        cu = new_turtle.heading()
        new_turtle.setheading(cu + gap)
        new_turtle.tiltangle()



draw(5)


screen.exitonclick()