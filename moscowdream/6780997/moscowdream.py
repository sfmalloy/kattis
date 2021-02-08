a,b,c,n = map(int, input().split())
valid = all([a>0,b>0,c>0,n>2]) and a+b+c>=n
if valid:
  print('YES')
else:
  print('NO')
