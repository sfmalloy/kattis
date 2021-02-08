N = int(input())

names = []
for i in range(N):
	names.append(input())

inc = sorted(names)
dec = sorted(names, reverse=True)

if inc == names:
	print('INCREASING')
elif dec == names:
	print('DECREASING')
else:
	print('NEITHER')

