from collections import defaultdict
cases = int(input())

for _ in range(cases):
    n,m = map(int, input().split())
    prizes = {}
    for _ in range(n):
        line = list(map(int, input().split()))
        key = tuple(line[1:-1])
        val = line[-1]
        prizes[key] = val
    recv = list(map(int, input().split()))
    counts = defaultdict(int)
    for r,i in zip(recv,range(1,m+1)):
        counts[i] += r
    cash = 0
    for p in prizes:
        able = 1000000
        for s in p:
            able = min(counts[s], able)
        for s in p:
            counts[s] -= able
        cash += able * prizes[p]
    print(cash)
