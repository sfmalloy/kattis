n = int(input())
s = 0

for i in map(int, input().split()):
    if (i < 0):
        n -= 1
    else:
        s += i

print(s / n)
