list(map(lambda a, b: print(a[b], end=' '), [dict(list(map(lambda a, b: (a, int(b)), "ABC", sorted(list(map(int, input().split()))))))] * 3, map(str, input())))
