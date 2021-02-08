n = int(input())

def digit_sum(n):
    return sum(list(map(int, list(str(n)))))

while ((n / digit_sum(n)) % 1 != 0):
    n += 1

print(n)
