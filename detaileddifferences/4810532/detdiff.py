for i in range(int(input())):
    a,b = input(),input()
    line = ''
    for k in range(len(a)):
        line += '*' if a[k] != b[k] else '.'
    print(a)
    print(b)
    print(line + '\n')
