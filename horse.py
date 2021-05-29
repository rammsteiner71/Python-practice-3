import math


def roots_of_quadratic_equation(a, b, c):
    answer = []
    if a == b == c == 0:
        answer.append('all')
    elif a == b == 0 and c != 0:
        answer.append('none')
    elif a == 0 and b != 0:
        x = -c / b
        answer.append(x)
    elif a != 0:
        x1 = (-b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
        x2 = (-b - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
        if x1 != x2:
            answer.append(x1)
        answer.append(x2)
    return answer


result = roots_of_quadratic_equation(1, -3, 2)
print(*result)