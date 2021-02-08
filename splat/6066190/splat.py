from math import pi

class Circle:
    def __init__(self, x, y, v, color):
        self.x = x
        self.y = y
        self.v = v
        self.color = color

c = int(input())

for _ in range(c):
    n = int(input())
    circles = []

    for _ in range(n):
        x, y, v, color = input().split()
        circles.append(Circle(float(x), float(y), float(v), color))
    
    m = int(input())
    for _ in range(m):
        splat_color = 'white'
        x, y = map(float, input().split())
        for circle in circles:
            if circle.v >= pi * ((x - circle.x)**2 + (y - circle.y)**2):
                splat_color = circle.color
        print(splat_color)