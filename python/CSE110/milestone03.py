kids = float(input("What is the current price of a child's meal?"))
adult = float(input("What is the current price of an adult's meal"))
numKids = input('How many kids are there?')
numAdults = input('How many adults are there?')
children = int(numKids)
adults = int(numAdults)
taxRate = float(input('What is the current sales tax rate where you live?'))
subTotal = (children * kids) + (adults * adult)
salesTax = (subTotal * taxRate / 100)
total = (subTotal + salesTax)

print(f'Subtotal: ${subTotal: .2f}')
print()
print(f'Sales Tax: ${salesTax: .2f}')
print()

tip = input('Would you like to add a 15% tip? (Y/N): ')
if tip == "Y":
    grandTotal = (subTotal + salesTax) + (total * .15)
elif tip == "N":
    grandTotal = (subTotal + salesTax)

print(f'Total: ${grandTotal: .2f}')

pay = float(input('What is the payment amount?'))
change = (pay - total)
print()
print(f'Change: ${change: .2f}')
