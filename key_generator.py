import random

LENGTH = 126976

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def key_gen():
    x = random.randint(10**(LENGTH-1), 10**LENGTH)
    while gcd(10**LENGTH, x) != 1:
        x = random.randint(10**(LENGTH-1), 10**LENGTH)

    return x

key_gen()