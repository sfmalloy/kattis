from fractions import Fraction

N = int(input())
nums = list(map(int, input().split()))
a = nums[0]
b = nums[1:]

for n in b:
  f = Fraction(a, n)
  print(f'{f.numerator}/{f.denominator}')