def catalan(n):
    answer = factor(2 * n) / (factor(n) * factor(n + 1))
    return answer


def factor(numb):
    answer = 1
    while numb != 0:
        answer *= numb
        numb -= 1
    return answer


for i in range(20):
    print(catalan(i))