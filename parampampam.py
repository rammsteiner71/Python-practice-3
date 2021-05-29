import math


def new_point(pi):
    x = R * (math.cos(pi) ** 3)
    y = R * (math.sin(pi) ** 3)
    length = math.sqrt((x_const - x) ** 2 + (y_const - y) ** 2)
    return round(length, 6), x, y


R = 1
x_const = 0.75
y_const = 0
i = 0
answer = 111, 0, 0
while i <= 44:
    t = i / 7
    tmp = new_point(t)
    if tmp[0] < answer[0]:
        answer = tmp
    i += 0.0001
print(answer[0])