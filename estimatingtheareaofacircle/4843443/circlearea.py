from math import pi
r,m,c = map(float, input().split())

while (r != 0):
    m_over_c = c / m
    print(pi * r * r, 4 * r * r * m_over_c)
    r,m,c = map(float, input().split())
