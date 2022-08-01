g,t,n = map(int, input().split())
towcap = .9 * (g - t)
items = sum(list(map(int, input().split())))
print(int(towcap - items))
