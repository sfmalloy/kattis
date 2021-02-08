old = input()
new = ''
for c in old:
    if (not new.endswith(c)):
        new += c

print(new)
