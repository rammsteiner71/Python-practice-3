def lucky(ticket):
    global lastTicket
    ticket = str(ticket)
    lastTicket = str(lastTicket)
    if len(lastTicket) < 6:
        lastTicket = " " * (len(lastTicket) - 6) + lastTicket
    if len(ticket) < 6:
        ticket = " " * (len(ticket) - 6) + ticket
    if (int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3]) + int(ticket[4]) + int(ticket[5])) and (
            int(lastTicket[0]) + int(lastTicket[1]) + int(lastTicket[2]) == int(lastTicket[3]) + int(
            lastTicket[4]) + int(lastTicket[5])):
        return "Счастливый"
    return "Несчастливый"


lastTicket = 123321
print(lucky(100001))