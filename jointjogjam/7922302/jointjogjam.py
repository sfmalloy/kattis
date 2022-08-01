def dist(x1, y1, x2, y2):
    return ((y2-y1)**2 + (x2-x1)**2)**0.5

def main():
    kx1, ky1, ox1, oy1, kx2, ky2, ox2, oy2 = map(int, input().split())
    print(max(dist(kx1, ky1, ox1, oy1), dist(kx2, ky2, ox2, oy2)))

if __name__ == '__main__':
    main()
