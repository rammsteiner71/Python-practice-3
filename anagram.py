import random


def generate_password(num):
    used = ['0', 'o', 'O', '1', 'I', 'l']
    answer = ''
    while len(answer) != num:
        tempRand = random.randint(48, 122)
        sign = chr(tempRand)
        if sign not in used and not (65 > tempRand > 57 or 97 > tempRand > 90):
            used.append(sign)
            answer += sign
    return answer


def main(amount, num):
    answer = []
    for i in range(amount):
        answer.append(generate_password(num))
    return answer


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")