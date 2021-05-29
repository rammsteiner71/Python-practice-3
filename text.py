nameGlbl = ''
date = ''


def setup_profile(name, vacationDates):
    global nameGlbl, date
    nameGlbl = name
    date = vacationDates


def print_application_for_leave():
    print("Заявление на отпуск в период " + date + ". " + nameGlbl, sep='')


def print_holiday_money_claim(amount):
    print("Прошу выплатить " + amount + " отпускных денег. " + nameGlbl, sep='')


def print_attorney_letter(toWhom):
    print("На время отпуска в период " + date + " моим заместителем назначается " + toWhom + ". " + nameGlbl, sep='')


setup_profile("Иван Петров", "1 июня – 20 июня")
print_application_for_leave()
print_application_for_leave()
print_holiday_money_claim("15 тысяч пиастров")
print_attorney_letter("Василий Васильев")