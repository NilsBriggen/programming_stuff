import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

from art import logo

repeat = True

bids = []

def gebot(name_indicated, bidden_money):
    new_bid = {}
    new_bid["name"] = name_indicated
    new_bid["bidden_money"] = bidden_money
    bids.append(new_bid)

while repeat == True:
    name = input("What's your name?\n")
    bid = float(input("What's your bid?\n"))
    bid = round(bid, 2)

    gebot(name, bid)

    repeat_ask = input("Are there more persons which want to bid? Y or n\n")
    if repeat_ask == "Y":
        repeat = True
        clear()
    else:
        repeat = False

print(bids)