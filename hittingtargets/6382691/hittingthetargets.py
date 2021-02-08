m = int(input())
rectangles = []
circles = []

for _ in range(m):
  line = input().split()
  shape = line[0]
  dims = list(map(int, line[1:]))

  if shape[0] == 'r':
    rectangles.append(dims)
  else:
    circles.append(dims)

def in_circle(c, x, y):
  return c[2]**2 >= abs(c[0] - x)**2 + abs(c[1] - y)**2

def in_rect(r, x, y):
  return x >= r[0] and x <= r[2] and y >= r[1] and y <= r[3]

n = int(input())
for _ in range(n):
  x, y = map(int, input().split())
  t = 0
  for r in rectangles:
    t += int(in_rect(r, x, y))
  for c in circles:
    t += int(in_circle(c, x, y))
  print(t)
