def swap(a, b, lst):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp

N = int(input())
ordered = [i for i in range(1, N+1)]
new = ordered.copy()

dists = list(map(int, input().split()))
for d,i in zip(ordered[1:], dists):
    new[i + 1] = d

for x in new:
    print(x, end=' ')
print()