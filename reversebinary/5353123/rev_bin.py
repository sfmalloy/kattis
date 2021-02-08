from math import log2

base10 = int(input())
base2 = 0
pow2 = 2 ** int(log2(base10)) 

while (base10 > 0):
	base2 += (base10 % 2) * pow2
	pow2 = pow2 // 2
	base10 = base10 // 2

print(base2)
