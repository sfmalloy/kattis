a = input()
b = input()
x = 1
for aa,bb in zip(a,b):
    if aa!=bb:
        x *= 2
print(x)
