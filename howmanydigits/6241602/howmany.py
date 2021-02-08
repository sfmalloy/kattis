import sys
from math import sqrt, log, pi, exp, log10

def fact_len(n):
	if n < 2:
		return 1
	return int((n*log(n) - n + 0.5*log(n) + log(sqrt(2*pi))) / log(10)) + 1

for c in sys.stdin:
	print(fact_len(int(c.rstrip())))

