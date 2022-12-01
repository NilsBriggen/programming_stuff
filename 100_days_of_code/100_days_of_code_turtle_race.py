from operator import is_
from tkinter import messagebox
import turtle as t
from random import randint

screen = t.Screen()
is_race_on = False
screen.setup(width=500, height=400)
colors = ["yellow", "orange", "red", "green", "purple", "blue"]
starting_point = -125
user_bet = screen.textinput("Chose your racer", "Chose the turtle you think will win. Enter a color: ")
turtles = []
print (user_bet)

for number in range(0, 6):
    turtle = t.Turtle("turtle")
    turtle.fillcolor(colors[number])
    turtle.penup()
    turtle.setpos(y=starting_point,x=-230)
    starting_point += 50
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on == True:
    for turtle in turtles:
        if turtle.xcor() >= 230.0 and is_race_on == True:
            winner = turtle.fillcolor()

            if winner == "yellow":
                transmit = "Yellow"
            elif winner == "orange":
                transmit = "Orange"
            elif winner == "red":
                transmit = "Red"
            elif winner == "green":
                transmit = "Green"
            elif winner == "purple":
                transmit = "Purple"
            elif winner == "blue":
                transmit = "Blue"

            if winner == user_bet:
                messagebox.showinfo("You've won!", f"Congratulations! You're guess was right. {transmit} has won!")
            else:
                messagebox.showinfo("You've lost!", f"You didn't guess right. {transmit} has won!")
            is_race_on = False
        distance = randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()