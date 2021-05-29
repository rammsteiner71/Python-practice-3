def ord_sum(word):
    answer = 0
    for i in word:
        answer += ord(i)
    return answer


amount = int(input())
words = []
for i in range(amount):
    temp = input()
    temp = temp.lower()
    if temp not in words:
        words.append(temp)
answer = []
already_in_use=[]
for i in words:
    temp = [i]
    if ord_sum(i) not in already_in_use:
        already_in_use.append(ord_sum(i))
        for j in words:
            if i != j and len(i) == len(j) and ord_sum(i) == ord_sum(j):
                temp.append(j)
        if len(temp) > 1:
            if temp not in answer:
                answer.append(sorted(temp))
for i in sorted(answer):
    print(*i)