N = int(input())

mx = 0
s1, d1 = map(int, input().split())
for _ in range(N - 1):
    s2, d2 = map(int, input().split())
    mx = max(mx, (d2 - d1) // (s2 - s1))
    s1, d1 = s2, d2
print(mx)