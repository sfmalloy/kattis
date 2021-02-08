total = 0
for probs in input().split(';'):
  l = list(map(int, probs.split('-')))
  if len(l) == 2:
    total += l[1] - l[0] + 1
  else:
    total += 1
print(total)