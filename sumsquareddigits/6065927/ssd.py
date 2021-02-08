def ssd(a):
    return sum([x**2 for x in a])

def convert_decimal(dec, b):
    digits = []
    while dec > 0:
        digits.append(dec % b)
        dec = dec // b
    return digits

P = int(input())

for _ in range(P):
    K, b, n = map(int, input().split())
    n_b = convert_decimal(n, b)
    print(f'{K} {ssd(n_b)}')