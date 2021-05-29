def ask_password():
    for i in range(3):
        passwrd = input()
        if passwrd == "password":
            print("Пароль принят")
            return
    print("В доступе отказано")


ask_password()