pieces = [1,1,2,2,2,8]
has = list(map(int, input().split()))
for i in range(6):
	print(pieces[i] - has[i], end=' ')
