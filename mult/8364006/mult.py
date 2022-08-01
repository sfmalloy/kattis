n = int(input())
first = int(input())

skip = False
i = 0
while i < n:
    k = int(input())
    if k % first == 0:
        print(k)
        i += 2
        if i < n:
            first = int(input())
    i += 1
