diff = 0
count = int(input())

if count % 2 == 1:
    print('still running')
    exit(0)

diff = 0
for i in range(0, count, 2):
    a = int(input())
    b = int(input())
    diff += b - a

print(diff)
