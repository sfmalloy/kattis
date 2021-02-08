cards = input().split()
counts = { }

for card in cards:
    if card[0] not in counts:
        counts[card[0]] = 1
    else:
        counts[card[0]] += 1

strong = 0
for card in counts:
    strong = max(strong, counts[card])

print(strong)