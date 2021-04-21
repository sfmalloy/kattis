dest_x, dest_y = map(int, input().split())
n = int(input())
cmds = [input() for _ in range(n)]
valid_cmds = ['Forward', 'Left', 'Right']

N,E,S,W = 0,1,2,3

def goto_dest(cmds):
    x = 0
    y = 0
    d = N
    for cmd in cmds:
        if cmd == 'Forward':
            if d == N:
                y += 1
            elif d == E:
                x += 1
            elif d == S:
                y -= 1
            else:
                x -= 1
        elif cmd == 'Right':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
    return x == dest_x and y == dest_y

for i in range(n):
    old = cmds[i]
    for alt in valid_cmds:
        if alt != cmds[i]:
            cmds[i] = alt
            if goto_dest(cmds):
                print(f'{i+1} {alt}')
                exit(0)
            cmds[i] = old
