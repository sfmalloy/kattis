t = int(input())

for _ in range(t):
    n = int(input())
    stores = sorted(list(map(int, input().split())))
    dist = sum([(stores[i + 1] - stores[i]) for i in range(n - 1)])

    print(dist * 2)
