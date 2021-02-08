n, h, v = map(int, input().split())
print(4 * max(v, abs(n-v)) * max(h, abs(n-h)))