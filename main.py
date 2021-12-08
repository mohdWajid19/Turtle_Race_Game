from turtle import Turtle,Screen
import random as r

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="make ur bet",prompt="Enter the colour of the turtle")
all_turtles = []
colors = ["red","blue","orange","yellow","purple","green"]
y_pos = [-70,-40,-10,20,50,80]
is_game_on = False
for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x = -230, y = y_pos[i])
    new_turtle.speed("fastest")
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winner = turtle.pencolor()
            if user_bet.lower() == winner:
                print(f"You've won the bet, the winner turtle is {winner}") 
            else:
                print(f"You've lost the bet, the winner turtle is {winner}") 
        turtle.forward(r.randint(0,10))



screen.exitonclick()