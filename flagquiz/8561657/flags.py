q = input()
n = int(input())

alts = []
for _ in range(n):
    alts.append(tuple(input().strip().split(',')))

diffs = {}
for a in alts:
    max_diff = 0
    for c in alts:
        d = 0
        if a != c:
            for ai,ci in zip(a,c):
                if ai != ci:
                    d += 1
            max_diff = max(d,max_diff)
    diffs[a] = max_diff

mx = min(diffs.values())
for a in alts:
    if diffs[a] == mx:
        print(', '.join(a))
