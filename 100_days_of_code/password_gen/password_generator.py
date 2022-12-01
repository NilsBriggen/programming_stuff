import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '≈', '@', '"', '<', '>', '¦', '°', '§', '¬', '|', '¢', '^', '~', '[', ']', '¨', '£', '{', '}', '.']
letter_value = {
    ' ': 0,
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
}

lists = [letters, numbers, symbols]
for thing in lists:
    for a in range(1, 10**3):
        random.shuffle(thing)

print("Welcome to the Python Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
shuffle_word = input(f"Please enter a random word. This word will be used to randomize the password even further\nYou cannot use symbols and numbers\n")
shuffle_word.lower()
shuffle_word = list(shuffle_word)


def retry(letters):
    global shuffle_word
    for lt in letters:
        if lt in symbols or lt in numbers:
            shuffle_word = []
            print('You cannot use symbols and numbers in this word. Please retry!')
            shuffle_word = list(input(f"Please enter a random word.\nYou cannot use symbols and numbers\n"))
            retry(shuffle_word)


retry(shuffle_word)


password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

for a in range(0, random.randint(1, 100)):
    random.shuffle(password_list)

randomizer = 0

for lt in shuffle_word:
    randomizer += letter_value[lt]

for a in range(0, randomizer**3):
    random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
