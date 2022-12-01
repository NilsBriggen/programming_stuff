import random
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def game():
    tester = False
    repeat = True
    cards_player = []
    cards_player.append(cards[random.randint(12, 12)])
    cards_player.append(cards[random.randint(12, 12)])
    cards_pc = []
    cards_pc.append(cards[random.randint(0, 12)])

    print(f"Your cards:", cards_player, "\nYour current score:", sum(cards_player))
    print(f"Computer's first card:", cards_pc)
    if sum(cards_player) == 21:
        cards_pc.append(cards[random.randint(0, 12)])
        while sum(cards_pc) <= 16:
            cards_pc.append(cards[random.randint(0, 12)])
        print(f"The computer's cards are:", cards_pc, "\nThe computer's final score:", sum(cards_pc))
        if sum(cards_pc) == 21:
            print("Draw!")
        else:
            print("Congratulations! You win!") 
        repeat = False
        tester = True
        
    if sum(cards_player) > 21 and 11 in cards_player:
        for n, i in enumerate(cards_player):
            if i == 11:
                cards_player[n] = 1
                print("As your score was higher than 21 and you had the number eleven the programm replaced it with a one")
                return
        print(f"Your cards:", cards_player, "\nYour current score:", sum(cards_player))

    while repeat == True:
        additional_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if "y" in additional_card:
            clear()
            cards_player.append(cards[random.randint(0, 12)])
            if sum(cards_player) > 21 and 11 in cards_player:
                for n, i in enumerate(cards_player):
                    if sum(cards_player) < 21:
                        continue
                    if i == 11:
                        cards_player[n] = 1
                        print("As your score was higher than 21 and you had the number eleven the programm replaced it with a one")
            print(f"Your cards:", cards_player, "\nYour current score:", sum(cards_player))
            if sum(cards_player) == 21:
                cards_pc.append(cards[random.randint(0, 12)])
                while sum(cards_pc) <= 16:
                    cards_pc.append(cards[random.randint(0, 12)])
                print(f"The computer's cards are:", cards_pc, "\nThe computer's final score:", sum(cards_pc))
                if sum(cards_pc) == 21:
                    print("Draw!")
                else:
                    print("Congratulations! You win!")
                tester = True    
            elif sum(cards_player) > 21:
                print("You went over. You lose")
                tester = True
            if tester == True:
                repeat = False
        else:
            repeat = False
    if tester == False:
        clear()
        print(f"Your final hand:", cards_player, "\nYour final score:", sum(cards_player))
        cards_pc.append(cards[random.randint(0, 12)])
        while sum(cards_pc) <= 16:
            cards_pc.append(cards[random.randint(0, 12)])
        print(f"The computer's cards are:", cards_pc, "\nThe computer's final score:", sum(cards_pc))
    if tester == True:
        return
    elif sum(cards_player) == 21:
        if sum(cards_pc) == 21:
            return
        else:
            print("Congratulations! You win!")    
    elif sum(cards_pc) > 21:
        print("Your opponent went over. You win")
    elif sum(cards_player) > 21:
        print("You went over. You lose")
    elif sum(cards_player) > sum(cards_pc):
        print("Congratulations! You win!")
    elif sum(cards_pc) > sum(cards_player):
        print("Your opponent wins")
    elif sum(cards_pc) == sum(cards_player):
        print("Draw!")
clear()
print(logo)
print("Welcome to Blackjack!\nNote: Jacks, Kings, Queens and Aces are shown by their value. That's why there can be quite a lot of 10's.\nBut anyways, have fun!")
repeat_game = True
while repeat_game == True:        
    game()
    user_repeat_game = input("Do you want to play another round? y or n\n")
    if user_repeat_game == "y" or user_repeat_game == "Y":
        repeat_game = True
        clear()
    else:
        repeat_game = False
        clear()
        print("Have a great day!")
       