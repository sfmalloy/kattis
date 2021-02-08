r,c,zr,zc = map(int, input().split())

old = []
for i in range(r):
	old.append(input())

new = []

for i in range(r):
	new_row = ''
	for j in range(c):
		for _ in range(zc):
			new_row += old[i][j]
	for _ in range(zr):
		new.append(new_row)

for line in new:
	print(line)
