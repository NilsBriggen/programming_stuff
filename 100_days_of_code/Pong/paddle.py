import turtle

STARTX1 = 350
STARTX2 = -350
STARTY = -50

class Paddle():
    def __init__(self):
        self.increment = 0
        self.paddle1 = []
        self.paddle2 = []
        for _ in range(5):
                obj = turtle.Turtle("square")
                obj.penup()
                obj.speed(0)
                obj.color("white")
                obj.resizemode("user")
                obj.shapesize(1, 2, 2)
                
                self.paddle1.append(obj)

        for _ in range(5):
                obj = turtle.Turtle("square")
                obj.penup()
                obj.speed(0)
                obj.color("white")
                obj.resizemode("user")
                obj.shapesize(1, 2, 2)
                
                self.paddle2.append(obj)
        
        for obj in self.paddle1:
            obj.goto(STARTX1, STARTY+self.increment)
            self.increment += 20

        for obj in self.paddle2:
            obj.goto(STARTX2, STARTY+self.increment)
            self.increment += 20

    def move_up1(self):
        if self.paddle1[4].ycor() >= 290:
            return
        else:
            for obj in self.paddle1: 
                obj.goto(obj.xcor(), obj.ycor()+20)
                turtle.Screen().update()

    def move_down1(self):
        if self.paddle1[0].ycor() <= -290:
            return
        else:
            for obj in self.paddle1:
                obj.goto(obj.xcor(), obj.ycor()-20)
                turtle.Screen().update()

    def move_up2(self):
        if self.paddle2[4].ycor() >= 290:
            return
        else:
            for obj in self.paddle2: 
                obj.goto(obj.xcor(), obj.ycor()+20)
                turtle.Screen().update()

    def move_down2(self):
        if self.paddle2[0].ycor() <= -290:
            return
        else:
            for obj in self.paddle2:
                obj.goto(obj.xcor(), obj.ycor()-20)
                turtle.Screen().update()