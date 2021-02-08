from math import ceil

def size(c_w, c_max):
	return 8 + ceil(40*((c_w - 4) / (c_max - 4)))

def get_width(t, P):
	return ceil((9/16) * t * P)

W, N = map(int, input().split())
case = 1
while not (W == 0 and N == 0):
	c = {}
	c_max = 0
	for _ in range(N):
		word, count = input().split()
		c[word] = int(count)
		c_max = max(int(count), c_max)

	heights = {}
	widths = {}
	for w in sorted(c):
		heights[w] = size(c[w], c_max)
		widths[w] = get_width(len(w), heights[w])

	total_height = 0
	height = 0
	width = 0
	words = list(heights.keys())
	i = 0
	while i < N:
		width = 0
		curr_heights = []
		while width < W and i < N:
			width += widths[words[i]] + 10
			curr_heights.append(heights[words[i]])
			i += 1
		if width - 10 > W:
			i -= 1
			total_height += max(curr_heights[:-1])
		else:
			total_height += max(curr_heights)
	print(f'CLOUD {case}: {total_height}')

	W, N = map(int, input().split())
	case += 1
