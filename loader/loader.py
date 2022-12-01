#The Loader module
#Available loaders: simple loader, yeet loader, yeet loader2, loading loader, swoosh loader, number, number fast, random number

import time
import os
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

def simple_loader():
    while True:
        clear()
        print ("-")
        time.sleep(random.random())
        clear()
        print ("\ ")
        time.sleep(random.random())
        clear()
        print ("|")
        time.sleep(random.random())
        clear()
        print ("/")
        time.sleep(random.random())
        clear()
    
def yeet_loader():
    while True:
        clear()
        print ("yeet")
        time.sleep(0.1)
        clear()
        print ("Yeet")
        time.sleep(0.1)
        clear()
        print("YEet")
        time.sleep(0.1)
        clear()
        print("YEEt")
        time.sleep(0.1)
        clear()
        print("YEET")
        time.sleep(0.1)
        clear()
        print("yEET")
        time.sleep(0.1)
        clear()
        print("yeET")
        time.sleep(0.1)
        clear()
        print("yeeT")
        time.sleep(0.1)

def yeet_loader2():
    while True:
        clear()
        print("Yeet")
        time.sleep(0.3)
        clear()
        print("yEet")
        time.sleep(0.3)
        clear()
        print("yeEt")
        time.sleep(0.3)
        clear()
        print("yeeT")
        time.sleep(0.3)
    
def loading_loader():
    while True:
        clear()
        print ('''
         /$$
        | $$
        | $$
        | $$
        | $$
        | $$
        | $$$$$$$$
        |________/''')
        time.sleep(0.3)
        clear()
        print('''
         /$$                
        | $$                
        | $$        /$$$$$$ 
        | $$       /$$__  $$
        | $$      | $$  \ $$ 
        | $$      | $$  | $$ 
        | $$$$$$$$|  $$$$$$/
        |________/ \______/ ''')
        time.sleep(0.3)
        clear()
        print ('''
         /$$                          
        | $$                          
        | $$        /$$$$$$   /$$$$$$ 
        | $$       /$$__  $$ |____  $$
        | $$      | $$  \ $$  /$$$$$$$
        | $$      | $$  | $$ /$$__  $$
        | $$$$$$$$|  $$$$$$/|  $$$$$$$
        |________/ \______/  \_______/''')
        time.sleep(0.3)
        clear()
        print('''
         /$$                                 /$$
        | $$                                | $$
        | $$        /$$$$$$   /$$$$$$   /$$$$$$$
        | $$       /$$__  $$ |____  $$ /$$__  $$
        | $$      | $$  \ $$  /$$$$$$$| $$  | $$
        | $$      | $$  | $$ /$$__  $$| $$  | $$
        | $$$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$
        |________/ \______/  \_______/ \_______/''')
        time.sleep(0.3)
        clear()
        print('''
         /$$                                 /$$ /$$
        | $$                                | $$|__/
        | $$        /$$$$$$   /$$$$$$   /$$$$$$$ /$$
        | $$       /$$__  $$ |____  $$ /$$__  $$| $$
        | $$      | $$  \ $$  /$$$$$$$| $$  | $$| $$
        | $$      | $$  | $$ /$$__  $$| $$  | $$| $$
        | $$$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$
        |________/ \______/  \_______/ \_______/|__/''')
        time.sleep(0.3)
        clear()
        print('''
         /$$                                 /$$ /$$         
        | $$                                | $$|__/          
        | $$        /$$$$$$   /$$$$$$   /$$$$$$$ /$$ /$$$$$$$ 
        | $$       /$$__  $$ |____  $$ /$$__  $$| $$| $$__  $$
        | $$      | $$  \ $$  /$$$$$$$| $$  | $$| $$| $$  \ $$
        | $$      | $$  | $$ /$$__  $$| $$  | $$| $$| $$  | $$
        | $$$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$| $$  | $$
        |________/ \______/  \_______/ \_______/|__/|__/  |__/''')
        time.sleep(0.3)
        clear()
        print('''
         /$$                                 /$$ /$$                    
        | $$                                | $$|__/                    
        | $$        /$$$$$$   /$$$$$$   /$$$$$$$ /$$ /$$$$$$$   /$$$$$$ 
        | $$       /$$__  $$ |____  $$ /$$__  $$| $$| $$__  $$ /$$__  $$
        | $$      | $$  \ $$  /$$$$$$$| $$  | $$| $$| $$  \ $$| $$  \ $$
        | $$      | $$  | $$ /$$__  $$| $$  | $$| $$| $$  | $$| $$  | $$
        | $$$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$| $$  | $$|  $$$$$$$
        |________/ \______/  \_______/ \_______/|__/|__/  |__/ \____  $$
                                                               /$$  \ $$
                                                              |  $$$$$$/
                                                               \______/ ''')
        time.sleep(0.3)
        clear()
        print ('''
         /$$                                 /$$ /$$                                
        | $$                                | $$|__/                                
        | $$        /$$$$$$   /$$$$$$   /$$$$$$$ /$$ /$$$$$$$   /$$$$$$             
        | $$       /$$__  $$ |____  $$ /$$__  $$| $$| $$__  $$ /$$__  $$            
        | $$      | $$  \ $$  /$$$$$$$| $$  | $$| $$| $$  \ $$| $$  \ $$            
        | $$      | $$  | $$ /$$__  $$| $$  | $$| $$| $$  | $$| $$  | $$            
        | $$$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$| $$  | $$|  $$$$$$$ /$$
        |________/ \______/  \_______/ \_______/|__/|__/  |__/ \____  $$|__/
                                                               /$$  \ $$            
                                                              |  $$$$$$/            
                                                               \______/ ''')
        time.sleep(0.3)
        clear()
        print('''
         /$$                                 /$$ /$$                                
        | $$                                | $$|__/                                
        | $$        /$$$$$$   /$$$$$$   /$$$$$$$ /$$ /$$$$$$$   /$$$$$$             
        | $$       /$$__  $$ |____  $$ /$$__  $$| $$| $$__  $$ /$$__  $$            
        | $$      | $$  \ $$  /$$$$$$$| $$  | $$| $$| $$  \ $$| $$  \ $$            
        | $$      | $$  | $$ /$$__  $$| $$  | $$| $$| $$  | $$| $$  | $$            
        | $$$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$| $$  | $$|  $$$$$$$ /$$ /$$ 
        |________/ \______/  \_______/ \_______/|__/|__/  |__/ \____  $$|__/|__/
                                                               /$$  \ $$            
                                                              |  $$$$$$/            
                                                               \______/ ''')
        time.sleep(0.3)
        clear()
        print('''
         /$$                                 /$$ /$$                                
        | $$                                | $$|__/                                
        | $$        /$$$$$$   /$$$$$$   /$$$$$$$ /$$ /$$$$$$$   /$$$$$$             
        | $$       /$$__  $$ |____  $$ /$$__  $$| $$| $$__  $$ /$$__  $$            
        | $$      | $$  \ $$  /$$$$$$$| $$  | $$| $$| $$  \ $$| $$  \ $$            
        | $$      | $$  | $$ /$$__  $$| $$  | $$| $$| $$  | $$| $$  | $$            
        | $$$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$| $$  | $$|  $$$$$$$ /$$ /$$ /$$
        |________/ \______/  \_______/ \_______/|__/|__/  |__/ \____  $$|__/|__/|__/
                                                               /$$  \ $$            
                                                              |  $$$$$$/            
                                                               \______/ ''')
        time.sleep(0.3)

