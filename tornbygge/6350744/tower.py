N = int(input())
bricks = list(map(int, input().split()))

t = 0
i = 0
while i < len(bricks):
  while i < len(bricks) - 1 and bricks[i] >= bricks[i + 1]:
    i += 1
  i += 1
  t += 1
print(t)