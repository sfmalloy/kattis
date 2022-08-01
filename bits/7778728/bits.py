for _ in range(int(input())):
    num = input()
    max_ones = 0
    for i in range(1, len(num) + 1):
        sub = num[0:i]
        max_ones = max(max_ones, bin(int(sub)).count('1'))
    print(max_ones)
