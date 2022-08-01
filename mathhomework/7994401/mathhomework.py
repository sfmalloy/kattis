def main():
    b,d,c,l = map(int, input().split())
    bl = 0
    found = False
    while bl <= l:
        dl = 0
        while bl+dl <= l:
            cl = 0
            while bl+dl+cl <= l:
                if bl+dl+cl == l:
                    print(bl//b,dl//d,cl//c)
                    found = True
                cl += c
            dl += d
        bl += b
    if not found:
        print('impossible')
    
if __name__ == '__main__':
    main()
