import armor
import classes
import difflib
import os
import races
import weapons

index = [armor.armor, weapons.weapons, races.races, classes.classes]
long_index = ["clear", "shield", "armor", "weapons", "races", "classes"]
index2 = {
    "armor": armor.armor,
    "weapons": weapons.weapons,
    "races": races.races,
    "classes": classes.classes
}
result_found = False

long_index.extend(armor.indexer())
long_index.extend(weapons.indexer())
long_index.extend(races.indexer())
long_index.extend(classes.indexer())


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def category_search(user_input):
    global result_found
    if user_input == "clear":
        cls()
    elif user_input == "shield":
        for obj, value in armor.shield.items():
            print(obj + ":", value)
        print("\n\n")
    elif user_input in index2:
        for obj, value in index2[user_input].items():
            print(obj)
        result_found = True
    else:
        for item in index:
            if user_input in item:
                for obj, value in item[user_input].items():
                    print(obj)
                result_found = True
        if not result_found:
            result_armor = armor.armor_subcategory_search(user_input)
            result_weapons = weapons.weapons_subcategory_search(user_input)
            if result_armor is False and result_weapons is False:
                similar = difflib.get_close_matches(user_input, long_index)
                if len(similar) != 0:
                    similar = ', '.join(similar)
                    print(f"No results were found! Did you intend to write this: {similar}\n\n")
                else:
                    print("no results were found!\n")
            else:
                print("\n")


while True:
    user = input("search for an item: ")
    category_search(user)
