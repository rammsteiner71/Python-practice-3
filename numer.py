def sum_gema(word):
    summ = 0
    for i in word:
        i = i.upper()
        summ += ord(i) - ord('A') + 1
    return summ


print("Для остановки ввода введите пустую строку")
words = []
temp = ' '
while True:
    temp = input()
    if temp == '':
        break
    words.append((temp, sum_gema(temp)))
words.sort()
for i in words:
    print(i[0])