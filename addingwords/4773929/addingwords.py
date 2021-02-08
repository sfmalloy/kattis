import sys

numbers = dict()
for line in sys.stdin:
    args = line.split()
    
    if (args[0] == 'def'):
        numbers[args[1]] = int(args[2])
    elif (args[0] == 'calc'):
        total = 0
        curr_number = 0
        curr_op = ''
        valid = True
        for arg in args:
            if (arg not in ['+', '-', '=', 'calc']):
                if (arg not in numbers):
                    valid = False
                    break
                curr_number = numbers[arg]
            
            if (arg == '+' or arg == '-'):
                curr_op = arg
            elif (arg != 'calc' and arg != '='):
                if (curr_op == '-'):
                    curr_number *= -1
                total += curr_number
        
        answer = 'unknown'
        if (valid):
            for key in numbers:
                if (numbers[key] == total):
                    answer = key
                    break
        print(line[5:-1], answer)
    elif (args[0] == 'clear'):
        numbers = dict()
