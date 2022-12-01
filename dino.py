from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
from numpy import *
import keyboard

X = 1900
Y = 800
X2 = 1308
Y2 = 750
X3 = 1850
Y3 = 700

REPLAYBTN = (X, Y)
DINO = (X2, Y2)

time.sleep(4)

def restartGame():
    pyautogui.click(REPLAYBTN)

def cactus_grab():
    time.sleep(4.1)
    box = (DINO[0]+25, DINO[1], DINO[0] + 115, DINO[1] + 5)
    Image = ImageOps.grayscale(ImageGrab.grab(box))
    color = array(Image.getcolors())
    if color.sum() >= 700:
        return True
    else:
        return False

def gameOver_grab():
    box2 = (X3, Y3, X3 + 100, Y3 + 5)
    Image2 = ImageOps.grayscale(ImageGrab.grab(box2))
    color2 = array(Image2.getcolors())
    print (color2.sum())
    if color2.sum() >= 830:
        return True
    else:
        return False


restartGame()   

while True:
    activator = cactus_grab()
    restarter = gameOver_grab()
    if keyboard.is_pressed('x'):
        exit()
    elif restarter:
        restartGame()
    elif activator:
        keyboard.send('space')



        
    