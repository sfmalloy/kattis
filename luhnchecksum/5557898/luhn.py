def double(d):
	d *= 2
	if (d > 9):
		d = sum(map(int, str(d)))
	return d

cases = int(input())

for i in range(cases):
	n = ''.join(reversed(input()))
	new = []

	for i in range(len(n)):
		if (i + 1) % 2 == 0:
			new.append(double(int(n[i])))
		else:
			new.append(int(n[i]))
	
	s = sum(new)
	print('PASS' if s % 10 == 0 else 'FAIL')
