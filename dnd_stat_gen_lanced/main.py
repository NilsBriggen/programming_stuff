from random import randint
import names, races, time, os

strength = 0
dexterity = 0
constitution = 0
intelligence = 0
wisdom = 0
charisma = 0
title_list = []
value_list = []
race = ""
sex = ""
subrace = ""
name = ""
virtue = ""
types = ["male", "female", "child"]
stat_values = [15, 14, 12, 11, 10, 8]
race_index = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half_Elf", "Half_Orc", "Tiefling"]
stat_index = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
class_list = [strength, dexterity, constitution, intelligence, wisdom, charisma]
dice_temp = []


def reset():
    global strength, dexterity, constitution, intelligence, wisdom, charisma, title_list, value_list, race, sex, subrace, name, virtue, dice_temp
    strength = 0
    dexterity = 0
    constitution = 0
    intelligence = 0
    wisdom = 0
    charisma = 0
    title_list = []
    value_list = []
    race = ""
    sex = ""
    subrace = ""
    name = ""
    virtue = ""
    types = ["male", "female", "child"]
    stat_values = [15, 14, 12, 11, 10, 8]
    race_index = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half_Elf", "Half_Orc", "Tiefling"]
    stat_index = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    dice_temp = []



def cls():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def table_gen():
    global strength, dexterity, constitution, intelligence, wisdom, charisma, race, subrace, name, sex, Class
    if subrace != race:
        print(f"\nName: {name}\nSex: {sex}\nRace: {race}\nSubrace: {subrace}\nStrength: {strength}\nDexterity: {dexterity}\nConstitution: {constitution}\nIntelligence: {intelligence}\nWisdom: {wisdom}\nCharisma: {charisma}")
    else:
        print(f"\nName: {name}\nSex: {sex}\nRace: {race}\nStrength: {strength}\nDexterity: {dexterity}\nConstitution: {constitution}\nIntelligence: {intelligence}\nWisdom: {wisdom}\nCharisma: {charisma}")


def name_gen():
    global name, race, sex, virtue
    print("class_calc lets go")
    names1 = names.Name
    sex = types[randint(0, 2)]
    if race == "Half-Orc":
        if sex == "child":
            sex = types[randint(0, 1)]
        list_length1 = len(names1["Half-Orc"][sex])-1
        name = names1["Half_Orc"][sex][randint(0, list_length1)]
    elif race == "Dwarf":
        if sex == "child":
            sex = types[randint(0, 1)]
        list_length1 = len(names1["Dwarf"][sex])-1
        list_length2 = len(names1["Dwarf"]["clan"])-1
        name = names1["Dwarf"][sex][randint(0, list_length1)] + " " + names1["Dwarf"]["clan"][randint(0, list_length2)]
    elif race == "Elf":
        list_length1 = len(names1["Halfling"][sex])-1
        list_length2 = len(names1["Halfling"]["family"])-1
        name = names1["Elf"][sex][randint(0, list_length1)] + " " + names1["Elf"]["family"][randint(0, list_length2)]
    elif race == "Halfling":
        if sex == "child":
            sex = types[randint(0, 1)]
        list_length1 = len(names1["Halfling"][sex])-1
        list_length2 = len(names1["Halfling"]["family"])-1
        name = names1["Halfling"][sex][randint(0, list_length1)] + " " + names1["Halfling"]["family"][randint(0, list_length2)]
    elif race == "Human":
        if sex == "child":
            sex = types[randint(0, 1)]
        list_length1 = len(names1["Human"][sex])-1
        list_length2 = len(names1["Human"]["family"])-1
        name = names1["Human"][sex][randint(0, list_length1)] + " " + names1["Human"]["family"][randint(0, list_length2)]
    elif race == "Dragonborn":
        list_length1 = len(names1["Dragonborn"][sex])-1
        list_length2 = len(names1["Dragonborn"]["clan"])-1
        name = names1["Dragonborn"][sex][randint(0, list_length1)] + " " + names1["Dragonborn"]["clan"][randint(0, list_length2)]
    elif race == "Gnome":
        if sex == "child":
            sex = types[randint(0, 1)]
        list_length1 = len(names1["Gnome"][sex])-1
        list_length2 = len(names1["Gnome"]["family"])-1
        list_length3 = len(names1["Gnome"]["nick"])-1
        name = names1["Gnome"][sex][randint(0, list_length1)] + ' "' + names1["Gnome"]["nick"][randint(0, list_length3)] + '" ' + names1["Gnome"]["family"][randint(0, list_length2)]
    elif race == "Half-Elf":
        if sex == "child":
            sex = types[randint(0, 1)]
        list_length1 = len(names1["Half-Elf"][sex])-1
        list_length2 = len(names1["Half-Elf"]["family"])-1
        name = names1["Half-Elf"][sex][randint(0, list_length1)] + " " + names1["Half-Elf"]["family"][randint(0, list_length2)]
    elif race == "Tiefling":
        while virtue == "":
            virtue = input(f"Choose a virtue for your character.\nAvailable Virtues: {str(names1['Tiefling']['virtue'])}\n")
            if virtue not in names1["Tiefling"]["virtue"]:
                print("You've made a typo. Please try again")
                virtue = ""
        if sex == "child":
            sex = types[randint(0, 1)]
        list_length1 = len(names1["Tiefling"][sex])-1
        name = names1["Tiefling"][sex][randint(0, list_length1)] + " " + virtue


