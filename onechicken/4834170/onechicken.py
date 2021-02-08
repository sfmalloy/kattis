a, b = map(int, input().split())
diff = b - a
piece = 'piece' if (abs(diff) == 1) else 'pieces'

if (b - a > 0):
    print('Dr. Chaz will have', diff, piece, 'of chicken left over!')
else:
    print('Dr. Chaz needs', abs(diff), 'more', piece, 'of chicken!')

