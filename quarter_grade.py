# Основной цикл программы
while True:

    # Ввод общего числа оценок
    try:
        grade_number = int(input('Введите количество ваших оценок за четверть: '))
    except ValueError:
        print('Введены некорректные данные! Повторите попытку.')
        continue

    # Ввод всех оценок
    grades = list(input('Введите все имеющиеся оценки (через запятую, без пробела): ').split(','))

    # Проверка на совпадение кол-ва заявленных оценок и введенных
    if len(grades) != grade_number:
        print("Введено не соответствующее заявленному кол-во оценок! Повторите попытку.")
        continue

    # Подготовка оценок к вычислениям
    try:
        for i in range(grade_number):
            grades[i] = int(grades[i])
    except ValueError:
        print(f"Введены некорректные данные! Повторите попытку.")

    # Вывод на экран предварительной оценки за четверть
    quarter_grade = sum(grades) / grade_number
    if quarter_grade < 2.65:
        quarter_grade = 2
    elif quarter_grade < 3.65:
        quarter_grade = 3
    elif quarter_grade < 4.65:
        quarter_grade = 4
    else:
        quarter_grade = 5
    print(f'Предварительная оценка за четверть: {quarter_grade}')

    # Проверка на завершение программы
    print('Хотите ли вы продолжить программу?')
    exit = input("Для завершения введите 'stop', для продолжения нажмите 'enter'")

    # Пользователь выбрал завершение программы
    if exit == 'stop':
        print('Вы завершили программу')
        break
