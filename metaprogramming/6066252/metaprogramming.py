import sys

nums = {}
for line in sys.stdin.readlines():
    tokens = line.strip().split()

    if tokens[0] == 'define':
        nums[tokens[2]] = int(tokens[1])
    else:
        if tokens[1] not in nums or tokens[3] not in nums:
            print('undefined')
        else:
            a = nums[tokens[1]]
            b = nums[tokens[3]]

            if tokens[2] == '<':
                print('true' if a < b else 'false')
            elif tokens[2] == '=':
                print('true' if a == b else 'false')
            else:
                print('true' if a > b else 'false')
            