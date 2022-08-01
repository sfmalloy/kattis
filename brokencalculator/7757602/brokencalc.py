
def main():
    prev_res = 1
    for _ in range(int(input())):
        a,op,b = input().split()
        a = int(a)
        b = int(b)
        if op == '+':
            prev_res = (a + b) - prev_res
        elif op == '-':
            prev_res = prev_res * (a - b)
        elif op == '*':
            prev_res = (a * b) ** 2
        else:
            prev_res = (a + a%2) // 2
        print(prev_res)

if __name__ == '__main__':
    main()    