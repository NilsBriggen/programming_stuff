from os import system, name
def clear():
    system('cls' if name=='nt' else 'clear')
from time import *
import random

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0

def less_resources_espresso():
    global water
    global milk
    global coffee
    global money
    water -= MENU["espresso"]["ingredients"]["water"]
    coffee -= MENU["espresso"]["ingredients"]["coffee"]
    money += MENU["espresso"]["cost"]
    if water < 0 or coffee < 0:
        water += MENU["espresso"]["ingredients"]["water"]
        coffee += MENU["espresso"]["ingredients"]["coffee"]
        money -= MENU["espresso"]["cost"]
        print("The machine doesn't have enough ingredients to make your coffee!\nPlease refill")
        return "error"
    return water, milk, coffee, money

def less_resources_latte():
    global water
    global milk
    global coffee
    global money
    water -= MENU["latte"]["ingredients"]["water"]
    milk -= MENU["latte"]["ingredients"]["milk"]
    coffee -= MENU["latte"]["ingredients"]["coffee"]
    money += MENU["latte"]["cost"]
    if water < 0 or milk < 0 or coffee < 0:
        water += MENU["latte"]["ingredients"]["water"]
        milk += MENU["latte"]["ingredients"]["water"]
        coffee += MENU["latte"]["ingredients"]["coffee"]
        money -= MENU["latte"]["cost"]
        print("The machine doesn't have enough ingredients to make your coffee!\nPlease refill")
        return "error"
    return water, milk, coffee

def less_resources_cappuccino():
    global water
    global milk
    global coffee
    global money
    water -= MENU["cappuccino"]["ingredients"]["water"]
    milk -= MENU["cappuccino"]["ingredients"]["milk"]
    coffee -= MENU["cappuccino"]["ingredients"]["coffee"]
    money += MENU["cappuccino"]["cost"]
    if water < 0 or milk < 0 or coffee < 0:
        water += MENU["cappuccino"]["ingredients"]["water"]
        milk += MENU["cappuccino"]["ingredients"]["water"]
        coffee += MENU["cappuccino"]["ingredients"]["coffee"]
        money -= MENU["cappuccino"]["cost"]
        print("The machine doesn't have enough ingredients to make your coffee!\nPlease refill")
        return "error"
    return water, milk, coffee

def report():
    print("Milk:", milk)
    print("Water:", water)
    print("Coffee", coffee)
    print("Money", money)

def empty_money():
    global money
    money = 0

def password():
    return "Coffee_mkr2000"

def refill():
    global water
    global milk
    global coffee
    water = 300
    milk = 200
    coffee = 100

def price_espresso():
    print("This costs", MENU["espresso"]["cost"])
    quarters = input("How many quarters do you insert? ")
    dimes = input("How many dimes do you insert? ")
    nickles = input("How many nickles do you insert? ")
    pennies = input("How many pennies do you insert? ")
    for char in letters:
        if char in quarters or char in dimes or char in nickles or char in pennies:
            print("You can't use letters for this!\nTry again")
            sleep(2)
            return "type error"
    else:
        quarters = int(quarters)
        dimes = int(dimes)
        nickles = int(nickles)
        pennies = int(pennies)
        price = MENU["espresso"]["cost"]
        quarter = quarters/4
        dime = dimes/10
        nickle = nickles/20
        penny = pennies/100
        price -= quarter + dime + nickle + penny
        return price

def price_latte():
    print("This costs", MENU["latte"]["cost"])
    quarters = input("How many quarters do you insert? ")
    dimes = input("How many dimes do you insert? ")
    nickles = input("How many nickles do you insert? ")
    pennies = input("How many pennies do you insert? ")
    for char in letters:
        if char in quarters or char in dimes or char in nickles or char in pennies:
            print("You can't use letters for this!\nTry again")
            sleep(2)
            return "type error"
    else:
        quarters = int(quarters)
        dimes = int(dimes)
        nickles = int(nickles)
        pennies = int(pennies)
        price = MENU["espresso"]["cost"]
        quarter = quarters/4
        dime = dimes/10
        nickle = nickles/20
        penny = pennies/100
        price -= quarter + dime + nickle + penny
        return price

