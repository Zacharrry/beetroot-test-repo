import random

random_list = []
index = 0

while index < 10:
    random_list.append(random.randrange(1,100))
    index += 1
index = 0
largest_number_in_list = 0
while index < 10:
    if random_list[index] > largest_number_in_list:
        largest_number_in_list = random_list[index]
    index += 1

print(f"\nОтриманий список: {random_list}")
print(f"Максимальне значення якого є: {largest_number_in_list}")
print()