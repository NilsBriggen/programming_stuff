import time
from math import sqrt
from matplotlib import pyplot as plt

def UnitConverter(x):
    x = (x/((6376*10**6)*2))*300
    return x

DELTA_T = 2000
G = UnitConverter(6.67408 * 10**(-11))
M = UnitConverter(3.98*10**14)
x = UnitConverter(6376*10**6)
y = 0
vx = 0
vy = UnitConverter(7904)
r = sqrt(x**2 + y**2)

#Plot the sun
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 6))
ax.plot(0, 0, 'yo', markersize=20)

#Plot the earth
x_results = []
y_results = []
for i in range(1000):
    ax = (-((G * M)/r**3))*x
    ay = (-((G * M)/r**3))*y
    vx = ax * DELTA_T + vx
    vy = ay * DELTA_T + vy
    x = vx * DELTA_T + x
    y = vy * DELTA_T + y
    r = sqrt(x**2 + y**2)
    x_results.append(x)
    y_results.append(y)

#plot graph
ax.plot(x_results, y_results, 'bo', markersize=5)
