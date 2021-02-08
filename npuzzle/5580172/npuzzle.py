import string

letters = list(map(str, string.ascii_uppercase[:15]))
letters.append('.')
letter_map = {letters.pop(0) : (i, j) for i in range(4) for j in range(4)}

dist = 0
for i in range(4):
    line = list(map(str, input()))
    for j in range(4):
        l = line[j]
        if l != '.':
            init = letter_map[l]
            dist += abs(i - init[0]) + abs(j - init[1])

print(dist)