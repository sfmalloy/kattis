n = int(input())
caps = [i for i in range(1, n + 1)]
canisters = sorted(list(map(int, input().split())))

frac = 1.0
popped = False

for b, c in zip(caps, canisters):
    if b >= c:
        frac = min(frac, c / b)
    elif b < c:
        popped = True
        break

print('impossible' if popped else frac)