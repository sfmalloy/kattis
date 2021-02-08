def check_slopes(r, c, taken_spots):
	for spot in taken_spots:
		if abs(r - spot[1]) == abs(c - spot[0]):
			return False
	return True

def check_dupes(taken_spots):
    rows = set()
    cols = set()

    for spot in taken_spots:
        rows.add(spot[1])
        cols.add(spot[0])
    
    return len(rows) == len(taken_spots) and len(cols) == len(taken_spots)

n = int(input())
taken_spots = []

for i in range(n):
    taken_spots.append(tuple(list(map(int, input().split()))))

valid = check_dupes(taken_spots)

if valid:
    for i in range(n):
        curr = taken_spots.pop()
        if not check_slopes(curr[1], curr[0], taken_spots):
            valid = False
            break
        
        taken_spots.insert(0, curr)

print(('' if valid else 'IN') + 'CORRECT')

# def valid_queens(n, holes, taken_spots=[], prev=-1, d=0):
# 	valid = 0
# 	for i in range(n):
# 		if not holes[d][i] and i not in taken_spots:
# 			if prev == -1 or check_slopes(d, i, taken_spots):
# 				if d == n - 1:
# 					return 1
# 				taken_spots.append(i)
# 				valid += valid_queens(n, holes, taken_spots, i, d+1)
# 				taken_spots.pop()
# 	return valid

# while True:
# 	n, m = map(int, input().split())
# 	if n == 0 and m == 0:
# 		break
# 	holes = [[False for _ in range(n)] for _ in range(n)]
# 	for h in range(m):
# 		r, c = map(int, input().split())
# 		holes[r][c] = True
# 	print(valid_queens(n, holes))
