time = input()
bins = []
for t in time:
    bins.append(bin(int(t))[2:])
    while len(bins[-1]) < 4:
        bins[-1] = '0' + bins[-1]

s = ''
for c in range(4):
    rw = ''
    for r in range(0,2):
        rw += '.*'[int(bins[r][c])] + ' '
    rw += '  '
    for r in range(2,4):
        rw += '.*'[int(bins[r][c])] + (' ' if r==2 else '')
    print(rw)
