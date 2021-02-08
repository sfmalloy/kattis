import sys
from math import sqrt

def dist(x1, y1, x2, y2):
  return sqrt((x2 - x1)**2 + (y2 - y1)**2)

gx, gy, dx, dy = map(float, input().split())
gspeed = 1
dspeed = 2

holes = []
for line in sys.stdin:
  x, y = map(float, line.rstrip().split())
  holes.append((x, y))

found = False
for x, y in holes:
  if dist(gx, gy, x, y) <= dist(dx, dy, x, y) / 2:
    found = True
    print(f'The gopher can escape through the hole at ({x},{y}).')
    break

if not found:
  print('The gopher cannot escape.')