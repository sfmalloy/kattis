color_list = {}

for i in range(0, int(input())):
    [a,b] = input().split()
    c = ''
    r = 0
    if (ord(a[0]) <= 57): 
        c = b
        r = int(a) / 2
    else:
        c = a
        r = int(b)

    color_list[r] = c

for r,c in sorted(color_list.items()):
    print(c)

