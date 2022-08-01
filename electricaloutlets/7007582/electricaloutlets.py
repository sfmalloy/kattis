N = int(input())

for _ in range(N):
    line = list(map(int, input().split()))
    k = line[0]
    print(sum(line[1:]) - k + 1)
