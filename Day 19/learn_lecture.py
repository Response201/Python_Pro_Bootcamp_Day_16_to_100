
#Functions & Event Listener

from turtle import *


screen = Screen()
tim = Turtle()


def left():
    tim.forward(10)

screen.listen()
screen.onkey(left, "a")




screen.listen() # listen() startar lyssning
screen.onkey(left, "a") # onkey kopplar tangent → funktion
mainloop()  # håller programmet igång



#Varför inga parenteser?
#
#screen.onkey(fram, "Up") # rätt
#screen.onkey(fram(), "Up") # fel
#
#fram = skickar funktionen
#
#fram() = kör funktionen direkt
