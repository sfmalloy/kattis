proved = set()
N = int(input())

for i in range(1, N+1):
    assumptions, conclusion = input().split('->')
    for a in assumptions.split():
        if a not in proved:
            print(i)
            exit(0)
    for c in conclusion.split():
        proved.add(c)
print('correct')