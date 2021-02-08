for _ in range(int(input())):
    K, N = map(int, input().split())
    print(f'{K} {sum(i for i in range(N+1)) + N}')
