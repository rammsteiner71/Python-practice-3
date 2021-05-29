import math


def solve(*coefficients):
    if len(coefficients) > 3 or len(coefficients) == 0:
        return None
    elif len(coefficients) == 3:
        return roots_of_quadratic_equation(coefficients[0], coefficients[1], coefficients[2])
    elif len(coefficients) == 2:
        return roots_of_quadratic_equation(b=coefficients[0], c=coefficients[1])
    elif len(coefficients) == 1:
        return roots_of_quadratic_equation(c=coefficients[0])


def roots_of_quadratic_equation(a=0, b=0, c=0):
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


print("Введите коэффициенты уравнения")
coeffs = input().split()
for i in range(len(coeffs)):
    coeffs[i] = int(coeffs[i])
print(solve(*coeffs))