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
    
    return len(rows) == len(taken_spots) and len(cols) == len(taken_spots) and len(taken_spots) == 8

n = 8
taken_spots = []

for row in range(n):
    line = input()
    col = 0
    for c in line:
        if c == '*':
            taken_spots.append(tuple([col, row]))
        col += 1

valid = check_dupes(taken_spots)

if valid:
    for i in range(n):
        curr = taken_spots.pop()
        if not check_slopes(curr[1], curr[0], taken_spots):
            valid = False
            break
        
        taken_spots.insert(0, curr)

print(('' if valid else 'in') + 'valid')