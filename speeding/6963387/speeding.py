n = int(input())
m = 0
t1,d1 = map(int, input().split())
for _ in range(n-1):
  t2,d2 = map(int, input().split())
  m = max((d2-d1)/(t2-t1), m)
  t1,d1 = t2,d2
print(int(m))
