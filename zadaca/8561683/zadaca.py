from functools import reduce
from math import gcd

_ = input()
a = reduce(lambda a,b:a*b, map(int, input().split())) 
_ = input()
b = reduce(lambda a,b:a*b, map(int, input().split())) 
g = gcd(a,b)
if g > 10**9:
    print(str(g)[-9:])
else:
    print(g)
