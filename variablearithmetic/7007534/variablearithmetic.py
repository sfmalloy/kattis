import re
import sys

vars = {}

for line in sys.stdin:
    line = line.strip()
    if re.search("\+", line):
        lexemes = line.split('+ ')
        leftover = []
        s = 0
        for l in lexemes:
            l = l.strip(' ')
            if l.isnumeric():
                s += int(l)
            elif l in vars:
                s += vars[l]
            else:
                leftover.append(l)
        valid_s = s != 0 or (s == 0 and re.search("0", line))
        if valid_s:
            print(s, end='')
        if len(leftover) > 0:
            if valid_s:
                print(' + ', end='')
            print(f'{" + ".join(leftover)}', end='')
        print()
    elif re.search('=', line):
        lexemes = line.split(' = ')
        vars[lexemes[0]] = int(lexemes[1])
    elif line == '0':
        break
    else:
        if line in vars:
            print(vars[line])
        else:
            print(line)

