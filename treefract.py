def encrypt_caesar(msg_to_crypt, shift_crypt=3):
    answer = ''
    for i in msg_to_crypt:
        if 1072 > ord(i.upper()) > 1039:
            char = ord(i.upper()) + shift_crypt
            while not (1072 > char > 1039):
                tmpShift = char - 1071
                char = 1039
                char += tmpShift
            if i.isupper():
                answer += chr(char)
            else:
                answer += chr(char).lower()
        else:
            answer += i
    return answer


def decrypt_caesar(msg_crypted, shift_decrypt=3):
    answer = ''
    for i in msg_crypted:
        if 1072 > ord(i.upper()) > 1039:
            char = ord(i.upper()) - shift_decrypt
            while not (1072 > char > 1039):
                tmpShift = 1040 - char
                char = 1072
                char -= tmpShift
            if i.isupper():
                answer += chr(char)
            else:
                answer += chr(char).lower()
        else:
            answer += i
    return answer


msg = 'Да здравствует салат Цезарь!'
shift = 5
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)