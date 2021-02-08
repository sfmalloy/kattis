presses = int(input())
a = 0
b = 1

for _ in range(presses - 1):
    t = a
    a = b
    b += t

print(a, b)
