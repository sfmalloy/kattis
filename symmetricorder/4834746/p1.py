n = int(input())
c = 1
while (n != 0):
    l = [None] * n
    for i in range(0, n // 2):
        l[i] = input()
        l[n - i - 1] = input()

    if (n % 2 == 1):
        l[(n // 2)] = input()

    print('SET',c)
    for name in l:
        print(name)
    n = int(input())
    c += 1 

