ascii_to_symbol = {
  """xxxxx
x...x
x...x
x...x
x...x
x...x
xxxxx""": '0',  
  """....x
....x
....x
....x
....x
....x
....x""": '1',  
  """xxxxx
....x
....x
xxxxx
x....
x....
xxxxx""": '2',  
  """xxxxx
....x
....x
xxxxx
....x
....x
xxxxx""": '3',  
  """x...x
x...x
x...x
xxxxx
....x
....x
....x""": '4',  
  """xxxxx
x....
x....
xxxxx
....x
....x
xxxxx""": '5',  
  """xxxxx
x....
x....
xxxxx
x...x
x...x
xxxxx""": '6',  
  """xxxxx
....x
....x
....x
....x
....x
....x""": '7',  
  """xxxxx
x...x
x...x
xxxxx
x...x
x...x
xxxxx""": '8',  
  """xxxxx
x...x
x...x
xxxxx
....x
....x
xxxxx""": '9',  
  """.....
..x..
..x..
xxxxx
..x..
..x..
.....""": '+'
}

symbol_to_ascii = {
  '0':"""xxxxx
x...x
x...x
x...x
x...x
x...x
xxxxx""",  
  '1':"""....x
....x
....x
....x
....x
....x
....x""",  
  '2':"""xxxxx
....x
....x
xxxxx
x....
x....
xxxxx""",  
  '3':"""xxxxx
....x
....x
xxxxx
....x
....x
xxxxx""",  
  '4':"""x...x
x...x
x...x
xxxxx
....x
....x
....x""",  
  '5':"""xxxxx
x....
x....
xxxxx
....x
....x
xxxxx""",  
  '6':"""xxxxx
x....
x....
xxxxx
x...x
x...x
xxxxx""",  
  '7':"""xxxxx
....x
....x
....x
....x
....x
....x""",  
  '8':"""xxxxx
x...x
x...x
xxxxx
x...x
x...x
xxxxx""",  
  '9':"""xxxxx
x...x
x...x
xxxxx
....x
....x
xxxxx""",  
  '+':""".....
..x..
..x..
xxxxx
..x..
..x..
....."""
}

lines = [input() for _ in range(7)]
tokens = ['' for _ in range(1 + (len(lines[0]) // 6))]
for i in range(7):
  line = [c for c in lines[i]]
  for j in range(5, len(line), 6):
    line[j] = '#'
  joined = ''
  for l in line:
    joined += l
  tokenized = joined.split('#')
  for j in range(len(tokens)):
    tokens[j] += tokenized[j] + ('\n' if i < 6 else '')

s = ''
for t in tokens:
  s += ascii_to_symbol[t]

a, b = map(int, s.split('+'))
ans = a + b
digits = []

for d in str(ans):
  digits.append(symbol_to_ascii[d])

ans_lines = [d.split('\n') for d in digits]

for i in range(len(ans_lines[0])):
  for j in range(len(ans_lines)):
    if j < len(ans_lines) - 1:
      print(ans_lines[j][i], end='.')
    else:
      print(ans_lines[j][i])
