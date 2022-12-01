from turtle import Turtle, Screen
screen = Screen()
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.startX = 0
        self.startY = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(3):
            self.add_segment()
        screen.update()

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self):
        t = Turtle('square')
        t.color('white')
        t.penup()
        t.goto(self.startX, self.startY)
        self.startX -= 20
        self.segments.append(t)
    
    def extend(self):
        t = Turtle('square')
        t.color('white')
        t.penup()
        t.goto(self.segments[-1].position())
        self.segments.append(t)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
            screen.update()

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
            screen.update()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
            screen.update()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
            screen.update()