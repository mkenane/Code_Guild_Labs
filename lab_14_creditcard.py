
userCardNumber = input('please enter the 16 digits on your credit card (no spaces or dashes: ')

def cardValidCheck(number):

    numberTurnedToList = list(number)
    checkNumber = numberTurnedToList.pop()
    print(checkNumber)
    numberTurnedToList.reverse()

    listTurnedInteger = [int(n) for n in numberTurnedToList[1::2]]
    multipliedDigits = [int(i) * 2 for i in numberTurnedToList[::2]]
    subtractedDigits = [x - 9 if x > 9 else x + 0 for x in multipliedDigits]
    secondDigit = str(sum(subtractedDigits) + sum(listTurnedInteger))[1]

    if secondDigit == checkNumber:
        return "This is a valid credit card"
    else:
        return "Not a valid credit card"

print(cardValidCheck("4556737586899855"))
