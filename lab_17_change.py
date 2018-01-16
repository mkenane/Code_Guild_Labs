

def changeDispense(n):

    quartersPossible = n // 25
    dimesPossible = (n % 25) // 10
    nicklesPossible = ((n % 25) % 10 ) // 5
    penniesPossible = ((n % 25) % 10 ) % 5

    changeToDispense = {'Quarters:': quartersPossible, 'Dimes:': dimesPossible, 'Nickles:': nicklesPossible, 'Pennies:': penniesPossible}

    return changeToDispense

print(changeDispense(86))
