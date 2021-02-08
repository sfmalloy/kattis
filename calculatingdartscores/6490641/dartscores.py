def sum_path(path):
  s = 0
  for p in path:
    p = p.split()
    n = int(p[1])
    if p[0] == 'triple':
      s += 3*n
    elif p[0] == 'double':
      s += 2*n
    else:
      s += n
  return s

paths = [[]]
score = int(input())
cool_path = []
while len(paths) > 0:
  a = paths.pop(0).copy()
  b = a.copy()
  c = a.copy()
  if sum_path(a) == score:
    cool_path = a
  if len(a) < 3:
    for h in range(20, 0, -1):
      a.append(f'triple {h}')
      b.append(f'double {h}')
      c.append(f'single {h}')
      paths.insert(0, a.copy())
      paths.insert(0, b.copy())
      paths.insert(0, c.copy())
      a.pop()
      b.pop()
      c.pop()

if cool_path == []:
  print('impossible')
else:
  for p in cool_path:
    print(p)