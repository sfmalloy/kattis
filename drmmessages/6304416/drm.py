
def value(word):
  val = 0
  for w in word:
    val += ord(w) - 65
  return val % 26

def rotate(letter, steps):
  if ord(letter) + steps > ord('Z'):
    return chr(ord(letter) + steps - 26)
  return chr(ord(letter) + steps)

def rotate_word(word, steps):
  new = ''
  for w in word:
    new += rotate(w, steps)
  return new

word = input()
first = word[:len(word) // 2]
last = word[len(word) // 2:]

new_first = rotate_word(first, value(first))
new_last = rotate_word(last, value(last))

final = ''
for a, b in zip(new_first, new_last):
  final += rotate(a, value(b))

print(final)