n = int(input())

t1,v1 = map(float, input().split())
area = 0
for i in range(0, n - 1):
    t2,v2 = map(float, input().split())
    area += (((v1 + v2) / 2) * abs(t2 - t1))
    t1,v1 = t2,v2

print(area / 1000)
