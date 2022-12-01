import threading
import time
import math
result = []
lösung = []
result2 = []
lösung2 = []
result3 = []
lösung3 = []
result4 = []
lösung4 = []
result5 = []
lösung5 = []
duration = 0

def first():
    for a in range(1, 99999999):
        #number1 = a/3456
        number1 = math.sqrt(a)
        if number1 % 1 == 0:
            result.append(number1)
            lösung.append(a)
    print("result:", result,"\n\nLösungszahlen:", lösung)

def second():
    for b in range(100000000, 199999999):
        #number2 = b/3456
        number2 = math.sqrt(b)
        if number2 % 1 == 0:
            result2.append(number2)
            lösung2.append(b)
    time.sleep(2)
    print("\n\nresult2:", result2, "\n\nLösungszahlen", lösung2)

def third():
    for c in range(200000000, 299999999):
        #number3 = c/3456
        number3 = math.sqrt(c)
        if number3 % 1 == 0:
            result3.append(number3)
            lösung3.append(c)
    time.sleep(4)
    print("\n\nresult3:", result4, "\n\nLösungszahlen", lösung4)

def fourth():
    for d in range(300000000, 399999999):
        #number4 = d/3456
        number4 = math.sqrt(d)
        if number4 % 1 == 0:
            result4.append(number4)
            lösung4.append(d)
    time.sleep(6)
    print("\n\nresult4:", result4, "\n\nLösungszahlen", lösung4)

def fifth():
    for e in range(400000000, 499999999):
        #number5 = e/3456
        number5 = math.sqrt(e)
        if number5 % 1 == 0:
            result5.append(number5)
            lösung5.append(e)
    time.sleep(8)
    print("\n\nresult5:", result5, "\n\nLösungszahlen", lösung5)
    global duration
    duration = time.process_time()
    print("dauer:", duration)

def runner():
    threading.Thread(target=first).start()
    threading.Thread(target=second).start()
    threading.Thread(target=third).start()
    threading.Thread(target=fourth).start()
    threading.Thread(target=fifth).start()
runner()
