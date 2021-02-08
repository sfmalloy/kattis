n = int(input())
while (n != -1):
    tot = 0
    prev_t = 0
    for i in range(n):
        [s,t] = map(int, input().split())
        tot += s * (t - prev_t)
        prev_t = t
    print(tot,'miles')
    n = int(input())
