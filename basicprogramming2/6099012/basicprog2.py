FOUR_SEVENS = 1
UNIQUE      = 2
HALF_SAME   = 3
MEDIANS     = 4
PRINT_RANGE = 5

N, t = map(int, input().split())
A = list(map(int, input().split()))
if t == FOUR_SEVENS:
    found = False
    elems = set(i for i in A)
    for i in elems:
        if 7777 - i != i and 7777 - i in elems:
            found = True
            break
    
    print('Yes' if found else 'No')
elif t == UNIQUE:
    elems = set(i for i in A)
    print('Unique' if len(elems) == len(A) else 'Contains duplicate')
elif t == HALF_SAME:
    counts = {}
    for i in A:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    
    found = False
    for c in counts:
        if counts[c] > N // 2:
            found = True
            print(c)
            break
    if not found:
        print(-1)
elif t == MEDIANS:
    A.sort()
    half_len = len(A) // 2
    if len(A) % 2 == 0:
        print(f'{A[half_len - 1]} {A[half_len]}')
    else:
        print(f'{A[half_len]}')
elif t == PRINT_RANGE:
    B = []
    for i in A:
        if i in range(100, 1000):
            B.append(i)
    B.sort()

    for b in B:
        print(b, end=' ')
    print()