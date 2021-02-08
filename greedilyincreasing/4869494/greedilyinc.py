n = int(input())
l = list(map(int, input().split()))
m = 0
g = []
size = 0
for i in l:
    if (i > m):
        m = i
        g.append(i)
        size += 1

print(size)
for i in g:
    print(str(i) + ' ', end = '')
