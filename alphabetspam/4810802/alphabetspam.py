alpha = input()
upper = 0
lower = 0
symbols = 0
whitespace = 0
for c in alpha:
    if (c.isupper()):
        upper += 1
    elif (c.islower()):
        lower += 1
    elif (c == '_'):
        whitespace += 1
    else:
        symbols += 1
l = len(alpha)
print(whitespace / l)
print(lower / l)
print(upper / l)
print(symbols / l)
