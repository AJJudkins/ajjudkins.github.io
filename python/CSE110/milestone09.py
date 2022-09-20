print("Welcome to the Shopping Cart Program!")
list_of_items = []
list_of_prices = []
total = 0
cont = True

while cont:

    print("Please select one of the following:")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Compute Total")
    print("5. Quit Program")
    choice = int(input("What is your choice? \n"))
    list_number = 0

    if choice == 1:
        item = input("What item would you like to add? \n")
        list_of_items.append(item)
        price = float(input("What is the price of the item? \n"))
        list_of_prices.append(price)
        print(f"{item} has been added to the cart.")
        print()

    elif choice == 2:

        print("The contents of your shopping cart are: ")

        for item, price in zip(list_of_items, list_of_prices):
            list_number += 1
            print(f"{list_number}. {item} - ${price:.2f}")

    elif choice == 3:
        removal = int(input("Which item would you like to remove?"))

        if removal <= len(list_of_items):
            list_of_items.pop(removal - 1)
            list_of_prices.pop(removal - 1)
            print("Item was removed.")
        else:
            print("Sorry, that is not a valid item number.")

    elif choice == 4:
        for price in list_of_prices:
            total += price
        print(f"Your total is ${total: .2f}")

    else:
        cont = False

print("Thank you for shopping with us!")
