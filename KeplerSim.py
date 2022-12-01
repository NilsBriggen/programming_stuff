import turtle, time
from math import sqrt

def UnitConverter(x):
    x = (x/((6376*10**6)*2))*300
    return x

DELTA_T = 2000
g = 6.67408 * 10**(-11)
m = 3.98*10**14
x = 6376*10**6
y = 0
vx = 0
vy = 7904
r = sqrt(x**2 + y**2)

G = UnitConverter(g)
M = UnitConverter(m)
x = UnitConverter(x)
vy = UnitConverter(vy)
r = UnitConverter(r)

print(G, M, x, vy)

# Set up the screen
screen = turtle.Screen()
screen.setup(600, 600)
screen.setworldcoordinates(-300, -300, 300, 300)
screen.bgcolor("black")
screen.title("Kepler")

# Create the turtles
creator = turtle.Turtle()
creator.shape("circle")
creator.color("white")
creator.hideturtle()

earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue")
earth.pendown()
earth.pensize(2)

#Draw the sun
creator.penup()
creator.setpos(0, 0)
creator.dot(20, "yellow")

while True:
    #Move the earth
    ax = (-((G * M)/r**3))*x
    ay = (-((G * M)/r**3))*y
    vx = ax * DELTA_T + vx
    vy = ay * DELTA_T + vy
    x = vx * DELTA_T + x
    y = vy * DELTA_T + y
    r = sqrt(x**2 + y**2)

    earth.speed(-1)
    earth.goto(x, y)
    print(x, y)
    #time.sleep(0.000001)
