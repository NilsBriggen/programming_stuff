from random import randint, choice
import names, races, time, os
from proficiencyb import Proficiency
from languages import Languages

RED = '\u001b[31m'
ORANGE = '\u001b[91m'
YELLOW = '\u001b[93m'
GREEN = '\u001b[32m'
BLUE = '\u001b[34m'
INDIGO = '\u001b[35m'
VIOLET = '\u001b[95m'
RESET = '\u001b[0m'
strength = 0
dexterity = 0
constitution = 0
intelligence = 0
wisdom = 0
charisma = 0
str_mod = 0
dex_mod = 0
con_mod = 0
int_mod = 0
wis_mod = 0
cha_mod = 0
title_list = []
value_list = []
language_prof = ["Acolyte", "Guild Artisan", "Hermit", "Noble", "Outlander", "Sage"]
class_list = {}
race = ""
geschlecht = ""
subrace = ""
name = ""
virtue = ""
stat_class = ""
language = []
types = ["male", "female", "child"]
stat_values = [15, 14, 12, 11, 10, 8]
race_index = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half_Elf", "Half_Orc", "Tiefling"]
stat_index = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
stat_index2 = [strength, dexterity, constitution, intelligence, wisdom, charisma]
dice_temp = []


virtue_index = ", ".join(names.Name["Tiefling"]["virtue"])

def reset():
    global strength, dexterity, constitution, intelligence, wisdom, charisma, title_list, value_list, race, geschlecht, subrace, name, virtue, dice_temp, class_list, stat_class, language, types, stat_values, race_index, stat_index, str_mod, dex_mod, con_mod, int_mod, wis_mod, cha_mod
    strength = 0
    dexterity = 0
    constitution = 0
    intelligence = 0
    wisdom = 0
    charisma = 0
    str_mod = 0
    dex_mod = 0
    con_mod = 0
    int_mod = 0
    wis_mod = 0
    cha_mod = 0
    title_list = []
    value_list = []
    class_list = {}
    race = ""
    geschlecht = ""
    subrace = ""
    name = ""
    virtue = ""
    stat_class = ""
    language = []
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


def class_calc_simple():
    global strength, dexterity, constitution, intelligence, wisdom, charisma, class_list, stat_class, race
    temp1 = []
    temp2 = []
    if race == "Rainbow Dragonborn":
        stat_class = choice(["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"])
    else:
        class_list = {"strength": strength, "dexterity": dexterity, "constitution": constitution, "intelligence": intelligence, "wisdom": wisdom, "charisma": charisma}
        for title, value in class_list.items():
            temp1.append(title)
            temp2.append(value)
        biggest = max(temp2)
        main_stat = temp1[temp2.index(biggest)]
        if main_stat == "strength":
            chooser = randint(0, 2)
            if chooser == 0:
                stat_class = "Barbarian"
            elif chooser == 1:
                stat_class = "Fighter"
            else:
                stat_class = "Paladin"
        elif main_stat == "charisma":
            chooser = randint(0, 3)
            if chooser == 0:
                stat_class = "Bard"
            elif chooser == 1:
                stat_class = "Paladin"
            elif chooser == 2:
                stat_class = "Sorcerer"
            else:
                stat_class = "Warlock"
        elif main_stat == "wisdom":
            chooser = randint(0, 3)
            if chooser == 0:
                stat_class = "Cleric"
            elif chooser == 1:
                stat_class = "Druid"
            elif chooser == 2:
                stat_class = "Monk"
            else:
                stat_class = "Ranger"
        elif main_stat == "dexterity":
            chooser = randint(0, 3)
            if chooser == 0:
                stat_class = "Fighter"
            elif chooser == 1:
                stat_class = "Monk"
            elif chooser == 2:
                stat_class = "Ranger"
            else:
                stat_class = "Rogue"
        elif main_stat == "intelligence":
            stat_class = "Wizard"
        else:
            stat_class = choice(["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"])



