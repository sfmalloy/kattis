h, w, n = map(int, input().split())
bricks = list(map(int, input().split()))

sad = False
idx = 0
for i in range(h):
  partial = 0
  while partial < w:
    partial += bricks[idx]
    idx += 1
  if partial % w != 0:
    sad = True
    print('NO')
    break

if not sad:
  print('YES')