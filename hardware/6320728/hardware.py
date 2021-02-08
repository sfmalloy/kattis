orders = int(input())

for _ in range(orders):
  name = input()
  
  num_addr, addr_word = input().split()
  num_addr = int(num_addr)

  digits = {str(i):0 for i in range(0, 10)}
  house_nums = []
  while len(house_nums) < num_addr:
    line = input().split()
    if line[0] == '+':
      first, last, step = map(int, line[1:])
      house_nums += [str(i) for i in range(first, last+1, step)]
    else:
      house_nums.append(line[0])
  
  for n in house_nums:
    for d in n:
      digits[d] += 1
  
  print(name)
  print(f'{num_addr} {addr_word}')
  s = 0
  for d in digits:
    print(f'Make {digits[d]} digit {d}')
    s += digits[d]
  if s == 1:
    print(f'In total {s} digit')
  else:
    print(f'In total {s} digits')
