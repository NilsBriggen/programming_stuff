from random import *
import multiprocessing

numbers = []
work_load_config = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000]

def work_load(num):
    for a in range(num-2000, num):
        numbers.append(a)

def pool():
    p=multiprocessing.Pool(8)
    p.map(work_load, work_load_config)
    p.close

if __name__=='__main__':
    pool()

shuffle(numbers)
print(numbers)