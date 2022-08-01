points = dict()
for r in range(3):
    line = input().split()
    for c in range(3):
        points[int(line[c]) - 1] = (r, c)

d = 0
for i in range(len(points) - 1):
    a = points[i]
    b = points[i + 1]
    d += ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

print(d)
