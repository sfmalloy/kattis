from math import log2

[m,n,t] = map(int, input().split())

valid = False
if (t == 1):
    f = n
    k = n - 1
    while (f <= m and k > 0):
        f *= k
        k -= 1

    valid = f <= m
elif (t == 2):
    two = 2
    for i in range(1, n):
        if (two <= m):
            two *= 2
        else:
            break

    valid = two <= m
elif (t == 3):
    valid = pow(n, 4) <= m
elif (t == 4):
    valid = pow(n, 3) <= m
elif (t == 5):
    valid = pow(n, 2) <= m
elif (t == 6):
    valid = (n * log2(n)) <= m
else:
    valid = n <= m

print('AC' if valid else 'TLE')
