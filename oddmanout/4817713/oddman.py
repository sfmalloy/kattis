n = int(input())

for i in range(0, n):
    couples = {}
    g = int(input())
    g_list = list(map(int, input().split()))
    g_list.sort()
    
    j = 0
    while (j < g):
        if (j == g - 1 or g_list[j] != g_list[j + 1]):
            print('Case #%d: %d' % (i + 1, g_list[j]))
            break
        else:
            j += 2
        
