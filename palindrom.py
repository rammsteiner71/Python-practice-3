def palindrome(text):
    tail = -1
    head = 0
    checkr = len(text) // 2
    while head != checkr:
        if text[head] == ' ':
            checkr += 1
            head+=1
        if text[tail] == ' ':
            checkr -= 1
            tail-=1
        if text[head] != ' ' and text[tail] != ' ':
            if text[head].upper() != text[tail].upper():
                return "Не палиндром"
        tail -= 1
        head += 1
    return "Палиндром"