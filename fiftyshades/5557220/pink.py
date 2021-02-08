import re

N = int(input())

color = re.compile('(\S)*(pink|rose)(\S)*', re.IGNORECASE)
count = 0

for i in range(N):
	if color.match(input().lower()):
		count += 1

if count == 0:
	print('I must watch Star Wars with my daughter')
else:
	print(count)