def price_cappuccino():
    print("This costs", MENU["cappuccino"]["cost"])
    quarters = input("How many quarters do you insert? ")
    dimes = input("How many dimes do you insert? ")
    nickles = input("How many nickles do you insert? ")
    pennies = input("How many pennies do you insert? ")
    for char in letters:
        if char in quarters or char in dimes or char in nickles or char in pennies:
            print("You can't use letters for this!\nTry again")
            sleep(2)
            return "type error"
    else:
        quarters = int(quarters)
        dimes = int(dimes)
        nickles = int(nickles)
        pennies = int(pennies)
        price = MENU["espresso"]["cost"]
        quarter = quarters/4
        dime = dimes/10
        nickle = nickles/20
        penny = pennies/100
        price -= quarter + dime + nickle + penny
        return price

def setting():
    in_setting = True
    while in_setting == True:
        settings = input("settings: ")
        if settings == "":
            in_setting = False
        elif settings == "help":
            print("With 'refill' the resources get filled up\nWith 'report' the machine prints how much resources are left in the system and how much money it collected\nWith 'empty money' You can take the money")
            sleep(10)
            clear()
        elif settings == "refill":
            refill()
            clear()
            refilling()
            clear()
        elif settings == "report":
            clear()
            data_collecter()
            clear()
            report()
            sleep(5)
            clear()
        elif settings == "empty money":
            print(f"Do you want to take", money, "Dollars? 'y' or 'n'")
            take_money = input("")
            if take_money == "y":
                clear()
                emptier()
                empty_money()
                clear()
            else:
                clear()
        else:
            print(settings, "is not a term")
            sleep(2)
            clear()

def password_checker():
    if True == True:
        if True == True:
            guesses = 0
            repeater = True
            while repeater == True:
                user_guess = input("Password: ")
                real_password = password()
                if user_guess == real_password:
                    clear()
                    settings_loader()
                    clear()
                    setting()
                    repeater = False
                elif user_guess == "cancel":
                    cancelling()
                    repeater = False
                else:
                    guesses += 1
                    if guesses == 3:
                        clear()
                        print("You guessed the password", guesses, "times wrong!\nThe machine will not be useable for", guesses/3*10, "seconds")
                        sleep(guesses/3*10)
                    elif guesses == 6:
                        print("You guessed the password", guesses, "times wrong!\nThe machine will not be useable for", guesses/3*10, "seconds")
                        sleep(guesses/3*10)
                        clear()
                    elif guesses == 9:
                        print("You guessed the password", guesses, "times wrong!\nThe machine will not be useable for", guesses/3*10, "seconds")
                        sleep(guesses/3*10)
                        clear()
                    elif guesses == 12:
                        print("You guessed the password", guesses, "times wrong!\nThe machine will not be useable for", guesses/3*10, "seconds")
                        sleep(guesses/3*10)
                        clear()
                    elif guesses == 15:
                        print("You guessed the password 15 times wrong!\nThe machine will now turn off!")
                        return "password_error"
                    else:
                        print("The password is wrong.\nTry again")
                        sleep(2)
                        clear()

def shutdown():
    a = 1
    while a <= 2:
        print("Shuting down.")
        sleep(random.random())
        clear()
        print("Shuting down..")
        sleep(random.random())
        clear()
        print("Shuting down...")
        sleep(random.random())
        clear()
        a += 1

def startup():
    a = 1
    while a <= 2:
        print("starting up.")
        sleep(random.random())
        clear()
        print("starting up..")
        sleep(random.random())
        clear()
        print("starting up...")
        sleep(random.random())
        clear()
        a += 1 

def refilling():
    a = 1
    while a <= 2:
        print("refilling.")
        sleep(random.random())
        clear()
        print("refilling..")
        sleep(random.random())
        clear()
        print("refilling...")
        sleep(random.random())
        clear()
        a += 1

def settings_loader():
    a = 1
    while a <= 2:
        print("loading settings.")
        sleep(random.random())
        clear()
        print("loading settings..")
        sleep(random.random())
        clear()
        print("loading settings...")
        sleep(random.random())
        clear()
        a += 1

def data_collecter():
    a = 1
    while a <= 2:
        print("collecting data.")
        sleep(random.random())
        clear()
        print("collecting data..")
        sleep(random.random())
        clear()
        print("collecting data...")
        sleep(random.random())
        clear()
        a += 1

def emptier():
    a = 1
    while a <= 2:
        print("emptying.")
        sleep(random.random())
        clear()
        print("emptying..")
        sleep(random.random())
        clear()
        print("emptying...")
        sleep(random.random())
        clear()
        a += 1

def cancelling():
    a = 1
    while a <= 1:
        clear()
        print("cancelling.")
        sleep(random.random())
        clear()
        print("cancelling..")
        sleep(random.random())
        clear()
        print("cancelling...")
        sleep(random.random())
        clear()
        a += 1