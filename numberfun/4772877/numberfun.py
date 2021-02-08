def is_possible(a, b, c):
    return (a + b == c or abs(a - b) == c or a * b == c or a / b == c or b / a == c)

n = int(input())

for i in range(0, n):
    [a,b,c] = map(int, input().split())
    print('Possible' if (is_possible(a, b, c)) else 'Impossible')
