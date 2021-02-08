M = S = 0

for _ in range(int(input())):
    m, s = map(int, input().split())
    M += m
    S += s
M *= 60

if (S <= M):
    print('measurement error')
else:
    print(S / M)