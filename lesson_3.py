# Запрос у пользователя числа и
# вывод на консоль информации о том является ли оно четным.

print("Проверка числа на четность или нечетность...")

# Запрос числа у пользователя
number = input("Введите число: ")

if number %2 == 0:
    print(f'Число {number} является четным')
else:
    print(f'Число {number} является нечетным')
