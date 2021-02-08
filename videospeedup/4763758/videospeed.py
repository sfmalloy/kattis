[n,p,k] = map(int, input().split())
t = list(map(int, input().split()))
t.append(k)

T = t[0]
speed = 100 + p

for i in range (1, n + 1):
    dt = t[i] - t[i - 1]
    T += dt * (speed / 100)
    speed += p

print(T)
