print("This program checks to see if a specific year is in fact a leap year. (Has an extra day in February)")

year = int(input("which year do you want to check?"))
by_four = year % 4
by_hundred = year % 100
by_four_hundred = year % 400

if by_four == 0:
    leap = True
    if by_hundred == 0:
        leap = False
        if by_four_hundred == 0:
            leap = True
        else:
            leap = False
    else:
        leap = True
else:
    leap = False

if leap == True:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
