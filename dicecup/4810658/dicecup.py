[n,m] = map(int, input().split())

a = min(n,m)
b = max(n,m)

for i in range(a + 1, b + 2):
    print(i)
