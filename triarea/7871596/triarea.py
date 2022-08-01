from functools import reduce
print(0.5*reduce(lambda a,b:a*b, list(map(int, input().split()))))