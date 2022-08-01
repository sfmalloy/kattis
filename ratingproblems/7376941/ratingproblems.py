n,k = map(int, input().split())

mn = 0
for _ in range(k):
    mn += int(input())
mx = (3*(n-k) + mn) / n
mn = (-3*(n-k) + mn) / n

print(mn, mx)