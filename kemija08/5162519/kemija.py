secret = input()
vowels = 'aeiou'

read_next = 0
sentence = ''
for c in secret:
    if (read_next == 0):
        if (c in vowels):
            read_next = 1
        sentence += c
    elif (read_next == 1):
        read_next = 2
    else:
        read_next = 0

print(sentence)
