n = int(input())

while n != -1:
  matrix = [list(map(int, input().split())) for _ in range(n)]

  weak = []
  for r in range(n):
    found = False
    for c1 in range(n):
      for c2 in range(c1+1, n):
        if matrix[r][c1] == 1 and matrix[r][c2] == 1:
          if matrix[c1][c2] == 1 and matrix[c2][c1] == 1:
            found = True
            break
        if found:
          break
      if found:
        break
    if not found:
      weak.append(r)
  for w in weak:
    print(w, end=' ')
  print()

  n = int(input())
