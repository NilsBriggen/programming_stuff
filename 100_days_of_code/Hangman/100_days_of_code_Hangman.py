#Step 4

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
import random
from word_list import word_list
from hangman_art import *

print(logo)

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    cls()
    if guess in display:
            print("This letter was used already")
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        lives -= 1
    if lives == 0:
            print("You lose!")
            end_of_game = True
            print(f"The word would've been: {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])


    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.