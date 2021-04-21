import sys

def win(player):
    if player != 'Tie':
        print(f'Player {player} wins.')
    else:
        print(f'Tie.')

for dice in sys.stdin:
    dice = list(map(int, dice.rstrip().split()))
    if dice == [0,0,0,0]:
        break
    # i know....
    a = int(''.join(map(str,(lambda a,b:[max(a,b),min(a,b)])(*dice[:2]))))
    b = int(''.join(map(str,(lambda a,b:[max(a,b),min(a,b)])(*dice[2:]))))

    if a == b:
        win('Tie')
    elif a == 21:
        win(1)
    elif b == 21:
        win(2)
    elif a % 11 == 0:
        if b % 11 == 0:
            win(1 if a > b else 2)
        else:
            win(1)
    elif b % 11 == 0:
        win(2)
    elif a > b:
        win(1)
    elif b > a:
        win(2)
