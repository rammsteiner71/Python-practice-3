def bracket_check(check):
    numbers = 0
    for i in check:
        if i == "(":
            numbers += 1
        elif i == ")" and numbers==0:
            numbers -= 1
            break
        elif i == ")":
            numbers -=1
    if numbers == 0:
        print("YES")
    else:
        print("NO")