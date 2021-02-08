n = int(input())
seen = []

for i in range(n):
    seen.append(int(input()))

if (seen[len(seen) - 1] == n):
    print('good job')
else:
    seen = sorted(seen)
    prev = 1
    for obstacle in seen:
        for i in range(prev, obstacle):
            print(i)
        prev = obstacle + 1

    if (prev < n - 1):
        for i in range(prev, n):
            print(i)

    num_seen = len(seen)
