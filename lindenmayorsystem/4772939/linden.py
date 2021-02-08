[n, m] = map(int, input().split())

rules = dict()
for i in range(0, n):
    curr = input().split(' -> ')
    rules[curr[0]] = curr[1]

seq = input()
for i in range(0, m):
    new_seq = ''
    for j in range(0, len(seq)):
        new_seq += rules[seq[j]] if (seq[j] in rules) else seq[j]
    seq = new_seq

print(seq)
