print("This program will tell you how many years, months, weeks, \
 and days you have left (if you were to live until 90 years old)")
age = int(input('How old are you? \n'))
years_left = 90 - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
print(f"You have {years_left} years, ", end="")
print(f"{months_left} months, ", end="")
print(f"{weeks_left} weeks, ", end="")
print(f"and {days_left} days left in your life")
