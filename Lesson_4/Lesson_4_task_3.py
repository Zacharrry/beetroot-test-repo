integers_from_1_to_100 = list(range(1,101,1))

divisible_by_7 = []
index = 0
while index < 100:
    if integers_from_1_to_100[index] % 7 == 0 and integers_from_1_to_100[index] % 5 != 0:
        divisible_by_7.append(integers_from_1_to_100[index])
    index += 1


print('\nЗнайдені числа ' +\
        'які діляться на 7, але не є  кратними 5-ти.')
print(divisible_by_7)
print()