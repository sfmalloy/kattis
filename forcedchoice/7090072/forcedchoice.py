n,p,s = map(int, input().split())

counts = [0 for _ in range(n+1)]
steps = []
for _ in range(s):
    cards = list(map(int, input().split()))
    m = cards[0]
    cards = cards[1:]
    keep = 'REMOVE'
    if p in cards:
        keep = 'KEEP'
    print(keep)
