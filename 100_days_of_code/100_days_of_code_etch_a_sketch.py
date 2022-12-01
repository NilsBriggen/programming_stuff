from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(10)
def move_backwards():
    t.backward(10)
def clockwise():
    t.right(5)
def anticlockwise():
    t.left(5)
def clear():
    t.penup()
    t.home()
    t.pendown()
    t.clear()


screen.listen()
screen.onkeypress(move_forwards, "Up")
screen.onkeypress(move_backwards, "Down")
screen.onkeypress(anticlockwise, "Left")
screen.onkeypress(clockwise, "Right")
screen.onkeypress(move_forwards, "w")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(anticlockwise, "a")
screen.onkeypress(clockwise, "d")
screen.onkeypress(clear, "c")
screen.exitonclick()