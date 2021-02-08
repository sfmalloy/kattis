from fractions import Fraction

def run_length_encoding(i):
  binary = [int(c) for c in reversed(bin(i).split('b')[1])]
  frac = []
  ones = zeros = 0
  counting_ones = True
  for d in binary:
    if counting_ones and d == 1:
      ones += 1
    elif counting_ones and d == 0:
      frac.append(ones)
      ones = 0
      zeros += 1
      counting_ones = False
    elif not counting_ones and d == 0:
      zeros += 1
    elif not counting_ones and d == 1:
      frac.append(zeros)
      zeros = 0
      ones += 1
      counting_ones = True
  
  frac.append(ones if ones != 0 else zeros)
  return frac

def continued_frac(f, k=0):
  if len(f) == k:
    return 0
  return Fraction(1, f[k] + continued_frac(f, k + 1))

for _ in range(int(input())):
  k, n = map(int, input().split())
  digits = run_length_encoding(n)
  f = 1 / continued_frac(digits)
  if f.denominator == 1:
    print(k, f'{f}/1')
  else:
    print(k, f)