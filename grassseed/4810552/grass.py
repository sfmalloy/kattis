cost,lawns = float(input()), int(input())
total = 0
for i in range(lawns):
    [w,l] = map(float, input().split())
    total += w * l * cost
print("%.7f" % total)
