import random


def score(name, number=-1):
    if number == -1:
        return scoring[name]
    else:
        return scoring[name][number]


scoring = {"Яблочко": 50, "Зеленое_кольцо": 25, "Внешнее_кольцо": {i + 1: random.randint(1, 60) for i in range(20)},
           "Внутреннее_кольцо": {i + 1: random.randint(1, 60) for i in range(20)}}
print("Значения для глобальной переменной scoring имеют случайные значения,\nдля данного запуска программы "
      "значения выглядят так :")
print("Яблочко\n" + str(scoring["Яблочко"]))
print("Зеленое_кольцо\n" + str(scoring["Зеленое_кольцо"]))
print("Внешнее_кольцо")
printerTemp = ''
for i in range(20):
    printerTemp += str(scoring["Внешнее_кольцо"][i+1]) + ' '
print(printerTemp)
print("Внутреннее_кольцо")
printerTemp = ''
for i in range(20):
    printerTemp += str(scoring["Внутреннее_кольцо"][i+1]) + ' '
print(printerTemp)


print(score("Внешнее_кольцо", 1))
print(score("Внутреннее_кольцо",1))