triple = input()
word_len = len(triple) // 3
words = set()

for i in range(0, len(triple), word_len):
	word = triple[i:word_len + i]
	if word in words:
		print(word)
		break
	words.add(word)
