n = int(input())

for _ in range(n):
    gnomes = list(map(int, input().split()))
    for i in range(2, gnomes[0]):
        if gnomes[i] - gnomes[i - 1] != 1:
            print(i)
            break