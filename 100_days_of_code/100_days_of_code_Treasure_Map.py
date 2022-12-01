import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gestures = [scissors, paper, rock]
player = int(input("What do you choose? enter 0 for scissors, 1 for paper and 2 for rock."))
ai = random.randint(0, 2)

player = gestures[player]
ai = gestures[ai]

if player == scissors:
    print(f"You chose scissors")
    print(scissors)
elif player == paper:
    print("You chose paper")
    print(paper)
else:
    print("You chose rock")
    print(rock)

if ai == scissors:
    print(f"The computer chose scissors")
    print(scissors)
elif ai == paper:
    print("The computer chose paper")
    print(paper)
else:
    print("The computer chose rock")
    print(rock)

if player == scissors and ai == scissors:
    print("tie")
if player == rock and ai == rock:
    print("tie")
if player == paper and ai == paper:
    print("tie")

if player == scissors and ai == rock:
    print("You lose")
if player == scissors and ai == paper:
    print("You win")

if player == paper and ai == scissors:
    print("You lose")
if player == paper and ai == rock:
    print("You win")

if player == rock and ai == scissors:
    print("You win")
if player == rock and ai == paper:
    print("You lose")