n = int(input())

for i in range(0, n):
    [r,e,c] = map(int, input().split())
    if (r > e - c):
        print('do not advertise')
    elif (r < e - c):
        print('advertise')
    else:
        print('does not matter')

