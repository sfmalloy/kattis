n = int(input())
s = 0
for i in range(0, n):
    [q,y] = map(float, input().split())
    s += q * y

print(s)
