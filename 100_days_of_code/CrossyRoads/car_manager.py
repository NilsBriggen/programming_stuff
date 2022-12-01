import random
from turtle import Turtle, Screen
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 1
LANES = [-250, -225, -200, -175, -150, -125, -100, -75, -50, -25, 0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250]


class CarManager:
    def __init__(self, level):
        self.level = level
        self.cars = []
        self.create_car()

    def move(self):
        speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (self.level-1)
        for car in self.cars:
            car.forward(speed)

    def create_car(self):
        for _ in range(1, 1000):
            self.add_car()
        Screen().update()

    def add_car(self):
        t = Turtle('square')
        t.resizemode('user')
        Screen().colormode(255)
        t.shapesize(0.5, 1)
        t.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        t.penup()
        t.goto((round(random.randint(-10000, 300)-1), random.choice(LANES)))
        self.cars.append(t)
