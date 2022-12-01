import random


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def key_gen():
    x = random.randint(10**256, 10**257)
    while gcd(10**256, x) != 1:
        x = random.randint(10**256, 10**257)
    return x


def text_to_binary(text):
    text = str(text)
    binary = ''.join('{0:08b}'.format(ord(x), 'b') for x in text)
    return binary


def to256(x):
    binary_a = text_to_binary(x)
    nuot = 0
    while len(binary_a) < 256:
        binary_a = text_to_binary(binary_a)
        nuot += 1
    print("jfztdtkudtdtddkudrzjdtu"+binary_a +"sakdfhsadfhoiadhfoiahiuda"+str(len(binary_a)))
    binary_a = str(nuot)+str(binary_a)
    return binary_a


def from256(a, b):
    che = 0
    while che < int(b):
        a = btt(a)
    return a


def split(word):
    return [char for char in word]


def dtb(n):
    b = bin(int(n)).replace("0b", "")
    return int(b)


def numtotext(n):
    n = str(n)
    s = [n[i:i + 2] for i in range(0, len(n), 2)]
    t = []
    for l in s:
        if split(l)[0] == "0":
            bt = split(l)
            bt.pop(0)
            bt.insert(0, "'")
            l = "".join(bt)
        try:
            if int(l) > 25:
                p = split(l)
                for i in p:
                    t.append(int(i)+97)
            else:
                t.append(int(l)+97)
        except:
            t.append(l)
    sm = []
    for b in t:
        try:
            lt = chr(b)
            sm.append(lt)
        except:
            sm.append(b)
    wd = "".join(sm)
    return wd


def texttonum(n):
    n = str(n)
    nb = []
    for letter in n:
        if letter == "'":
            letter = 0
        try:
            letter = int(letter)
        except:
            pass
        try:
            tbp = ord(letter)-97
            nb.append(tbp)
        except:
            nb.append(letter)
    nn = []
    for i in nb:
        o = str(i)
        nn.append(o)
    nn = "".join(nn)
    return nn


def btd(n):
    a = int(str(n), 2)
    return(a)


def mix(a, b):
    a = split(a)
    lett = a[0]
    a.pop(0)
    a = "".join(a)
    a = int(a)
    b = int(b)
    c = int(a)*int(b)
    d = dtb(c)
    e = d*b
    g = numtotext(str(e))
    return str(lett)+str(g)


def unmix(a, b):
    a = split(a)
    print(len(a))
    lett = a[1]
    a.pop(0)
    a = "".join(a)
    c = texttonum(a)
    a = int(a)
    b = int(b)
    d = c/b
    e = btd(d)
    f = e/b
    return f, lett


def unmix2(a, b):
    a = split(a)
    print(len(a))
    lett = a[0]
    a.pop(0)
    a = "".join(a)
    c = texttonum(a)
    print(c)
    c = int(c)
    b = int(b)
    d = c//b
    print(d)
    e = btd(d)
    f = e//b
    return f, lett


def splitx(n, b):
    a = [n[i:i + b] for i in range(0, len(n), b)]
    return(a)


def btt(a_binary_string):
    binary_values = splitx(a_binary_string, 8)
    ascii_string = ""
    for binary_value in binary_values:
        print(binary_value)
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    print(len(ascii_string))
    return ascii_string


def bttspec(a_binary_string):
    lenx = len(a_binary_string)
    print(lenx)
    u = lenx % 8
    print(u)
    zs = ""
    u = 8-u
    print(u)
    while u > 0:
        zs += "0"
        u -= 1
    print(u)
    b_binary_string = zs+a_binary_string
    binary_values = splitx(b_binary_string, 8)
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    return ascii_string


action = input("Do you want to encode or decode or generate a key(1/2/3)?\n")
if action == "1":
    text = input("Text to encrypt:\n")
    bin1 = to256(text)
    key = input("Key:\n")
    crypted = mix(bin1, key)
    print(crypted)
if action == "2":
    text = input("Text to decrypt:\n")
    key = input("Key:\n")
    print(text)
    text2 = split(text)
    text = []
    for i in text2:
        if i == "'":
            text.append("0")
        else:
            text.append(i)
    text = "".join(text)
    print(text)
    crypted = unmix2(text, key)
    u = 1
    output = str(crypted[0])
    print(output)
    while int(u) < int(crypted[1]):
        output = bttspec(output)
        u += 1
    print("\nthis is the output: "+output)
    finaloutput1 = btt(output)
    finaloutput = btt(finaloutput1)
    print(finaloutput)
    print("End")
if action == "3":
    new_key = key_gen()
    print(new_key)
