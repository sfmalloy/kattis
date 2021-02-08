
def combine(a, b, x=''):
	print(f'{a}{x}{b}')

y, p = input().split()
if y[-1] == 'e':
	combine(y, p, 'x')
elif y[-1] in 'aiou':
	combine(y[:-1], p, 'ex')
elif y[-2:] == 'ex':
	combine(y, p)
else:
	combine(y, p, 'ex')
