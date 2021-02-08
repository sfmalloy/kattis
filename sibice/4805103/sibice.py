import math

[n, w, h] = map(int, input().split())

for i in range(n):
    curr = int(input())
    diag = math.sqrt(math.pow(w, 2) + math.pow(h, 2))
    if (curr <= w or curr <= h or curr <= diag):
        print('DA')
    else:
        print('NE')

