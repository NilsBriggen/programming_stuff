import turtle
from random import randint

class Ball():
    def __init__(self):
        self.ball = turtle.Turtle("circle")
        self.ball.penup()
        self.ball.color("white")
        self.ball.resizemode("user")
        self.ball.shapesize(2, 2, 2)
    
    def reboundx(self):
        h = self.ball.heading()
        newh = 180 - h + randint(-20, 20)
        self.ball.seth(newh)
        self.ball.fd(20)
        turtle.Screen().update()

    def reboundy(self):
        h = self.ball.heading()
        newh = -h + randint(-20, 20)
        self.ball.seth(newh)
        self.ball.fd(10)
        turtle.Screen().update()

    def reset1(self):
        self.ball.goto(0, 0)
        self.ball.seth(randint(-135, -45))

    def reset2(self):
        self.ball.goto(0, 0)
        self.ball.seth(randint(45, 135))