from math import floor, ceil

N = int(input())

for _ in range(N):
    b,p = map(float, input().split())
    t = p / b
    bpm = 60 / t
    dbpm = 60 / p
    print(f'{bpm - dbpm} {bpm} {bpm + dbpm}')