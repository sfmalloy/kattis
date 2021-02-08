mode, s_in = input().split()

if mode == 'E':
  c = 1
  s = ''
  for i in range(len(s_in) - 1):
    if s_in[i] == s_in[i + 1]:
      c += 1
    else:
      s += s_in[i] + str(c)
      c = 1
  s += s_in[-1] + str(c)
  print(s)
else:
  for i in range(0, len(s_in), 2):
    l = s_in[i]
    n = int(s_in[i + 1])
    print(l * n, end='')
  print()
