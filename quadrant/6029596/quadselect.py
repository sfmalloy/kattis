print((lambda x, y: (1 if x * y > 0 else 2) + (2 if (x < 0 and y < 0) or (x > 0 and y < 0) else 0))(int(input()), int(input())))
