L, x = map(int, input().split())
count = bad = 0

for _ in range(x):
    command, n = input().split()
    n = int(n)

    if (command == 'enter'):
        if (n + count > L):
            bad += 1
        else:
            count += n
    elif (command == 'leave'):
        count -= n

print(bad)
