n,m = map(int, input().split())
a = input()
b = input()

def to_num(letter):
    return ord(letter) - 97

def to_letter(num):
    return chr(num + 97)

num_a = [to_num(l) for l in a]
num_b = [to_num(l) for l in b]

plaintext = ''

for i in range(m - n):
    k = (num_b[m - i - 1] - num_a[-1]) % 26
    num_a.pop()
    num_a.insert(0, k)
    plaintext = to_letter(k) + plaintext

print(plaintext + a)
