g,s,c = map(int, input().split())

total_buy = 3*g + 2*s + c

victory = {'Province': 8, 'Duchy': 5, 'Estate': 2}
treasure = {'Gold': 6, 'Silver': 3, 'Copper': 0}

buy_victory = ''
buy_treasure = ''

for v in victory:
  if total_buy >= victory[v]:
    buy_victory = v
    break

for t in treasure:
  if total_buy >= treasure[t]:
    buy_treasure = t
    break

print(buy_victory, end='')
if buy_victory != '' and buy_treasure != '':
  print(' or ', end='')
print(buy_treasure)