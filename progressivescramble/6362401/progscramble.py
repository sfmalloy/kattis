N = int(input())

def val(s):
  if s == ' ':
    return 0
  return ord(s) - 96

def symbol(s):
  s %= 27
  if s == 0:
    return ' '
  return chr(96 + s)

def encode(msg):
  enc = ''
  prev = 0
  for s in msg:
    v = val(s) + prev
    enc += symbol(v)
    prev = v
  return enc

def decode(msg):
  dec = ''
  prev = 0
  vals = []
  for s in msg:
    v = val(s)
    while v < prev:
      v += 27
    vals.append(v)
    prev = v
  
  dec_vals = []
  for i in range(len(vals)-1, 0, -1):
    dec_vals.insert(0, vals[i] - vals[i-1])
  dec_vals.insert(0, vals[0])

  for v in dec_vals:
    dec += symbol(v)

  return dec

for _ in range(N):
  line = input()
  mode = line[0]
  msg = line[2:]

  if mode == 'e':
    print(encode(msg))
  else:
    print(decode(msg))