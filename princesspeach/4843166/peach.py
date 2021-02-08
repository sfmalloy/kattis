n, y = map(int, input().split())
seen = set()

for i in range(y):
    seen.add(int(input()))

seen = sorted(seen)

prev = 0
for obstacle in seen:
    for i in range(prev, obstacle):
        print(i)
    prev = obstacle + 1

if (prev < n - 1):
    for i in range(prev, n):
        print(i)

num_seen = len(seen)
print(f'Mario got {num_seen} of the dangerous obstacles.')
