print((str(input())[-1] + str(abs(sum([(i if i < 0 else 0) for i in list(map(int,
	input().split()))]))))[1:])
