from turtle import *
import random


screen = Screen()
screen.setup(500,600)
no_winner=False
colors =["red", "blue", "green", "yellow", "pink"]
turtles = []


bet = screen.textinput("Make your bet", "Which turtle is going to win? Red, Green, Blue, Yellow or Pink?")



for color in colors:
    new_turtle = Turtle()
    new_turtle.hideturtle()
    turtles.append({"turtle": new_turtle, "color": color, "score": 0})



start_position = -200
for t in turtles:
        t["turtle"].hideturtle()
        t["turtle"].penup()
        t["turtle"].goto(-230, start_position)
        start_position+=100
        t["turtle"].color(t["color"])
        t["turtle"].shape("turtle")
        t["turtle"].showturtle()




def move_forward(turtle,this):

    random_move = int(random.randint(1,10))
    turtle.forward(random_move)
    for turtle in turtles:
        if turtle["color"] == this:
            turtle["score"] += random_move


def find_winner():
    for turtle in turtles:
        if  turtle["score"] >=440:
            return turtle["color"].title()





if bet :
    no_winner =True


while no_winner:
        win = find_winner()
        if win:
            no_winner=False
            if win == bet.title():
                print(f"🎉 Congratulations! You guessed correctly. The winner is {win}!")
            else:
                print(f"Sorry, your bet was {bet.title()}. The winner is {win}. Better luck next time!")

        for t in turtles:
            move_forward(t["turtle"], t["color"])






screen.exitonclick()