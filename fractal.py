
def fractal_print(fractal):
    fractalId = 0
    for i in range(len(fractal)):
        if fractal[i] == fractal:
            fractalId = i
    fractalForPrint = fractal[:]
    fractalForPrint[fractalId] = fractal
    print(fractalForPrint)


fractal = [3]
fractal.append(fractal)
fractal.append(2)
fractal_print(fractal)