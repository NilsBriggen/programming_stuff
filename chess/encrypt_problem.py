def splitx(n,b):
    a=[n[i:i + b] for i in range(0, len(n), b)]
    return(a)

def bttspec(a_binary_string):
    lenx=len(a_binary_string)
    print(lenx)
    u=lenx%8
    print(u)
    zs=""
    u=8-u
    print(u)
    while u>0:
        zs+="0"
        u-=1

    print(u)
    b_binary_string=zs+a_binary_string
    binary_values = splitx(b_binary_string,8)
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    return ascii_string

print(bttspec(str(input("binary: "))))