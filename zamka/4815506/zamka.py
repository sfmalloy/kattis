l = int(input())
d = int(input())
x = int(input())
n = l
m = d

def digit_sum(n):
    s = 0
    while (n > 0):
        s += n % 10
        n = n // 10
    return s

while (digit_sum(n) != x):
    n += 1

while (digit_sum(m) != x):
    m -= 1

print(n)
print(m)
