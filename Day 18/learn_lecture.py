"""Day 18 – Turtle & GUI (Korta anteckningar)
Turtle – grunder

Används för enkel grafik & GUI-tänk

import turtle
tim = turtle.Turtle()
screen = turtle.Screen()



Rörelse
tim.forward(100)
tim.left(90)




Penna & stil
tim.penup()
tim.pendown()
tim.color("red")
tim.pensize(5)




Loop – former
for _ in range(4):
    tim.forward(100)
    tim.left(90)




Random Walk
import random
directions = [0, 90, 180, 270]
tim.setheading(random.choice(directions))
tim.forward(30)




Events (GUI)
def move():
tim.forward(20)
screen.listen()
screen.onkey(move, "w")



Avslut
screen.exitonclick()


* Turtle = ritar
* Screen = fönster
* Loopar + events = interaktiv grafik


"""