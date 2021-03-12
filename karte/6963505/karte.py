line = input()
suits = {'P':13,'K':13,'H':13,'T':13}
seen = set()
i = 0
while i < len(line):
  c = line[i:i+3]
  if c in seen:
    print('GRESKA')
    exit(0)
  seen.add(c)
  suits[c[0]] -= 1
  i += 3

for c in suits:
  print(suits[c], end=' ')
print()

