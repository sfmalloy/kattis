cases = int(input())

for i in range(1, cases+1):
	_ = int(input())
	v1 = sorted(list(map(int, input().split())))
	v2 = sorted(list(map(int, input().split())), reverse=True)
	dot = 0
	for a,b in zip(v1, v2):
		dot += a * b
	print(f'Case #{i}: {dot}')
