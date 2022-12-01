from random import randint
from tkinter import *
from userkey import *

text = '''Wee Woo Wee Woo'''

def key_gen():
    global KEY, DEPRECATED_KEY
    try:
        DEPRECATED_KEY = keys["KEY"]
    except NameError:
        pass
    KEY = int("".join([str(randint(0, 8)) for i in range(8)]))

if len(str(keys["KEY"])) == 8 and len(str(keys["DEPRECATED_KEY"])) == 8:
    KEY = keys["KEY"]
    DEPRECATED_KEY = keys["DEPRECATED_KEY"]
else:
    key_gen()
    keys["KEY"] = KEY
    keys["DEPRECATED_KEY"] = DEPRECATED_KEY

def encrypt(text):
    binary_list = []
    # convert ascii to binary
    for char in text:
        binary = bin(ord(char))[2:]
        binary_list.append(binary)
    for i in range(len(binary_list)):
        binary_list[i] = str(int(binary_list[i]) + KEY)
    binary = ''.join(binary_list)
    return binary

def decrypt(binary):
    data_list = []
    binary_list = []
    for i in range(0, len(binary), 8):
        binary_list.append(binary[i:i+8])
    try:
        for i in range(len(binary_list)):
            binary_list[i] = str(int(binary_list[i]) - KEY)
            data_list.append(chr(int(binary_list[i], 2)))
        data = ''.join(data_list)
    except:
        data = backup_decrypt(binary)
        #convert binary to ascii
    return data

def backup_decrypt(binary):
    data_list = []
    binary_list = []
    for i in range(0, len(binary), 8):
        binary_list.append(binary[i:i+8])
    for i in range(len(binary_list)):
        binary_list[i] = str(int(binary_list[i]) - DEPRECATED_KEY)
        data_list.append(chr(int(binary_list[i], 2)))
        #convert binary to ascii
    data = ''.join(data_list)
    data = data + " (Encryption key changed)"
    return data

def read_file():
    with open('Save.nic', 'r') as f:
        binary = f.read()
        if binary == "":
            return ""
        data = decrypt(binary)
        print("Read data (decrypted): " + data)
        return data

def save_file():
    data = text
    print("Save data (decrypted): " + data)
    binary = encrypt(data)
    with open('Save.nic', 'w') as f:
        f.write(binary)

#setup Screen
root = Tk()
root.title("Encryption")
root.geometry("300x300")

#setup encryption button
button1 = Button(root, text="Read", command=read_file)
button1.pack()
#setup decryption button
button2 = Button(root, text="Write", command=save_file)
button2.pack()
#setup new key button
button3 = Button(root, text="New Key", command=key_gen)
button3.pack()
mainloop()