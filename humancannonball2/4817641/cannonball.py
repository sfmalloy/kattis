from math import sin, cos, radians

n = int(input())

for i in range(0, n):
    [v0, theta, x, h1, h2] = map(float, input().split())
    t = x / (v0 * cos(radians(theta)))
    y = (v0 * t * sin(radians(theta))) - (0.5 * 9.81 * (t ** 2))

    print('Safe' if y >= h1 + 1 and y <= h2 - 1 else 'Not Safe')
