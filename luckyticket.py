def do_bet(number, bet):
    global bets
    if bet == 0 or number in bets or number>10 or number<1:
        print("Что-то пошло не так, попробуйте еще раз")
    else:
        print("Ваша ставка в размере " + str(bet) + " на лошадь " + str(number) + " принята")
        bets.append(number)


bets = []
do_bet(1, 10)
do_bet(1, 100)
do_bet(2, 0)
do_bet(2, 200)