print('Please enter the following information:')

print()

firstName = input('First Name:')
lastName = input('Last Name:')
email = input('E-mail Address:')
phone = input('Phone Number:')
title = input('Job Title:')
id = input('ID Number:')
hair = input('Hair Color:')
age = input('Age:')
month = input('Month You Started Working Here:')
train = input('Completion of Advanced Training:')

print()

print('The ID card is:')
print('------------------------------------------')

print(f"{lastName.upper()}, {firstName.capitalize()}")
print(title.title())
print(f"ID: {id}")

print()

print(email.lower())
print(phone)

print()

print(f"Hair: {hair} Age: {age}")
print(f"Month: {month} Training: {train}")

print('------------------------------------------')
