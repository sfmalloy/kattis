from math import sqrt

a,b,c,d = map(int, input().split())
s = sum([a,b,c,d]) / 2
p = 1
for x in [a,b,c,d]:
    p *= s-x
A = sqrt(p)
print(A)