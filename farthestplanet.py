text = input().split()
vowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
is_ok = True
amount_of_vowels_old = -1
for i in text:
    amount_of_vowels = len(list(filter(lambda x: x in vowels, i)))
    if amount_of_vowels != amount_of_vowels_old and amount_of_vowels_old != -1:
        is_ok = False
        break
    amount_of_vowels_old = amount_of_vowels
if is_ok:
    print("Парам пам-пам")
else:
    print("Пам парам")