print('YES'if(lambda a,b,c,n:all([a,b,c,n>2,a+b+c>=n]))(*map(int,input().split()))else'NO')
