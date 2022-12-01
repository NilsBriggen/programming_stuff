#The Loader module
#Available loaders: simple loader, yeet loader, yeet loader2, loading loader, swoosh loader

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
        print(random.randint(a, a+10))
        a+=10
        time.sleep(1)
        clear()
 
def choice():
    number_choosen = input("Choose the loader\n1 = simple\n2 = loading loader \n3 = swoosh \n4 = number\n5 = number random fast\n6 = random number. Range increasing by ten\n\n")
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
        loader = loading_loader()
    elif user_choice == 3:
        loader = swoosh_loader()
    elif user_choice == 4:
        loader = number_loader()
    elif user_choice == 5:
        loader = number_loader_fast()
    elif user_choice == 6:
        loader = random_number()
    else:
        clear()
        input("This input doesn't match up with the options\nPress enter to continue\n")
        continue
        
    loader