def table_gen():
    global strength, dexterity, constitution, intelligence, wisdom, charisma, race, subrace, name, geschlecht, stat_class, language, proficiency

    if proficiency != str(proficiency):
        proficiency = ", ".join(proficiency)
    if race == "Half_Elf":
        race = "Half-Elf"
    if race == "Half_Orc":
        race = "Half-Orc"
    language = ", ".join(language)
    if subrace == "Black Dragonborn":
        subrace = "\u001b[7m Black Dragonborn \u001b[0m"
    elif subrace == "Blue Dragonborn":
        subrace = "\u001b[36m Blue Dragonborn \u001b[0m"
    elif subrace == "Brass Dragonborn":
        subrace = "\u001b[93m Brass Dragonborn \u001b[0m"
    elif subrace == "Bronze Dragonborn":
        subrace = "\u001b[33m Bronze Dragonborn \u001b[0m"
    elif subrace == "Copper Dragonborn":
        subrace = "\u001b[33m Copper Dragonborn \u001b[0m"
    elif subrace == "Gold Dragonborn":
        subrace = "\u001b[93m Gold Dragonborn \u001b[0m"
    elif subrace == "Green Dragonborn":
        subrace = "\u001b[32m Green Dragonborn \u001b[0m"
    elif subrace == "Red Dragonborn":
        subrace = "\u001b[91m Red Dragonborn \u001b[0m"
    elif subrace == "Silver Dragonborn":
        subrace = "\u001b[90m Silver Dragonborn \u001b[0m"
    elif subrace == "White Dragonborn":
        subrace = "\u001b[97m White Dragonborn \u001b[0m"
    elif race == "Rainbow Dragonborn":
        subrace = f"{RED}R{RESET} {ORANGE}A{RESET} {YELLOW}I{RESET} {GREEN}N{RESET} {BLUE}B{RESET} {INDIGO}O{RESET} {VIOLET}W{RESET}   {RED}D{RESET} {ORANGE}R{RESET} {YELLOW}A{RESET} {GREEN}G{RESET} {BLUE}O{RESET} {INDIGO}N{RESET} {VIOLET}B{RESET} {RED}O{RESET} {ORANGE}R{RESET} {YELLOW}N{RESET}"
    if subrace != race:
        print(f"\nName: {name}\nGeschlecht: {geschlecht}\nClass: {stat_class}\nSubrace: {subrace}\nProficiency: {proficiency}\nLanguage: {language}\nStrength: {strength} | Strength modifier: {str_mod}\nDexterity: {dexterity} | Dexterity modifier: {dex_mod}\nConstitution: {constitution} | Constitution modifier: {con_mod}\nIntelligence: {intelligence} | Intelligence modifier: {int_mod}\nWisdom: {wisdom} | Wisdom modifier: {wis_mod}\nCharisma: {charisma} | Charisma modifier: {cha_mod}")
    else:
        print(f"\nName: {name}\nGeschlecht: {geschlecht}\nClass: {stat_class}\nSubrace: {race}\nProficiency: {proficiency}\nLanguage: {language}\nStrength: {strength} | Strength modifier: {str_mod}\nDexterity: {dexterity} | Dexterity modifier: {dex_mod}\nConstitution: {constitution} | Constitution modifier: {con_mod}\nIntelligence: {intelligence} | Intelligence modifier: {int_mod}\nWisdom: {wisdom} | Wisdom modifier: {wis_mod}\nCharisma: {charisma} | Charisma modifier: {cha_mod}")


def language_calc_gen():
    global language
    chooser = randint(0, 99)
    if chooser == 0:
        language.append("Sämbädäm")
    elif chooser <= 9:
        chooser = randint(0, 3)
        language.append(Languages["language_index"]["Primordial"][chooser])
    elif chooser <= 39:
        chooser = randint(0, 6)
        language.append(Languages["language_index"]["Exotic"][chooser])
    elif chooser <= 99:
        chooser = randint(0, 7)
        language.append(Languages["language_index"]["Standard"][chooser])



def language_calc():
    global language, language_prof, proficiency
    if race == "Rainbow Dragonborn":
        language = Languages["all"]
        return
    item = Languages["Race"][race]
    if item == "Random":
        language_calc_gen()
    else:
        language.append(item)
    if proficiency in language_prof:
        for x in range(0, Languages["Background"][proficiency]):
            language_calc_gen()



def skill_calc():
    global str_mod, dex_mod, con_mod, int_mod, wis_mod, cha_mod, stat_index, proficiency
    temp = []
    if race == "Rainbow Dragonborn":
        proficiency = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
        return
    else:
        for prof_list, values in Proficiency["Background"].items():
            temp.append(prof_list)
        proficiency = choice(temp)

        for item in Proficiency["Background"][proficiency]:
            if item == "Athletics":
                str_mod += 2
            elif item == "Acrobatics" or item == "Sleight of Hand" or item == "Stealth":
                dex_mod += 2
            elif item == "Arcana" or item == "History" or item == "Religion":
                int_mod += 2
            elif item == "Animal Handling" or item == "Insight" or item == "Medicine" or item == "Perception" or item == "Survival":
                wis_mod += 2
            elif item == "Deception" or item == "Intimidation" or item == "Performance" or item == "Persuasion":
                cha_mod += 2


