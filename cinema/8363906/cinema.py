n,m = map(int, input().split())
filled = 0
angry = 0
for c in iter(map(int, input().split())):
    if filled + c <= n:
        filled += c
    else:
        angry += 1
print(angry)
