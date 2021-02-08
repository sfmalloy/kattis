N, Q = map(int, input().split())
locations = [int(c) for c in input().split()]

for _ in range(Q):
    q, a, b = map(int, input().split())
    if (q == 1):
        locations[a - 1] = b
    else:
        print(abs(locations[a - 1] - locations[b - 1]))

