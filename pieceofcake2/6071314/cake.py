print((lambda n, h, v: 4 * max(h, abs(n-h)) * max(v, abs(n-v)))(*tuple(map(int, input().split()))))
