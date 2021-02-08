import itertools

N = int(input())
while (N != 0):
	a = [int(input()) for _ in range(N)]
	b = [int(input()) for _ in range(N)]

	a_sort = sorted(a.copy())
	b_sort = sorted(b.copy())

	m = {}
	for it in zip(a_sort, b_sort):
		m[it[0]] = it[1]
	
	for i in a:
		print(m[i])
	
	print('')
	N = int(input())