def modifier_gen_assist(item):
    global strength, dexterity, constitution, intelligence, wisdom, charisma, str_mod, dex_mod, con_mod, int_mod, wis_mod, cha_mod, stat_index, stat_index2
    stat_index2 = [strength, dexterity, constitution, intelligence, wisdom, charisma]
    if stat_index2[stat_index.index(item)] == "All of it":
        mod = "∞"
    elif stat_index2[stat_index.index(item)] == 30:
        mod = 10
    elif stat_index2[stat_index.index(item)] >= 28:
        mod = 9
    elif stat_index2[stat_index.index(item)] >= 26:
        mod = 8
    elif stat_index2[stat_index.index(item)] >= 24:
        mod = 7
    elif stat_index2[stat_index.index(item)] >= 22:
        mod = 6
    elif stat_index2[stat_index.index(item)] >= 20:
        mod = 5
    elif stat_index2[stat_index.index(item)] >= 18:
        mod = 4
    elif stat_index2[stat_index.index(item)] >= 16:
        mod = 3
    elif stat_index2[stat_index.index(item)] >= 14:
        mod = 2
    elif stat_index2[stat_index.index(item)] >= 12:
        mod = 1
    elif stat_index2[stat_index.index(item)] >= 10:
        mod = 0
    elif stat_index2[stat_index.index(item)] >= 8:
        mod = -1
    elif stat_index2[stat_index.index(item)] >= 6:
        mod = -2
    elif stat_index2[stat_index.index(item)] >= 4:
        mod = -3
    elif stat_index2[stat_index.index(item)] >= 2:
        mod = -4
    elif stat_index2[stat_index.index(item)] == 1:
        mod = -5
    return mod


def modifier_gen():
    global strength, dexterity, constitution, intelligence, wisdom, charisma, str_mod, dex_mod, con_mod, int_mod, wis_mod, cha_mod
    for item in stat_index:
        if item == "strength":
            str_mod = modifier_gen_assist(item)
        elif item == "dexterity":
            dex_mod = modifier_gen_assist(item)
        elif item == "constitution":
            con_mod = modifier_gen_assist(item)
        elif item == "intelligence":
            int_mod = modifier_gen_assist(item)
        elif item == "wisdom":
            wis_mod = modifier_gen_assist(item)
        elif item == "charisma":
            cha_mod = modifier_gen_assist(item)

