from collections import defaultdict

rosters = defaultdict(set)

n = int(input())
for _ in range(n):
    line = input().split(' ')
    name = ' '.join(line[:2])
    cls = line[2]
    rosters[cls].add(name)

for cls in sorted(rosters.keys()):
    print(f'{cls} {len(rosters[cls])}')
