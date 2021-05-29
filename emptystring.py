print("Введите пустую строку для того чтобы прекратить ввод")
line = ' '
text = []
while True:
    line = input()
    if line == '':
        break
    text.append(line)
answer = []
for i in range(len(text)):
    isFirst = True
    wasSign = False
    answertmp = ''
    for j in text[i]:
        if isFirst and j != ' ' and j != '#':
            isFirst = False
        elif isFirst and j == '#':
            wasSign = True
            isFirst = False
            pass
        elif wasSign:
            answertmp += j
    if answertmp != '':
        answer.append("Line " + str(i + 1) + ":" + answertmp)
print(*answer, sep='\n')