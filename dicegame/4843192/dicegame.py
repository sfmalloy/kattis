g = sum(list(map(int, input().split())))
e = sum(list(map(int, input().split())))

if (g == e):
    print('Tie')
elif (g < e):
    print('Emma')
else:
    print('Gunnar')
