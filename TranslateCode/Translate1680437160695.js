function gcd(a, b) {
    while (b) {
        a, b = b, a % b
    }
    return a
}

function key_gen() {
    x = Math.floor(Math.random() * (10**LENGTH - 10**(LENGTH-1) + 1)) + 10**(LENGTH-1);
    while (gcd(10**256, x) != 1) {
        x = Math.floor(Math.random() * (10**LENGTH - 10**(LENGTH-1) + 1)) + 10**(LENGTH-1);
    }

    return x
}

LENGTH = 1048576
key_gen()
