N = int(input()) % 2

str_a = input()
l = len(str_a)

a = int(str_a, 2)
b = int(input(), 2)

if N == 1:
	b = (~b + (1 << l)) % (1 << l)

print('Deletion', ('succeeded' if a == b else 'failed'))
