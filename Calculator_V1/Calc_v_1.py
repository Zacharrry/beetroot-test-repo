name = input("Для початку роботи потрібно ввести Ваше ім\'я: ").capitalize()
clear_screen = "\033c"
clear_screen = "\033c"

attention = "\nУвага! Цей калькулятор має змогу виконувати дії тільки з двома числами." +\
      "\nНаприклад: X + Y або X - Y"
operation = "\n\nДоступні операції:" +\
            "\n\t1) додавання чисел" +\
            "\n\t2) віднімання чисел" +\
            "\n\t3) множення чисел" +\
            "\n\t4) ділення чисел" +\
            "\n\t5) піднести число в стеінь" +\
            "\n\t6) ділення по модулю" +\
            "\n\t7) ділення націло"

functions = "\n\nДоступні функції:" +\
            "\n\t8) знайти квадрат числа" +\
            "\n\t9) округлення числа до вказаної кілкості знаків" +\
            "\n\t10) обчислення факторіалу" 

type_error = "\nНекоректний тип даних"
next_iteration = "\nДля продовження натисніть клавішу [ENTER]: "

num_a_request = "\nВведіть будь ласка перше число: "
num_b_request = "\nВведіть будь ласка друге число: "

while True:
    
        print(clear_screen)
        print("Здоровенькі були, ",name, "Де вас носило?")
        
        print(attention,operation.expandtabs(8), functions.expandtabs(8))
        
        user_choice = input("\nВведіть номер операції або 'quit' для виходу: ").strip()
        
        if ((user_choice.isdigit() and int(user_choice) < 11) or user_choice == 'quit') is False:
            print(clear_screen)
            
            print("\nНекорректний тип операції\n")
            input(next_iteration)
            continue
        elif user_choice.isdigit():
            user_choice = int(user_choice)
            
        if user_choice == 'quit':
            print("\nХорошого Вам дня!\n")
            quit()
        
        if user_choice <= 7:
        
            if user_choice != 5:
                a = input(num_a_request).strip()
                b = input(num_b_request).strip()
                
                
            if user_choice == 5:
                a = input("\nВведіть основу степеня: ").strip
                b = input("Введите показник степеня: ").strip
                
            if a.count('-') > 1:
                print(type_error, "в числі", a)
                input(next_iteration)
                continue
            
            if b.count('-') == 1:
                if b[0] != '-':
                    input(next_iteration)
                    continue
                    
            if a.count('.') > 1 or a.count(',') > 1:
                print(type_error, "в числі", a)
                input(next_iteration)
                continue
            
            if a.lstrip('-').isdigit():
                a = int(a)    
            elif a.count('.') == 1:
                a = float(a)
            elif a.count(',') == 1:
                a = float(a.replace(',','.',1))
            else:
                print(type_error, "в числі", a)
                input(next_iteration)
                continue
            if b.count('-') == 1:
                if b[0] != '-':
                    print(type_error, "в числі", b)
                    input(next_iteration)
                    continue
            if b.count('.') > 1 or b.count(',') > 1:
                c
                input(next_iteration)
                continue
                
            if b.lstrip('-').isdigit():
                b = int(b)
            elif b.count('.') == 1:
                b = float(b)
            elif b.count(',') == 1:
                b = float(b.replace(',','.',1))
            else:
                print(type_error, "в числі", b)
                input(next_iteration)
                continue
            
        if user_choice == 1:
                print(f'\nРезультат додавання {a} + {b}: {a + b}')
                input(next_iteration)
                continue
            
        elif user_choice == 2:
                print(f'\nРезультат віднімання {a} - {b}: {a + b}')
                input(next_iteration)
                continue
            
        elif user_choice == 3:
                print(f'\nРезультат множення {a} * {b}: {a * b}')
                input(next_iteration)
                continue
                
        elif user_choice == 4:
                if b == 0:
                    print("\nУпсю Ділення на нуль!")
                    input(next_iteration)
                    continue
                    
                print(f'\nРезультат ділення {a} / {b}: {a / b}')
                input(next_iteration)
                continue
                
        elif user_choice == 5:
                print(f'\nРезультата піднесення основи {a} до показника {b}: {a ** b}')
                input(next_iteration)
                continue
            
        elif user_choice == 6:
                print(f'\nРезультат ділення по модулю {a} mod {b}: {a % b}')
                input(next_iteration)
                continue
                
        elif user_choice == 7:
                print(f'\nРезультат ділення без остачі {a} / {b}: {a // b}')
                input(next_iteration)
                continue
                
        elif user_choice == 8:
                num_sqrt = input("Введіть основу кореня: ").strip()
                
                if num_sqrt.count('-') >= 1:
                    print(type_error, 'в числі', num_sqrt)
                    print("Основа квадратного кореня не може бути від\'ємною")
                    input(next_iteration)
                    continue
                    
                if num_sqrt.count('.') > 1 or num_sqrt.count(',') > 1:
                    print(type_error, 'в числі', num_sqrt)
                    input(next_iteration)
                    continue
                    
                if num_sqrt.isdigit():
                    num_sqrt = int(num_sqrt)                  
                elif num_sqrt.count('.') == 1:
                    num_sqrt = float(num_sqrt)
                elif num_sqrt.count(',') == 1:
                    num_sqrt = float(num_sqrt.replace(',','.',1))
                else:
                    print(type_error, 'в числі', num_sqrt)
                    print("Основа квадратного кореня не може бути від\'ємною")
                    input(next_iteration)
                    continue
                    
                print(f'\nРезультат обчислення квадратного кореня з {num_sqrt}: {num_sqrt**(1/2)}')
                input(next_iteration)
                continue
                
        elif user_choice == 9:
                
                a = input("\nВведіть число для округлення: ").strip()
                b = input("\nВведіть число знаків після коми: ").strip()
                
                if a.count('-') > 1:
                    print(type_error, 'в числі', a)
                    input(next_iteration)
                    continue
                if b.count('-') == 1:
                    if b[0] != '-':
                        print(type_error, 'в числі', a)
                        input(next_iteration)
                        continue
                    
                if a.count('.') > 1 or a.count(',') >1:
                    print(type_error, 'в числі', a)
                    input(next_iteration)
                    continue
                    
                if a.lstrip('-').isdigit():
                    a = int(a)
                elif a.count('.') == 1:
                    a = float(a)
                elif a.count(',') == 1:
                    a = float(a.replace(',','.',1))
                else :
                    print(type_error, 'в числі', a)
                    input(next_iteration)
                    continue
                    
                if b.count('.') >= 1 or b.count(',') >= 1:
                    print(type_error, 'в числі', b)
                    print('Число знаків після коми може бути тільки натуральним.')
                    input(next_iteration)
                    continue
                    
                if b.isdigit():
                    b =int(b)
                else:
                    print(type_error, 'в числі', b)
                    print('Число знаків після коми може бути тільки натуральним.')
                    input(next_iteration)
                    continue
                    
                print(f'\nРезультат округлення {a} до {b} знаків після коми: {round(a,b)}')
                input(next_iteration)
                continue
                
        elif user_choice == 10:
                factorial_num = input("Введіть число факторіалу: ").strip()
                
                
                if factorial_num.count('-') >= 1:
                    print(type_error, 'в числі', factorial_num)
                    print("Число факторіалу очікується натуральним.")
                    input(next_iteration)
                    continue
                
                if factorial_num.count('-') >= 1 or factorial_num.count(',') >= 1:
                    print(type_error, 'в числі', factorial_num)
                    print("Число факторіалу очікується натуральним.")
                    input(next_iteration)
                    continue
                    
                if factorial_num.isdigit():
                    factorial_num = int(factorial_num)
                else:
                    print(type_error, 'в числі', factorial_num)
                    print("Число факторіалу очікується натуральним.")
                    input(next_iteration)
                    continue
                index = 1
                n = factorial_num
                while index < n:
                    factorial_num *= index
                    index += 1
                    
                print(f"\nРезультат обчислення факторіалу: {factorial_num}")
                input(next_iteration)
                continue
                
                    
                    
                    
                    
                
                    
                    
                        
                
                
                
                                        

                                        


                    
                
                    
            
                        

            
