N = int(input())

for i in range(N):
    alien_input, source, target = input().split()

    source_num = 0
    magnitude = 1
    for a in reversed(alien_input):
        source_num += source.index(a) * magnitude
        magnitude *= len(source)

    target_base = len(target)
    target_num = []
    while source_num > 0:
        target_num.append(target[source_num % target_base])
        source_num //= target_base
    print(f'Case #{i+1}: {"".join(reversed(target_num))}')