def swoosh_loader():
    while True:
        clear()
        print("O------")
        time.sleep(0.1)
        clear()
        print("-O-----")
        time.sleep(0.1)
        clear()
        print("--O----")
        time.sleep(0.1)
        clear()
        print("---O---")
        time.sleep(0.1)
        clear()
        print("----O--")
        time.sleep(0.1)
        clear()
        print("-----O-")
        time.sleep(0.1)
        clear()
        print("------O")
        time.sleep(0.1)
        clear()
        print("-----O-")
        time.sleep(0.1)
        clear()
        print("----O--")
        time.sleep(0.1)
        clear()
        print("---O---")
        time.sleep(0.1)
        clear()
        print("--O----")
        time.sleep(0.1)
        clear()
        print("-O-----")
        time.sleep(0.1)
        clear()
        print("O------")
        time.sleep(0.1)
    
def number_loader():
    a=0
    while True:
        clear()
        print(a)
        a += 1
        time.sleep(1.0)
    
def number_loader_fast():
    a = 0
    while True:
        clear()
        print(a)
        a += 1
        time.sleep(random.random()/10)

def random_number():
    clear()
    a=0
    while True:
        if a > 90:
            print(100)
            exit()
        print(random.randint(a, a+10))
        a+=10
        time.sleep(1)
        clear()
 
def choice():
    number_choosen = input("Choose the loader\n1 = simple\n2 = yeet 1\n3 = yeet 2\n4 = loading loader\n5 = swoosh\n6 = number\n7 = number random fast\n8 = random number. Range increasing by ten\n\n")
    clear()
    for char in letters:
        if char in number_choosen:
            input("This input doesn't match up with the options\nPress enter to continue\n")
            clear()
            return "error"
    return number_choosen
       
while True:
    state = choice() 
    if state == "error":
        continue   
    else:
        user_choice = state  
    
    user_choice = int(user_choice)
    if user_choice == 1:
        loader = simple_loader()
    elif user_choice == 2:
        loader = yeet_loader()
    elif user_choice == 3:
        loader = yeet_loader2()
    elif user_choice == 4:
        loader = loading_loader()
    elif user_choice == 5:
        loader = swoosh_loader()
    elif user_choice == 6:
        loader = number_loader()
    elif user_choice == 7:
        loader = number_loader_fast()
    elif user_choice == 8:
        loader = random_number()
    else:
        clear()
        input("This input doesn't match up with the options\nPress enter to continue\n")
        continue
        
    loader
