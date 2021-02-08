n = input()
per = 'per'
BIGPER = 'PER'
wrong = 0
for i in range(len(n)):
    if (n[i] != per[i % 3] and n[i] != BIGPER[i % 3]):
        wrong += 1

print(wrong)
