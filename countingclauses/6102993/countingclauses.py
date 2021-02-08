m, n = map(int, input().split())

for _ in range(m):
    l = list(map(int, input().split()))
    _ = sum(l)

if m >= 8:
    print('satisfactory')
else:
    print('unsatisfactory')