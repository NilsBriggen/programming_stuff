from turtle import Screen
from white import White
import os
import ctypes
user32 = ctypes.windll.user32
screenwidth = user32.GetSystemMetrics(0)
screenheight = user32.GetSystemMetrics(1)
white = White()

currentDir = os.getcwd()

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width = 1.0, height = 1.0, startx=0, starty=0)
screen.title("Chess")
screen.bgpic(currentDir+'\\resources\\background.png')

#white.walk()

screen.mainloop()

#Icons by https://www.flaticon.com/authors/deemakdaksina