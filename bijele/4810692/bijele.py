real = [1,1,2,2,2,8]
have = list(map(int, input().split()))
need = ''
for i in range(0,len(real)):
    need += str(real[i] - have[i]) + ' '
print(need)
