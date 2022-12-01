barbarian = {}
bard = {}
cleric = {}
druid = {}
fighter = {}
monk = {}
paladin = {}
ranger = {}
rogue = {}
sorcerer = {}
warlock = {}
wizard = {}

classes = {
    "barbarian": barbarian,
    "bard": bard,
    "cleric": cleric,
    "druid": druid,
    "fighter": fighter,
    "monk": monk,
    "paladin": paladin,
    "ranger": ranger,
    "rogue": rogue,
    "sorcerer": sorcerer,
    "warlock": warlock,
    "wizard": wizard,
}

classes_index = [barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, wizard]
indexed = []


def indexer():
    for obj, value in classes.items():
        indexed.append(obj)
    return indexed
