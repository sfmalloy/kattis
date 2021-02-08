N = int(input())
scores = [int(input()) for _ in range(N)]

avg = 0
for i in range(N):
    four = five = 1.0
    s = 0
    popped = scores.pop(i)
    for j in range(N - 1):
        s += (four / five) * scores[j]
        four *= 4
        five *= 5
    avg += s / 5
    scores.insert(i, popped)
avg /= N

four = five = 1.0
s = 0
for i in range(N):
    s += scores[i] * (four / five)
    four *= 4
    five *= 5

print(s / 5)
print(avg)