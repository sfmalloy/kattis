def fact(n):
    if n < 2:
        return 1
    return n * fact(n - 1)

def nCr(n, r):
    return fact(n) / (fact(r) * fact(n - r))

def bin_prob(n, x, p, q):
    return nCr(n, x) * (p**x) * (q**(n-x))

def get_total_prob(x, y, win):
    loss = 1 - win
    total = 0
    for t in range(x, y+1):
        total += bin_prob(y, t, win, loss)
    return total

def main():

    '''
    r -> cannot obtain a value >= r
    s -> number of sides on die
    x -> min rolls
    y -> total rolls
    w -> pay w times Bobby's bet
    '''

    for _ in range(int(input())):
        r,s,x,y,w = map(int, input().split())
        prob_single_win = (s-r+1) / s
        # print(prob_single_win)
        prob_total = get_total_prob(x, y, prob_single_win)
        print('yes' if prob_total * w > 1 else 'no')

if __name__ == '__main__':
    main()