def item_checker(item):
    global strength, dexterity, constitution, intelligence, wisdom, charisma, race, subrace
    if "str_boost" in item:
        exec("strength += races."+race+"[subrace]['str_boost']")
        exec('''print(f"Added a {races.'''+race+'''[subrace]['str_boost']} point advantage to strength")''')
    if "dex_boost" in item:
        exec("dexterity += races."+race+"[subrace]['dex_boost']")
        exec('''print(f"Added a {races.'''+race+'''[subrace]['dex_boost']} point advantage to dexterity")''')
    if "con_boost" in item:
        exec("constitution += races."+race+"[subrace]['con_boost']")
        exec('''print(f"Added a {races.'''+race+'''[subrace]['con_boost']} point advantage to constitution")''')
    if "int_boost" in item:
        exec("intelligence += races."+race+"[subrace]['int_boost']")
        exec('''print(f"Added a {races.'''+race+'''[subrace]['int_boost']} point advantage to intelligence")''')
    if "wis_boost" in item:
        exec("wisdom += races."+race+"[subrace]['wis_boost']")
        exec('''print(f"Added a {races.'''+race+'''[subrace]['wis_boost']} point advantage to wisdom")''')
    if "cha_boost" in item:
        exec("charisma += races."+race+"[subrace]['cha_boost']")
        exec('''print(f"Added a {races.'''+race+'''[subrace]['cha_boost']} point advantage to charisma")''')
    if "random_boost" in item:
        temp_rand = randint(0, 5)
        exec(stat_index[temp_rand]+"+=1")
        print(f"Added 1 random point advantage to {stat_index[temp_rand]}")
        temp_rand = randint(0, 5)
        exec(stat_index[temp_rand]+"+=1")
        print(f"Added 1 random point advantage to {stat_index[temp_rand]}")


def loader():
    global race, subrace
    if race == "Dwarf":
        for title, value in races.Dwarf.items():
            title_list.append(title)
            value_list.append(value)
        chooser = randint(0, 1)
        subrace = title_list[chooser]
        item_checker(value_list[chooser])
    elif race == "Half_Elf":
        for title, value in races.Half_Elf.items():
            title_list.append(title)
            value_list.append(value)
        subrace = title_list[0]
        item_checker(value_list[0])
    elif race == "Half_Orc":
        for title, value in races.Half_Orc.items():
            title_list.append(title)
            value_list.append(value)
        subrace = title_list[0]
        item_checker(value_list[0])
    elif race == "Tiefling":
        for title, value in races.Tiefling.items():
            title_list.append(title)
            value_list.append(value)
        subrace = title_list[0]
        item_checker(value_list[0])
    elif race == "Human":
        for title, value in races.Human.items():
            title_list.append(title)
            value_list.append(value)
        subrace = title_list[0]
        item_checker(value_list[0])
    elif race == "Dragonborn":
        for title, value in races.Dragonborn.items():
            title_list.append(title)
            value_list.append(value)
        subrace = title_list[0]
        item_checker(value_list[0])
    elif race == "Halfling":
        for title, value in races.Halfling.items():
            title_list.append(title)
            value_list.append(value)
        chooser = randint(0, 1)
        subrace = title_list[chooser]
        item_checker(value_list[chooser])
    elif race == "Gnome":
        for title, value in races.Gnome.items():
            title_list.append(title)
            value_list.append(value)
        chooser = randint(0, 1)
        subrace = title_list[chooser]
        item_checker(value_list[chooser])
    elif race == "Elf":
        for title, value in races.Elf.items():
            title_list.append(title)
            value_list.append(value)
        chooser = randint(0, 2)
        subrace = title_list[chooser]
        item_checker(value_list[chooser])


def stat_gen_normal():
    global strength, dexterity, constitution, intelligence, wisdom, charisma, race, subrace
    strength = stat_values[randint(0, 5)]
    stat_values.remove(strength)
    dexterity = stat_values[randint(0, 4)]
    stat_values.remove(dexterity)
    constitution = stat_values[randint(0, 3)]
    stat_values.remove(constitution)
    intelligence = stat_values[randint(0, 2)]
    stat_values.remove(intelligence)
    wisdom = stat_values[randint(0, 1)]
    stat_values.remove(wisdom)
    charisma = stat_values[0]
    race = race_index[randint(0, 8)]
    loader()


def dice():
    result = 0
    temp = []
    for i in range(0, 4):
        temp.append(randint(1, 6))
    temp.remove(min(temp))
    for item in temp:
        result += item
    return result


def stat_gen_hardcore():
    global strength, dexterity, constitution, intelligence, wisdom, charisma, race, subrace
    strength = dice()
    dexterity = dice()
    constitution = dice()
    intelligence = dice()
    wisdom = dice()
    charisma = dice()
    race = race_index[randint(0, 8)]
    loader()


run = True

while run:
    cls()
    reset()
    mode = str(input("Choose your generator mode. Enter '1' for simple generation. Enter '2' for advanced generation.\n"))
    if mode == "1":
        stat_gen_normal()
        name_gen()
        table_gen()
    elif mode == "2":
        stat_gen_hardcore()
        name_gen()
        table_gen()
    else:
        print("Error: 666\nGo to hell")
    rerun = str(input("\nRerun the generator? Press enter for yes. Enter '1' for no.\n"))
    if rerun == "1":
        run = False
    elif rerun != "":
        print("Well...\nYou've made a typo...\nAnd you had to type one number or even nothing...\nWell the generator will now run again...")
        time.sleep(5)
