from tkinter.colorchooser import askcolor
import turtle

class Board():
    def __init__(self):
        self.positionx = [-400, -300, -200, -100, 0, 100, 200, 300]
        self.positiony = [400, 300, 200, 100, 0, -100, -200, -300]

        self.boardCreator = turtle.Turtle(visible=False)
        turtle.colormode(255)
        self.boardCreator.penup()
        self.boardCreator.color('white')
        self.boardCreator.speed(0)

    def draw_square(self, color):
        self.boardCreator.fillcolor(color)
        self.boardCreator.begin_fill()
        for _ in range(4):
            self.boardCreator.forward(100)
            self.boardCreator.right(90)
        self.boardCreator.end_fill()

    def draw_game(self):
        self.color1 = '#145f4b'
        self.color2 = '#fae8a8'
        for a in range(0, 8):
            self.boardCreator.goto(self.boardCreator.xcor(), self.positiony[a-1])
            for b in range(0, 8):
                self.boardCreator.goto(self.positionx[b-1], self.boardCreator.ycor())
                if a%2 == 0 and b%2 == 0:
                    self.draw_square(self.color1)
                elif a%2 == 1 and b%2 == 1:
                    self.draw_square(self.color1)
                else:
                    self.draw_square(self.color2)