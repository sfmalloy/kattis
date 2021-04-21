import re

pows = [1, 2, 4, 8, 16, 32, 64]

words = input().split()
letters = []
pow2 = 6
curr = 0
for w in words:
    w = ''.join(list(filter(lambda s: re.match(r'[A-Za-z0-9]', s), w)))
    if re.match(r'(u*m*)+$', w):
        for d in w:
            if d == 'u':
                curr += pows[pow2]
            pow2 -= 1
            if pow2 < 0:
                letters.append(chr(curr))
                pow2 = 6
                curr = 0

print(''.join(letters))
