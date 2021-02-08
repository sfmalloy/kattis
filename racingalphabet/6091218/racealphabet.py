from string import ascii_uppercase
from math import pi

def mod(n, m):
    if n < 0:
        return (n + 2*m) % m
    return n % m

key = ascii_uppercase + ' \''
c = pi * 60
spacing = c / len(key)

dist_right = {key[i]: i * spacing for i in range(len(key))}
dist_left = {key[-i]: i * spacing for i in range(len(key))}

for _ in range(int(input())):
    travelled = 0
    msg = input()

    for i in range(len(msg) - 1):
        travelled += min(mod(dist_right[msg[i + 1]] - dist_right[msg[i]], c), mod(dist_left[msg[i + 1]] - dist_left[msg[i]], c))

    print((travelled / 15) + len(msg))