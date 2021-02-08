scored = {'A' : 0, 'B' : 0}
win_by_two = False

record = input()
for i in range(0, len(record) - 1, 2):
    person = record[i]
    points = int(record[i + 1])
    scored[person] += points

if (scored['A'] > scored['B']):
    print('A')
else:
    print('B')
