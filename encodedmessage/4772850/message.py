from math import sqrt

def message_matrix(message):
    size = int(sqrt(len(message)))
    matrix = []
    index = 0

    for i in range(0, size):
        row = message[i * size:(i + 1) * size]
        matrix.append(row)

    return matrix

n = int(input())

for i in range(0, n):
    message = input()
    matrix = message_matrix(message)

    j = len(matrix) - 1
    new_message = ''
    while (j >= 0):
        for k in range(0, len(matrix)):
            new_message += matrix[k][j]
        
        j -= 1

    print(new_message)

