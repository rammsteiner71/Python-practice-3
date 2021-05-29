def prime(numb):
    for i in range(numb-2):
        if numb % (i+2) == 0:
            return "Составное число"
    return "Простое число"