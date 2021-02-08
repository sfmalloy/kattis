from math import sqrt

N = int(input())

def transpose(s):
  jmp = int(sqrt(len(s)))
  t = ''
  for i in range(jmp - 1, -1, -1):
    for j in range(jmp):
      t += s[j*jmp + i]
  return t

for _ in range(N):
  print(transpose(input()))