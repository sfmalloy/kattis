line = input()

while (line != '0'):
    x1,y1,x2,y2,p = map(float, line.split())
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    dist = ((dy**p) + (dx**p))**(1/p)

    print(dist)

    line = input()
