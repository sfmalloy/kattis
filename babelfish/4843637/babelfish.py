import sys

words = dict()
line = input()
while (line != ''):
    line = line.split()
    words[line[1]] = line[0]
    line = input()

for word in sys.stdin:
    print(words[word[:-1]] if (word[:-1] in words) else 'eh')
