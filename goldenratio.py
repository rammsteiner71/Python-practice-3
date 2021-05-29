def golden_ratio(i):
    first = 1
    second = 1
    for j in range(i-1):
        temp = second
        second += first
        first = temp
    print(second/first)


golden_ratio(1)
golden_ratio(2)
golden_ratio(4)