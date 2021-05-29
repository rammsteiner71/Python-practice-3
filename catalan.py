vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')


def translate(text):
    global translatedText
    for i in text:
        if not i.lower() in vowels:
            if len(translatedText) == 0:
                translatedText += i
            else:
                if not (translatedText[-1] == ' ' and i == ' '):
                    translatedText += i


translatedText = ''
translate(
    "Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. "
    "Достаточно небольшой тренировки - и вы сможете это делать.")
print(translatedText)