from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
from numpy import *
import keyboard

X1 = 623
Y1 = 500
X2 = 705
Y2 = 500
X3 = 787
Y3 = 500
X4 = 870
Y4 = 500

Button1 = (X1, Y1)
Button2 = (X2, Y2)
Button3 = (X3, Y3)
Button4 = (X4, Y4)
Buttons = [Button1, Button2, Button3, Button4]

time.sleep(4)

def tile_grab():
    for button in Buttons:
        box = (button[0], button[1]+15, button[0] + 70, button[1] + 20)
        Image = ImageOps.grayscale(ImageGrab.grab(box))
        color = array(Image.getcolors())
        if color.sum() <= 380:
            pyautogui.leftClick(button[0]+40, button[1] + 30)

'''def gameOver_grab():
    box2 = (X3, Y3, X3 + 100, Y3 + 5)
    Image2 = ImageOps.grayscale(ImageGrab.grab(box2))
    color2 = array(Image2.getcolors())
    print (color2.sum())
    if color2.sum() >= 830:
        return True
    else:
        return False'''


#restartGame()   
print('Ready!')

while True:
    tile_grab()
    #restarter = gameOver_grab()
    if keyboard.is_pressed('x'):
        exit()
    #elif restarter:
    #    restartGame()