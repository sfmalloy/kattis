key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
size = len(key)
rot = 1

while (rot != 0):
    i = input()
    if (i != '0'):
        [rot,s] = i.split()
        rot = int(rot)
        new_s = ''
        for c in s:
            char_index = 0
            if (c == '_'):
                char_index = 26
            elif (c == '.'):
                char_index = 27
            else:
                char_index = ord(c) - 65

            new_s = key[(char_index + rot) % size] + new_s
        print(new_s)
    else:
        rot = 0
