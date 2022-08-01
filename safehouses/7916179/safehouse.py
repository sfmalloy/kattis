N = int(input())

def dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

safehouses = []
spies = []

for r in range(N):
    line = input()
    for c in range(N):
        if line[c] == 'H':
            safehouses.append((r,c))
        if line[c] == 'S':
            spies.append((r,c))

max_dist = 0
for s in spies:
    nearest_dist = float('inf')
    nearest_house = (0, 0)
    for h in safehouses:
        d = dist(s, h)
        if d < nearest_dist:
            nearest_dist = d
            nearest_house = h
    max_dist = max(nearest_dist, max_dist)

print(max_dist)