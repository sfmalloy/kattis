index_str = ""
for i in range(0, 5):
    s = input()
    if ("FBI" in s):
        index_str += str(i + 1) + ' '

if (len(index_str) == 0):
    print("HE GOT AWAY!")
else:
    print(index_str)
