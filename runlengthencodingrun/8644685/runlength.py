mode, line = input().split()

ans = ''
if mode == 'E':
    curr = line[0]
    i = 0
    while True:
        n = 0
        while i < len(line) and curr == line[i]:
            n += 1
            i += 1
        ans += f'{curr}{n}'
        if i < len(line):
            curr = line[i]
        else:
            break
else:
    for i in range(0, len(line), 2):
        char = line[i]
        n = int(line[i+1])
        ans += char * n

print(ans)
