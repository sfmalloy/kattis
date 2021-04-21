num_rows, num_cols = map(int, input().split())
rows = [list(map(str, input())) for _ in range(num_rows)]

def valid_seat(r,c,char):
    return (0 <= r < num_rows) and (0 <= c < num_cols) and rows[r][c] == char

# Find empty seat with largest neighbor count
best_seat = (0, 0, 0)
for r in range(num_rows):
    for c in range(num_cols):
        if rows[r][c] == '.':
            seat_count = 0
            for rr in range(-1,2):
                for cc in range(-1,2):
                    if valid_seat(r+rr,c+cc,'o'):
                        seat_count += 1
            if seat_count > best_seat[0]:
                best_seat = (seat_count,r,c)

rows[best_seat[1]][best_seat[2]] = 'o'

shooketh = set()
for r in range(num_rows):
    for c in range(num_cols):
        if rows[r][c] == 'o':
            for rr in range(-1,2):
                for cc in range(-1,2):
                    if (valid_seat(r+rr,c+cc,'o') and (r+rr,c+cc,r,c) not in shooketh
                        and not (rr == 0 and cc == 0)):
                        shooketh.add((r,c,r+rr,c+cc))

print(len(shooketh))
