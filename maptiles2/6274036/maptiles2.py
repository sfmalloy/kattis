s = input()
x_data = ''
y_data = ''
for c in s:
	x_data += str(int(c) % 2)
	y_data += str(int(c) // 2)
print(f'{len(s)} {int(x_data, 2)} {int(y_data, 2)}')
