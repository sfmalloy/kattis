T = int(input())

for _ in range(T):
	k = int(input())
	final = init = 0

	for i in range(k):
		init = 2 * final + 0.5
		final = init
	print(int(2 * init))

	# P_f = P_i - ((P_i / 2) - 0.5)
	# 2 * P_f + 0.5 = P_i
