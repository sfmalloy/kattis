import string

encrypt = input()
key = input()
letters = string.ascii_uppercase
letter_map = dict(map(lambda a, b: (a, b), letters, [i for i in range(26)]))

msg = ''
for i in range(len(key)):
	c = letter_map[encrypt[i]]
	k = letter_map[key[i]]
	if i % 2 == 0:
		msg += letters[(c - k) % 26]
	else:
		msg += letters[(c + k) % 26]

print(msg)
