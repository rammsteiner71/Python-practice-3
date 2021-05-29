def swap(firstElem, secondElem):
    tempFirst = firstElem[:]
    tempSecond = secondElem[:]
    change(firstElem, tempSecond)
    change(secondElem, tempFirst)


def change(array, tempArr):
    for i in range(len(tempArr)):
        array[i] = tempArr[i]
    while len(array) != len(tempArr):
        array.pop(-1)


first = [1, 2, 3]
second = [4, 5, 6]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)