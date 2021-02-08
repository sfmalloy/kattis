import sys

for line in sys.stdin:
	lst = list(map(int, line.split()))
	N = len(lst)

	for i in range(N):
		k = lst.pop(0)
		s = sum(lst)
		if k == s:
			print(k)
			break
		lst.append(k)
