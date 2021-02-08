x, n = int(input()), int(input())
curr_total = x

for i in range (0, n):
    curr_total += x - int(input())

print(curr_total)
