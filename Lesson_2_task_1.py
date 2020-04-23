name = "Yaroslav"
day = "Everyday"

message = 'Good day {}! {} is a perfect day to learn some Python.'
print(message.format(name, day))

# Another example text formatting

print(f'Good day {name}! {day} is a perfect day to learn some Python.')
print()

#
# Maybe correct way must include name day of the week.
# Also variable 'name' may gets from user input.
#

today = date.today()

name = input("What's your name please? ")

print(f'Good day {name.capitalize()}! {today.strftime("%A")} is a perfect day to learn some Python')