def name_gen():
    global name, race, geschlecht, virtue, types
    names1 = names.Name
    geschlecht = types[randint(0, 2)]
    if race == "Half_Orc":
        if geschlecht == "child":
            geschlecht = types[randint(0, 1)]
        list_length1 = len(names1["Half_Orc"][geschlecht])-1
        name = names1["Half_Orc"][geschlecht][randint(0, list_length1)]
    elif race == "Dwarf":
        if geschlecht == "child":
            geschlecht = types[randint(0, 1)]
        list_length1 = len(names1["Dwarf"][geschlecht])-1
        list_length2 = len(names1["Dwarf"]["clan"])-1
        name = names1["Dwarf"][geschlecht][randint(0, list_length1)] + " " + names1["Dwarf"]["clan"][randint(0, list_length2)]
    elif race == "Elf":
        list_length1 = len(names1["Elf"][geschlecht])-1
        list_length2 = len(names1["Elf"]["family"])-1
        name = names1["Elf"][geschlecht][randint(0, list_length1)] + " " + names1["Elf"]["family"][randint(0, list_length2)]
    elif race == "Halfling":
        if geschlecht == "child":
            geschlecht = types[randint(0, 1)]
        list_length1 = len(names1["Halfling"][geschlecht])-1
        list_length2 = len(names1["Halfling"]["family"])-1
        name = names1["Halfling"][geschlecht][randint(0, list_length1)] + " " + names1["Halfling"]["family"][randint(0, list_length2)]
    elif race == "Human":
        if geschlecht == "child":
            geschlecht = types[randint(0, 1)]
        list_length1 = len(names1["Human"][geschlecht])-1
        list_length2 = len(names1["Human"]["family"])-1
        name = names1["Human"][geschlecht][randint(0, list_length1)] + " " + names1["Human"]["family"][randint(0, list_length2)]
    elif race == "Dragonborn":
        list_length1 = len(names1["Dragonborn"][geschlecht])-1
        list_length2 = len(names1["Dragonborn"]["clan"])-1
        name = names1["Dragonborn"][geschlecht][randint(0, list_length1)] + " " + names1["Dragonborn"]["clan"][randint(0, list_length2)]
    elif race == "Gnome":
        if geschlecht == "child":
            geschlecht = types[randint(0, 1)]
        list_length1 = len(names1["Gnome"][geschlecht])-1
        list_length2 = len(names1["Gnome"]["family"])-1
        list_length3 = len(names1["Gnome"]["nick"])-1
        name = names1["Gnome"][geschlecht][randint(0, list_length1)] + ' "' + names1["Gnome"]["nick"][randint(0, list_length3)] + '" ' + names1["Gnome"]["family"][randint(0, list_length2)]
    elif race == "Half_Elf":
        if geschlecht == "child":
            geschlecht = types[randint(0, 1)]
        list_length1 = len(names1["Half_Elf"][geschlecht])-1
        list_length2 = len(names1["Half_Elf"]["family"])-1
        name = names1["Half_Elf"][geschlecht][randint(0, list_length1)] + " " + names1["Half_Elf"]["family"][randint(0, list_length2)]
    elif race == "Tiefling":
        while virtue == "":
            virtue = (input(f"Choose a virtue for your character.\nAvailable Virtues: {virtue_index}\n")).capitalize()
            if virtue not in names.Name["Tiefling"]["virtue"]:
                print("You've made a typo. Please try again")
                virtue = ""
            else:
                virtue = (str(virtue)).capitalize()
        if geschlecht == "child":
            geschlecht = types[randint(0, 1)]
        list_length1 = len(names1["Tiefling"][geschlecht])-1
        name = names1["Tiefling"][geschlecht][randint(0, list_length1)] + ' "' + virtue + '" '
    elif race == "Rainbow Dragonborn":
        name = 'Hans "slightly too close"'
        geschlecht = f"{RED}R{RESET} {ORANGE}A{RESET} {YELLOW}I{RESET} {GREEN}N{RESET} {BLUE}B{RESET} {INDIGO}O{RESET} {VIOLET}W{RESET}   {RED}D{RESET} {ORANGE}R{RESET} {YELLOW}A{RESET} {GREEN}G{RESET} {BLUE}O{RESET} {INDIGO}N{RESET} {VIOLET}B{RESET} {RED}O{RESET} {ORANGE}R{RESET} {YELLOW}N{RESET}"


def item_checker(item):
    global strength, dexterity, constitution, intelligence, wisdom, charisma, race, subrace
    if race == "Rainbow Dragonborn":
        strength = races.Easteregg["Rainbow Dragonborn"]['str_boost']
        dexterity = races.Easteregg["Rainbow Dragonborn"]['dex_boost']
        constitution = races.Easteregg["Rainbow Dragonborn"]['con_boost']
        intelligence = races.Easteregg["Rainbow Dragonborn"]['int_boost']
        wisdom = races.Easteregg["Rainbow Dragonborn"]['wis_boost']
        charisma = races.Easteregg["Rainbow Dragonborn"]['cha_boost']
    else:
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
            exec(stat_index[temp_rand]+" += 1")
            print(f"Added 1 random point advantage to {stat_index[temp_rand]}")
            temp_rand = randint(0, 5)
            exec(stat_index[temp_rand]+" += 1")
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
        chooser = randint(0, 9)
        subrace = title_list[chooser]
        item_checker(value_list[chooser])
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
    elif race == "Rainbow Dragonborn":
        for title, value in races.Easteregg.items():
            title_list.append(title)
            value_list.append(value)
        subrace = title_list[0]
        item_checker(value_list[0])


def stat_gen_normal():
    global strength, dexterity, constitution, intelligence, wisdom, charisma, race, subrace, stat_values
    stat_values = [15, 14, 12, 11, 10, 8]
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
    easteregg = randint(0, 99)
    if easteregg == 0:
        race = "Rainbow Dragonborn"
    else:
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
    easteregg = randint(0, 99)
    if easteregg == 0:
        race = "Rainbow Dragonborn"
    else:
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
        class_calc_simple()
        modifier_gen()
        skill_calc()
        language_calc()
        table_gen()
    elif mode == "2":
        stat_gen_hardcore()
        name_gen()
        class_calc_simple()
        modifier_gen()
        skill_calc()
        language_calc()
        table_gen()
    else:
        print("Error: 666\nGo to hell")
    rerun = str(input("\nRerun the generator? Press enter for yes. Enter '1' for no.\n"))
    if rerun == "1":
        run = False
    elif rerun != "":
        print("\nWell...\nYou've made a typo...\nAnd you had to type one number or even nothing...\nWell the generator will now run again...")
        time.sleep(6)
        cls()
