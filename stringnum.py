import copy


def transpose(matrixx):
    tempMatrix = copy.deepcopy(matrixx)
    height = len(tempMatrix)
    width = len(tempMatrix[0])
    x = 0
    if height > width:
        for i in range(height):
            for j in range(height - width):
                matrixx[i].append(-9999)
        x = height
    elif height < width:
        for i in range(height):
            for j in range(width - height):
                matrixx[i].append(-9999)
        x = width
    for i in range(height):
        for j in range(width):
            matrixx[i][j] = -9999
    for i in range(height):
        for j in range(width):
            matrixx[j][i] = tempMatrix[i][j]
    for i in range(x):
        for j in range(x, 0, -1):
            if matrixx[i][j - 1] == -9999:
                matrixx[i].pop(-1)


matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)