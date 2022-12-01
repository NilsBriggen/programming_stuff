from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
from numpy import *
import multiprocessing
import keyboard

# Record: 746



X1 = 611
Y1 = 667
X2 = 715
Y2 = 667
X3 = 819
Y3 = 667
X4 = 921
Y4 = 667

Button1 = (X1, Y1)
Button2 = (X2, Y2)
Button3 = (X3, Y3)
Button4 = (X4, Y4)
Buttons = [Button1, Button2, Button3, Button4]
numbers = [0, 1, 2, 3]

time.sleep(4)
turns = 0
turns2 = 0
seconds1 = 120
seconds2 = 170

def converter(seconds):
    global turns
    turns = int((seconds/5)*40)
    #print(turns)
def converter2(seconds):
    global turns2
    turns2 = int((seconds/5)*40)
    #print(turns2)

converter(seconds1)
converter2(seconds2)

def tile_grab(i):
    a = 0
    b = 0
    while True:
        a += 1
        button = Buttons[i]
        box = (button[0], button[1], button[0] + 50, button[1] + 5)
        Image = ImageOps.grayscale(ImageGrab.grab(box))
        color = array(Image.getcolors())
        if color.sum() <= 600:
            pyautogui.leftClick(button[0]+35, button[1] + 60 + b)
        #if a%10 == 0:

        if keyboard.is_pressed('c'):
            print(color.sum())
            exit()
        if a == turns or a == turns2:
            b+=60
            print('UPGRADES PEOPLE!!!')
        if keyboard.is_pressed('x'):
            exit()

print('Ready!')

def par_process():
    pool = multiprocessing.Pool(4)
    pool.map(tile_grab, numbers)
    pool.close()

if __name__ == '__main__':    
    par_process()
