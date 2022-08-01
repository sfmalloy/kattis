L,_ = map(int, input().split())

foods = set()
rows = []
for _ in range(L):
    rows.append(set(input().split()))
    foods |= rows[-1]

for r in rows:
    foods &= r

common = sorted(list(foods))
print(len(common))
for c in common:
    print(c)