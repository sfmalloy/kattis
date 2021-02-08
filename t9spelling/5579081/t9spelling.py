import string
N = int(input())

letters_per_number = [3,3,3,3,3,4,3,4]
letters = string.ascii_lowercase
t9_map = {' ' : '0'}

l = 0
for i in range(2, 10):
    num_str = ''
    for j in range(letters_per_number[i - 2]):
        num_str += str(i)
        t9_map[letters[l]] = num_str
        l += 1

for i in range(N):
    msg = input()
    ret = ''
    for c in msg:
        if len(ret) > 0 and t9_map[c][0] == ret[-1]:
            ret += ' '

        ret += t9_map[c]
        

    print(f'Case #{i + 1}: {ret}')
    