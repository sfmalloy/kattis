from functools import lru_cache

@lru_cache(maxsize=None)
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

e = 0
for i in range(int(input())+1):
    e += 1 / fact(i)
print(e)
