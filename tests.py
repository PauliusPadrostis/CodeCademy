x = 0
while True:
    x += 1

    while x < 20:
        if x > 0:
            x += 1
        elif x > 10:
            x += 2
        else:
            x += 3

    x += 20
    break
