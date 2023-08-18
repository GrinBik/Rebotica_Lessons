from lesson_10 import calculator


print('КАЛЬКУЛЯТОР\n')
while True:
    # Запрос чисел и оператора у пользователя
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    oper = input("Введите оператор (+, -, *, /) или 'stop' для выхода: ")

    # Проверка на завершение программы
    if oper == 'stop':
        print("Программа завершена!!!")
        break
    # Проверка правильности введенного оператора
    elif oper not in ['+','-','/','*']:
        print("Оператор не распознан...\n")
        continue
    else:
        result = calculator(num1, oper, num2)
        short = lambda: print(f'{num1} {oper} {num2} = {result}')
        short()