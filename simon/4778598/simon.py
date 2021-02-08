T = int(input())

for i in range(T):
    curr = input()
    if (len(curr) > 10 and curr[0:10] == 'simon says'):
        print(curr[11:])
    else:
        print()
