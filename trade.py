def defractalize(fractal):
    popList = []
    for i in range(len(fractal)):
        if fractal[i] == fractal:
            popList.append(i)
    for i in popList:
        fractal.pop(i)


fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
defractalize(fractal)
print(fractal)