print('YES'if (lambda a,b,c,n:all([a>0,b>0,c>0,n>2])and a+b+c>=n)(*map(int,input().split()))else'NO')
