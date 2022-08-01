from collections import defaultdict

def main():
    letters = defaultdict(int)
    for l in input():
        letters[l] += 1

    removed = 0
    while True:
        if len(letters) <= 2:
            break
        min_letter = min(letters, key=lambda l:letters[l])
        removed += letters[min_letter]
        letters.pop(min_letter)
    print(removed)

if __name__ == '__main__':
    main()
