s = 0
f = 1

for i in range(0, int(input()) + 1):
    s += 1 / f
    if (i >= 1):
        f *= i + 1

print(s)
