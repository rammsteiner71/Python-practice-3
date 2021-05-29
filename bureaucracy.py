def print_only_new(text):
    global messages
    number = int(text.split()[-1])
    if number not in messages:
        messages.append(number)
        print(text)


messages = []
print_only_new("Шутка номер 15")
print_only_new("Шутка номер 23")
print_only_new("Шутка номер 23")
print_only_new("Шутка номер 24")
print_only_new("Шутка номер 100")
print_only_new("Шутка номер 24")
print_only_new("Шутка номер 99")
print_only_new("Шутка номер 15")
print_only_new("Шутка номер 100")