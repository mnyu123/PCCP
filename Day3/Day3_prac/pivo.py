def pivo(num):
    if (num == 0):
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return pivo(num-1) + pivo(num-2)


print(pivo(3))