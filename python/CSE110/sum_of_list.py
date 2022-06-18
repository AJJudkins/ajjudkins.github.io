print("Enter a list of numbers, type 0 when finished.")
print()
numbers = []
sum_of_numbers = 0


def sum(sum_of_numbers):
    for number in numbers:
        sum_of_numbers += number
    return sum_of_numbers


while number != 0:
    number = float(input("Enter a number: \n"))
    if number != 0:
        numbers.append(number)


sum_of = sum(sum_of_numbers)
print(f"The sum is {sum_of}")

count = len(numbers)
average = sum / count

print(f"The average is: {average}")
