def take_input():
    ipt = input()
    _, lst = ipt.split(': ') if len(ipt) > 0 else None
    lst = lst.split(',')
    return lst

white = take_input()
black = take_input()

board = [[':::' if (r+c)%2==1 else '...' for c in range(8)] for r in range(8)]

def ltoi(l):
    return ord(l) - 97

def place_pieces(pieces, color):
    p,c,r = '','',''
    for piece in pieces:
        if len(piece) > 2:
            p,c,r = map(str, piece)
        elif len(piece) > 0:
            p = 'P'
            c,r = map(str,piece)
        else:
            break
        letter = p if color == 'white' else p.lower()
        old = board[8-int(r)][ltoi(c)]
        board[8-int(r)][ltoi(c)] = f'{old[0]}{letter}{old[0]}'

place_pieces(white, 'white')
place_pieces(black, 'black')

def print_banner():
    print('+---+---+---+---+---+---+---+---+')

print_banner()
for r in board:
    for c in r:
        print(f'|{c}',end='')
    print('|')
    print_banner()

