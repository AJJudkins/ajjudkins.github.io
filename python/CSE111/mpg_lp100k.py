def main():
    starting_millage = float(
        input("What was your starting millage on your odometer? \n"))
    end_millage = float(
        input("What was your finishing millage on your odometer? \n"))
    gallons_used = float(input("How many gallons did you use? \n"))

    mpg = miles_per_gallon(starting_millage, end_millage, gallons_used)

    lp100k = liters_per_100k(mpg)

    print(f"You got {mpg: .1f} miles per gallon.")
    print(f"You got {lp100k: .2f} per 100 kilometers.")
    pass


def miles_per_gallon(start, end, gallons):
    miles = end - start
    mpg = miles / gallons
    return mpg


def liters_per_100k(mpg):
    lp100k = 235.215 / mpg
    return lp100k


main()
