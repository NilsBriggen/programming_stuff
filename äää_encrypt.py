decode = {
    "äää": "a",
    "ääö": "b",
    "ääü": "c",
    "äöä": "d",
    "äöö": "e",
    "äöü": "f",
    "äüä": "g",
    "äüä": "h",
    "äüö": "i",
    "äüü": "j",
    "öää": "k",
    "öäö": "l",
    "öäü": "m",
    "ööä": "n",
    "ööö": "o",
    "öüä": "p",
    "öüö": "q",
    "öüü": "r",
    "üää": "s",
    "üäö": "t",
    "üäü": "u",
    "üöä": "v",
    "üöö": "w",
    "üöü": "x",
    "üüä": "y",
    "üüö": "z",
    "üüü": ".",
}

encode = {
    "a": "äää",
    "b": "aaö",
    "c": "ääü",
    "d": "äöä",
    "e": "äöö",
    "f": "äöü",
    "g": "äüä",
    "h": "äüä",
    "i": "äüö",
    "j": "äüü",
    "k": "öää",
    "l": "öäö",
    "m": "öäü",
    "n": "ööä",
    "o": "ööö",
    "p": "öüä",
    "q": "öüö",
    "r": "öüü",
    "s": "üää",
    "t": "üäö",
    "u": "üäü",
    "v": "üöä",
    "w": "üöö",
    "x": "üöü",
    "y": "üüä",
    "z": "üüö",
    ".": "üüü",
}

text_list = []
output = []

while True:
    mode = input("Choose your mode. type e or d (encode/decode): ")
    if mode == "e":
        text = ""
        text_list = []
        output = []
        text = input("Enter your text to encrypt it: ")
        text = text.lower()
        text = text.replace(" ", "")
        text_list = list(text)
        for item in text_list:
            output.append(encode[item])
        print(" ".join(output))

    if mode == "d":
        text = ""
        text_list = []
        output = []
        text = input("Enter your text to decrypt it: ")
        text = text.lower()
        text_list = text.split(" ")
        for item in text_list:
            output.append(decode[item])
        print(" ".join(output))