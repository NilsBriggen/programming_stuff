import turtle
import random

t = turtle.Turtle()
turtle.colormode(255)
t.pensize(20)
t.speed(-1)
t.penup()
turtle.screensize(700, 700)
t.ht()

#-------------------------------

colors = [(21, 114, 173), (142, 163, 184), (204, 137, 166), (190, 173, 17), (145, 17, 32), (238, 213, 62), (67, 24, 31), (17, 138, 59), (219, 161, 88), (122, 71, 100), (49, 29, 26), (197, 65, 28), (7, 107, 64), (227, 169, 197), (240, 78, 29), (29, 177, 84), (21, 172, 188), (243, 214, 4)]

t.setpos(-200, -200)
for h in range(1, 11):
    for l in range(1, 11):
        t.dot(20, colors[random.randint(0, 17)])
        t.forward(50)
    t.setpos(-200, t.ycor()+50)


#-------------------------------

screen = turtle.Screen()
screen.exitonclick()