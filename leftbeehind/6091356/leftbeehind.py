# if sweet + sour == 13: 'Never speak again.'
# if sour > sweet: 'Left beehind.'
# if sweet > sour: 'To the convention.'
# if sweet == sour: 'Undecided.'

sweet, sour = map(int, input().split())
while not (sweet == 0 and sour == 0):
    if sweet + sour == 13:
        print('Never speak again.')
    elif sour > sweet:
        print('Left beehind.')
    elif sweet > sour:
        print('To the convention.')
    else:
        print('Undecided.')
    sweet, sour = map(int, input().split())
