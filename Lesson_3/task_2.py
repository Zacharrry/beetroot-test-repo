phone_number = input('Please enter your phone number.' +\
'\nPhone number must be 10 digits: ')

if phone_number.isdigit() is not True:
    print("\nPhone number must be only digits character.")
elif len(phone_number) != 10:
    print("\nPhone number must contain 10 digits")
else:
    print(f'\nPhone number correct: {phone_number}')
