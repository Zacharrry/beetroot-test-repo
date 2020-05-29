import random


random_list1 = []
random_list2 = []

index = 0
while index < 10:
    random_list1.append(random.randrange(1,100))
    random_list2.append(random.randrange(1,100))
    index += 1

common_integers = []
index = 0
while index < 10:
    if random_list1[index] in random_list2:
        common_integers.append(random_list1[index])
    index += 1


print(f'\nСписок 1: {random_list1}')
print(f'Список 2: {random_list2}')

print(f'\nЗнайдені спільні числа: {common_integers}')