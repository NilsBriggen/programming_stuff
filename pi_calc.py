pi = []

x = 3
b = 1

def equation():
    global b, x
    b -= 1/x
    x+=2
    b += 1/x

for a in range(0, 1000000000):
    equation()
    x+=2

print(b*4)