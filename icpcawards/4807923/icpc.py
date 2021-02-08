n = int(input())
u_set = set()

for i in range(0, n):
    if (len(u_set) == 12):
        break
    [u, team] = input().split()
    if (not u in u_set):
        u_set.add(u)
        print(u, team)
