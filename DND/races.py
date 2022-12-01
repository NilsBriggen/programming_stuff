dwarf = {}
elf = {}
halfling = {}
human = {}
dragonborn = {}
gnome = {}
half_elf = {}
half_orc = {}
tiefling = {}

races = {
    "dwarf": dwarf,
    "elf": elf,
    "halfling": halfling,
    "human": human,
    "dragonborn": dragonborn,
    "gnome": gnome,
    "half elf": half_elf,
    "half orc": half_orc,
    "tiefling": tiefling,
}

races_index = [dwarf, elf, halfling, human, dragonborn, gnome, half_elf, half_orc, tiefling]
indexed = []


def indexer():
    for obj, value in races.items():
        indexed.append(obj)
    return indexed
