# Запрос у пользователя числа и
# вывод на консоль информации о том является ли оно четным.
# Программа должна завершаться только, когда пользователь введет "stop".

while True:
    number = input("""Введите число для проверки четности или нечетности.
(для завершения программы введите 'stop'): """)
    if number == 'stop':
        print('\nВы завершили работу программы!!!')
        break
    else:
        number = int(number)
        if number % 2 == 0:
            print(f'\nЧисло {number} является четным\n')
        else:
            print(f'\nЧисло {number} является нечетным\n')
