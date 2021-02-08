# Direction constants
DOWN       = 0
RIGHT			 = 1
RIGHT_DIAG = 2
LEFT_DIAG  = 3

class node:
	def __init__(self, row, col, color, direction, count):
		self.row = row
		self.col = col
		self.color = color
		self.direction = direction
		self.count = count
	def __str__(self):
		return f'row={self.row} col={self.col} color={self.color} direction={self.pdir(self.direction)} count={self.count}'
	def pdir(self, d):
		if d == DOWN:
			return 'down'
		if d == RIGHT:
			return 'right'
		if d == RIGHT_DIAG:
			return 'right_diag'
		if d == LEFT_DIAG:
			return 'left_diag'
R,C,N = map(int, input().split())
board = []

for r in range(R):
	board.append(input().split())


def init_frontier():
	frontier = []
	for d in range(0, 4):
		frontier.append(node(0, 0, board[0][0], d, 1))
	return frontier

def expand(n, direction):
	next_row = n.row
	next_col = n.col
	if direction == DOWN:
		next_row += 1
	elif direction == RIGHT:
		next_col += 1
	elif direction == RIGHT_DIAG:
		next_row += 1
		next_col += 1
	elif direction == LEFT_DIAG:
		next_row += 1
		next_col -= 1

	if next_row == R or next_col == C or next_col == -1:
		return None

	count = 1
	if board[next_row][next_col] == n.color and n.direction == direction:
		count = n.count + 1
	elif board[next_row][next_col] == n.color:
		count = 2

	return node(next_row, next_col, board[next_row][next_col], direction, count)

# consider returning path and return last piece in path to get winner.
# also do a bfs so you don't have to do this nonsense lol, keep a queue going
def find_winner(frontier=init_frontier()):
	while len(frontier) > 0:
		if frontier[0].count == N and frontier[0].color != 'O':
			return frontier[0].color
		curr = frontier[0]
		frontier.pop(0)
		for d in range(0, 4):
			frontier.insert(0, expand(curr, d))
			if frontier[0] is None:
				frontier.pop(0)	

	return None

winner = find_winner()
if winner is None:
	print('NONE')
elif winner[-1] == 'B':
	print('BLUE WINS')
else:
	print('RED WINS')
