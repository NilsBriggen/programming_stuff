import random, sys

LENGTH = 1048576
#sys.set_int_max_str_digits(maxdigits=LENGTH)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def key_gen():
    x = random.randint(10**(LENGTH-1), 10**LENGTH)
    while gcd(10**256, x) != 1:
        x = random.randint(10**(LENGTH-1), 10**LENGTH)

    return x

key_gen()