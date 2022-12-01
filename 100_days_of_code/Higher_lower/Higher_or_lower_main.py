from art import *
from game_data import *
from random import *
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

score = 0

def points():
    global score
    score += 1

def game():
    clear()
    print(logo)    
    if score > 0:
        print("Your score is:", score)
    safe_p1 = randint(0, 48)
    safe_p2 = randint(0, 48)
    while safe_p2 == safe_p1:
        safe_p1 = randint(0, 48)
        return safe_p1
    person1 = data[safe_p1]
    person2 = data[safe_p2]
    print("Compare A:", person1['name'],"\nA", person1['description'],"from", person1['country'])
    print(vs)
    print("Against B:", person2['name'],"\nA", person2['description'],"from", person2['country'])
    user_input = input("Who has more followers? Type 'A' or 'B': ")
    if user_input == "a" or user_input == "A":
        if person1['follower_count'] > person2['follower_count']:
            points()
            game()
        else:
            print("This is wrong!")
            exit()
    elif user_input == "b" or user_input == "B":
        if person1['follower_count'] < person2['follower_count']:
            points()
            game()
        else:
            print("This is wrong!\nYour final score is", score)
            exit()    

game()