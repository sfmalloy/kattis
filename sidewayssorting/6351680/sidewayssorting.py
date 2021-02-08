h, w = map(int, input().split())

while h != 0 and w != 0:
  lines = ['' for _ in range(w)]
  for _ in range(h):
    line = input()
    for k in range(w):
      lines[k] += line[k]
  words = sorted(lines, key=lambda s: s.lower())
  sortedlines = ['' for _ in range(h)]
  for i in range(w):
    for j in range(h):
      sortedlines[j] += words[i][j]
  for x in sortedlines:
    print(x)
  print()
  h, w = map(int, input().split())
