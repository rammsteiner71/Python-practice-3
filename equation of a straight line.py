def line(s, t):
    if float(t.split(';')[1]) == float(s.split('x')[0]) * float(t.split(';')[0]) + float(s.split('x')[1]):
        print(True)
    else:
        print(False)