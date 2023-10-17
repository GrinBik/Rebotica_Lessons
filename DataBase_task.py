import pandas


# Подготовка словаря для дальнейшего создания DataFrame
def create_data(headers, lines):
    # Запоминаем длины списков
    len_headers = len(headers)
    len_lines = len(lines)
    # Итоговый словарь для DataFrame
    data = {}
    # Какое кол-во строк необходимо к заполнению
    number_of_lines = 0
    # Подготовка данных к заполнению каждого столбца
    for index, value in enumerate(headers):
        data[value] = temp_storage = [lines[j] for j in range(index, min(index + len_headers * 4, len_lines), len_headers)]
        # На первом шаге известно максимальное кол-во ожидаемых строк
        if index == 0:
            number_of_lines = len(temp_storage)
        # Для DataFrame необходимо одинаковое кол-во данных у каждой строки
        if len(temp_storage) < number_of_lines:
            data[value] = temp_storage + ['-']
    return data


# Входные данные
list_1 = ['first', 'second', 'third', 'fourth']
list_2 = [1,2,3,4,5,6,7,8,9,10,]

# Преобразовываем данные к DataFrame
result = create_data(list_1, list_2)

# Создание таблицы
db = pandas.DataFrame(result)
# Вывод
print(db)
