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

print(key_gen())