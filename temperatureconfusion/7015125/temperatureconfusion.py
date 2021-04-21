from fractions import Fraction
n,d = map(int, input().split('/'))
f = Fraction(5,9) * (Fraction(n,d) - 32)
print(f'{f.numerator}/{f.denominator}')