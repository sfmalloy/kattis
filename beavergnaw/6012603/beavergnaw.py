from math import pi

D,V = map(int, input().split())

while D != 0 and V != 0:
    V_D = (pi/4) * D**3
    dV = V_D - V

    d = ((6/pi)*dV - (1/2)*D**3)**(1/3)

    print(d)
    
    D,V = map(int, input().split())
