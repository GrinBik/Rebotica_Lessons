def calc(num1, num2, oper):
    if oper == '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
        else:
            print(f'{num1} / {num2} = {result}')
        finally:
            print('повторим..')
while True:

    try:
        num1 = int(input('Введите первое число: '))
    except ValueError:
        print('Введите, пожалуйста, число!')
        continue
    else:
        print('Отлично! Продолжим..')

    oper = input('Введите оператор: ')

    try:
        num2 = int(input('Введите второе число: '))
    except ValueError:
        print('Введите, пожалуйста, число!')
        continue
    else:
        print('Отлично! Продолжим..')

    calc(num1, num2, oper)