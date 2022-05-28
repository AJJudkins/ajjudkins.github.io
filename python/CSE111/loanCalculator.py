print('Please rate the following questions between 1-10 (1 being the lowest and 10 the highest):')
loan = float(input('How large is the loan? '))
credit = float(input('How good is your credit history? '))
income = float(input('How good is your income? '))
down = float(input('How large is your down payment? '))

if loan >= 5:
    if loan >= 7 and credit >= 7:
        print('Yes')
    elif (credit >= 7 or income >= 7) and down >= 5:
        print('Yes')
    else:
        print('No')
elif loan < 5:
    if credit <= 4:
        print('No')
