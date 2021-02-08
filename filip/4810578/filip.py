[a,b] = map(int, input().split())

def flip_int(x):
    x_new = 0
    p = 2
    while(p >= 0):
        x_new += (x % 10) * pow(10, p)
        x = int(x / 10)
        p -= 1

    return x_new

a = flip_int(a)
b = flip_int(b)

print(a if a > b else b)
