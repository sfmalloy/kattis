T = int(input())

for _ in range(T):
    case = list(map(int, input().split(' ')))
    case.pop()
    extra = 0
    pop = 1
    for t in case:
        if (t > pop * 2):
            extra += t - (pop * 2)
        pop = t
    print(extra)
