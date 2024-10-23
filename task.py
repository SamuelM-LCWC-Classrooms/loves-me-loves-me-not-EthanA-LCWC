def loves_me(number):
    yes_or_no = 1
    love_or_not = ""
    for i in range(1, number + 1):
        if yes_or_no == 1:
            answer = "Loves me"
            yes_or_no = 0
        elif yes_or_no == 0:
            answer = "Loves me not"
            yes_or_no = 1
        if i == number:
            answer = answer.upper()
        else:
            answer += ", "
        love_or_not += answer
    return str(love_or_not)
