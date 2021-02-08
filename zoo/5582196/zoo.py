from operator import itemgetter

N = int(input())
lst = 1
while N != 0:
    animals = {}
    for _ in range(N):
        animal = input().split()[-1].lower()
        if animal in animals:
            animals[animal] += 1
        else:
            animals[animal] = 1
    
    print(f'List {lst}:')
    for animal, count in sorted(animals.items(), key=itemgetter(0)):
        print(f'{animal} | {count}')
    lst += 1
    
    N = int(input())