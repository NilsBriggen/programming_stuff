light = {
    "padded": {
        "cost": "5 gp",
        "class": 11,
        "weight": 8,
        "limit_dex_modifier": "none",
        "strength": "none",
        "stealth": "disadvantage",
    },
    "leather": {
        "cost": "10 gp",
        "class": 11,
        "weight": 10,
        "limit_dex_modifier": "none",
        "strength": "none",
        "stealth": "none",
    },
    "studded leather": {
        "cost": "45 gp",
        "class": 12,
        "weight": 13,
        "limit_dex_modifier": "none",
        "strength": "none",
        "stealth": "none",
    },
}

medium = {
    "hide": {
        "cost": "10 gp",
        "class": 12,
        "weight": 12,
        "limit_dex_modifier": "max. 2",
        "strength": "none",
        "stealth": "none",
    },
    "chain shirt": {
        "cost": "50 gp",
        "class": 13,
        "weight": 20,
        "limit_dex_modifier": "max. 2",
        "strength": "none",
        "stealth": "none",
    },
    "scale mail": {
        "cost": "50 gp",
        "class": 14,
        "weight": 45,
        "limit_dex_modifier": "max. 2",
        "strength": "none",
        "stealth": "disadvantage",
    },
    "breastplate": {
        "cost": "400 gp",
        "class": 14,
        "weight": 20,
        "limit_dex_modifier": "max. 2",
        "strength": "none",
        "stealth": "none",
    },
    "half plate": {
        "cost": "750 gp",
        "class": 15,
        "weight": 40,
        "limit_dex_modifier": "max. 2",
        "strength": "none",
        "stealth": "disadvantage",
    }
}

heavy = {
    "ring mail": {
        "cost": "30 gp",
        "class": 14,
        "weight": 40,
        "limit_dex_modifier": "none",
        "strength": "none",
        "stealth": "none",
    },
    "chain mail": {
        "cost": "75 gp",
        "class": 16,
        "weight": 55,
        "limit_dex_modifier": "none",
        "strength": "Str 13",
        "stealth": "disadvantage",
    },
    "splint": {
        "cost": "200 gp",
        "class": 17,
        "weight": 60,
        "limit_dex_modifier": "none",
        "strength": "Str 15",
        "stealth": "disadvantage",
    },
    "plate": {
        "cost": "1'500 gp",
        "class": 18,
        "weight": 65,
        "limit_dex_modifier": "none",
        "strength": "Str 15",
        "stealth": "disadvantage",
    }
}

shield = {
    "cost": "10 gp",
    "class": 2,
    "weight": 6,
    "limit_dex_modifier": "Is dex modifier",
    "strength": "none",
    "stealth": "none",
}

armor = {
    "light": light,
    "medium": medium,
    "heavy": heavy,
    "shield": shield,
}

armor_index = [light, medium, heavy]
indexed = []


def indexer():
    for item in armor_index:
        for obj, value in item.items():
            indexed.append(obj)
    return indexed


def armor_subcategory_search(user):
    result = False
    for item in armor_index:
        if user in item:
            for obj, value in item[user].items():
                print(obj + ":", value)
            result = True
    if result:
        return True
    else:
        return False
