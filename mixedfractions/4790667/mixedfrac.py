[a, b] = map(int, input().split())

while (a != 0 and b != 0):
    x = a % b
    y = int(a / b)

    print(y, x, '/', b)

    [a, b] = map(int, input().split())
