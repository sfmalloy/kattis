line = input().split()
h = int(line[0])
root = (2 ** (h + 1)) - 1

if (len(line) == 2):
    path = line[1]
    d = 1
    for c in path:
        if (c == 'L'):
            root -= d
            d *= 2
        else:
            root -= d + 1
            d *= 2
            d += 1

print(root)
