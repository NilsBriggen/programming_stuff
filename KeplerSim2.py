import time, pygame
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

print(x, vy)

pygame.init()
pygame.display.set_mode((600, 600))
pygame.display.set_caption("Kepler")
pygame.coordinates

#draw the sun
pygame.draw.circle(screen, (255, 255, 0), (300, 300), 20)

#draw the earth
pygame.draw.circle(screen, (0, 0, 255), (int(x), int(y)), 10)

while True:
#Move the earth
    x_old = x
    y_old = y
    ax = (-((G * M)/r**3))*x
    ay = (-((G * M)/r**3))*y
    vx = ax * DELTA_T + vx
    vy = ay * DELTA_T + vy
    x = vx * DELTA_T + x
    y = vy * DELTA_T + y
    r = sqrt(x**2 + y**2)

    #delete previous earth
    pygame.draw.circle(screen, (0, 0, 0), (int(x_old), int(y_old)), 10)

    #draw the earth
    pygame.draw.circle(screen, (0, 0, 255), (int(x), int(y)), 10)
    pygame.display.update()
    time.sleep(0.2)

