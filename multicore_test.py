from multiprocessing import *
import math

lösung = []
x=0

def cruncher(x):
    for a in range(1, 100000000):
        lösung = []
        a+=x
        number1 = math.sqrt(a)
        if number1 % 1 == 0:
            lösung.append(a)
    print("lösung:", lösung)

if __name__ == '__main__':
    with Pool(5) as p:
        p.map(cruncher, [0, 100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000])
