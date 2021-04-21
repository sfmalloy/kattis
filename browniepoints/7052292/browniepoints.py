n = int(input())

def calc_brownie(mx,my,points):
    stan = ollie = 0
    for x,y in points:
        if (x < mx and y < my) or (x > mx and y > my):
            stan += 1
        elif (x > mx and y < my) or (x < mx and y > my):
            ollie += 1
    return stan, ollie


while n != 0:
    points = []
    X = set()
    Y = set()
    x_mid = y_mid = 0
    for _ in range(n):
        x, y = map(int, input().split())
        X.add(x)
        Y.add(y)
        points.append((x,y))
    mid_x, mid_y = points[n//2]
    stan, ollie = calc_brownie(mid_x, mid_y, points)
    # stan = 0
    # ollie = 0
    # for x,y in points:
    #     if x == mid_x:
    #         s, o = calc_brownie(x,y,points)
    #         if o > ollie:
    #             stan = s
    #             ollie = o
    print(stan, ollie)
        
    n = int(input())