from sys import stdin

score = correct = 0
wrong_counts = {}
line = input()
while line != '-1':
    time, prob, is_correct = line.split()
    time = int(time)

    if is_correct == 'wrong':
        if prob in wrong_counts:
            wrong_counts[prob] += 1
        else:
            wrong_counts[prob] = 1
    else:
        score += time
        if prob in wrong_counts:
            score += 20 * wrong_counts[prob]
        correct += 1

    line = input()

print(f'{correct} {score}')