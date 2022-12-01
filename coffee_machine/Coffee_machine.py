from Data import *
from time import *
import random
clear()
On = False
existing = True
repeater = True
while existing == True:
    while On == True:
        clear()
        choice = input("Would you like an espresso, a latte or a cappuccino?\n")
        if choice == "Off":
            On = False
            clear()
            shutdown()
            clear()
        elif choice == "settings":
            clear()
            if password_checker() == "password_error":
                On = False
                clear()
                continue     
        elif choice == "latte":
            price = price_latte()
            if price == "type error":
                continue
            elif price < 0:
                change = price*-1
                change = round(change, 2)
                print("Your change is", change, "Dollars")
            elif price > 0:
                print("This was not enough money!\nTry again")
                continue
            latte = less_resources_latte()
            if latte == "error":
                sleep(2)
                continue
            sleep(2)
            print("Enjoy your Latte!")
            sleep(2)
        elif choice == "espresso":
            price = price_espresso()
            if price == "type error":
                continue
            elif price < 0:
                change = price*-1
                change = round(change, 2)
                print("Your change is", change, "Dollars")
            elif price > 0:
                print("This was not enough money!\nTry again")
                continue
            espresso = less_resources_espresso()
            if espresso == "error":
                sleep(2)
                continue
            sleep(2)
            print("Enjoy your espresso!")
            sleep(2)
        else:
            price = price_cappuccino()
            if price == "type error":
                continue
            elif price < 0:
                change = price*-1
                change = round(change, 2)
                print("Your change is", change, "Dollars")
            elif price > 0:
                print("This was not enough money!\nTry again")
                continue
            cappuccino = less_resources_cappuccino()
            if cappuccino == "error":
                sleep(2)
                continue
            sleep(2)
            print("Enjoy your cappuccino!")
            sleep(2)
    On_Off = input("")
    if On_Off == "On":
        clear()
        startup()
        On = True
        clear()
        sleep(random.random())