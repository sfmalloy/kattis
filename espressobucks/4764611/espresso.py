[n, m] = map(int, input().split())
espresso_map = [input() for i in range(0, n)]

def needsCaffine(espresso_map, row, col):
    if (row - 1 >= 0 and espresso_map[row - 1][col] == 'E'):
        return False
    if (row + 1 < len(espresso_map) and espresso_map[row + 1][col] == 'E'):
        return False
    if (col - 1 >= 0 and espresso_map[row][col - 1] == 'E'):
        return False
    if (col + 1 < len(espresso_map[0]) and espresso_map[row][col + 1] == 'E'):
        return False

    return True

for i in range(0, n):
    for j in range(0, m):
        if (espresso_map[i][j] == '.' and needsCaffine(espresso_map, i, j)):
            espresso_map[i] = espresso_map[i][:j] + 'E' + espresso_map[i][j + 1:]
    
    print(espresso_map[i])
