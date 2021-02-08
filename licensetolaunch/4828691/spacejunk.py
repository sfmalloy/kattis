n = int(input())
days = list(map(int, input().split()))
min_junk = 1000000001
min_day = 0
for i in range(n):
    min_day = i if (days[i] < min_junk) else min_day
    min_junk = days[min_day]

print(min_day)
