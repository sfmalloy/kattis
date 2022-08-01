n,m = map(int, input().split())
filled = 0
inside = 0
for c in iter(map(int, input().split())):
    if filled + c <= n:
        filled += c
        inside += 1
    else:
        break
print(m - inside)
