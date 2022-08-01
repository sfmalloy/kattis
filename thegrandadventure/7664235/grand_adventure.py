backpack = {'$': 0, '|': 0, '*': 0}

for _ in range(int(input())):
    success = True
    for c in input():
        if c == 'b':
            if backpack['$'] > 0:
                backpack['$'] -= 1
            else:
                success = False
                break
        elif c == 't':
            if backpack['|'] > 0:
                backpack['|'] -= 1
            else:
                success = False
                break
        elif c == 'j':
            if backpack['*'] > 0:
                backpack['*'] -= 1
            else:
                success = False
                break
        elif c != '.':
            backpack[c] += 1
    if any(i > 0 for i in backpack.values()):
        success = False
    print('YES' if success else 'NO')
    for b in backpack:
        backpack[b] = 0
    