# lesson 1 Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# Для каждого упражнения составить графическое представление алгоритма в виде
# блок-схемы и написать программную реализацию.

# task 1
# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# three_digit_number = input('Введите трехзначное число -> ')
# validation = True if three_digit_number.isdigit() and len(three_digit_number) == 3 else False
# if validation:
#     numeral_1, numeral_2, numeral_3 = map(int, three_digit_number)
#     print(f'Сумма цифр трехзначного числа: {sum((numeral_1, numeral_2, numeral_3))}, \
# произведение цифр трехзначного числа: {numeral_1 * numeral_2 * numeral_3}')
# else:
#     print('Вы ввели что-то не то')

# task 2
# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

# print(f'И {5 & 6} Или {5 | 6} исключающее Или {5 ^ 6} Нет 5 {~ 5} Нет 6 {~ 6}'
#     f'\nПобитовый сдвиг вправо на два знака: {5 >> 2}, побитовый сдвиг влево на два знака {5 << 2}')

# task 3
# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.

# coordinates = input('Введите координаты двух точек, четыре значения через пробел -> ').split()
# validation = True if len(coordinates) == 4 else False
# if validation:
#     x1, y1, x2, y2 = map(float, coordinates)
#     try:
#         k = (y2 - y1) / (x2 - x1)
#     except ZeroDivisionError as err:
#         print('Ошибка деления на ноль')
#     else:
#         b = y1 - k * x1
#         print(f'Уравнение прямой: y = {k}x + {b}')
# else:
#     print('Введено что-то не то')

# task 4
# 4. Написать программу, которая генерирует в указанных пользователем границах
# случайное целое число,
# случайное вещественное число,
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

# import random
#
# range_of_numbers = input('Введите через пробел диапазон чисел -> ').split()
# validation = True if len(range_of_numbers) == 2 and all((el.isdigit() for el in range_of_numbers)) else False
# if validation:
#     num_1, num_2 = map(int, range_of_numbers)
#     print(f'Случайное целое число в диапазоне от {num_1} до {num_2}: {random.randint(num_1, num_2)}')
# else:
#     print('Введено что-то не то')


# import random
#
# range_of_numbers = input('Введите через пробел диапазон чисел -> ').split()
# validation = True if len(range_of_numbers) == 2 and all((el.isdigit() for el in range_of_numbers)) else False
# if validation:
#     num_1, num_2 = map(int, range_of_numbers)
#     print(f'Случайное вещественное число в диапазоне от {num_1} до {num_2}: {random.uniform(num_1, num_2)}')
# else:
#     print('Введено что-то не то')

# import random
# import string
#
# alphabet = string.ascii_lowercase
#
# range_of_letters = input('Введите диапазон букв английского алфавита через пробел -> ').split()
# validation = True if len(range_of_letters) == 2 and all(
#     (el in alphabet and len(el) == 1 for el in range_of_letters)) else False
# if validation:
#     range_letter_1, range_letter_2 = alphabet.find(range_of_letters[0]), alphabet.find(range_of_letters[1]) + 1
#     random_letter_number = random.randint(range_letter_1, range_letter_2)
#     print(
#         f'Случайная буква из диапазона: {alphabet[random_letter_number]}, буквы диапазона: {(range_letters := alphabet[range_letter_1: range_letter_2])}, '
#         f'количество букв диапазона: {len(range_letters)}')
# else:
#     print('Введено что-то не то')

# task 5
# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

# import string
#
# alphabet = string.ascii_lowercase
#
# two_letters = input('Введите две буквы английского алфавита через пробел ').split()
# validation = True if len(two_letters) == 2 and two_letters[0] in alphabet and two_letters[1] in alphabet else False
#
# if validation:
#     letter_number_1, letter_number_2 = alphabet.find(two_letters[0]) + 1, alphabet.find(two_letters[1]) + 1
#     range_between_letters = max(letter_number_1, letter_number_2) - min(letter_number_1, letter_number_2) - 1
#     print(f'Первая буква стоит на {letter_number_1} месте, вторая на {letter_number_2} месте,\
# между ними находится {range_between_letters} букв(ы): {alphabet[letter_number_1:letter_number_2 - 1]}')
# else:
#     print('Введено что-то не то')

# task 6
# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# import string
#
# alphabet = string.ascii_lowercase
#
# number_letter = input('Введите номер буквы в английском алфавите: ')
# validation = True if number_letter.isdecimal() and (len(number_letter) == 1 or 2) and (
#     number_letter := int(number_letter)) <= 26 else False
# print(type(number_letter))
# if validation:
#     print(alphabet[number_letter - 1])
# else:
#     print('Введено что-то не то')

# task 7
# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

# three_segments = input('Введите через пробел длины трех отрезков (см. целые): ').split()
# validation = True if len(three_segments) == 3 and all((el.isdigit() for el in three_segments)) else False
# if validation:
#     section_1, section_2, section_3 = map(int, three_segments)
#     if section_1 + section_2 > section_3 and section_1 + section_3 > section_2 and section_2 + section_3 > section_1:
#         print('Треугольник существует')
#         if section_1 == section_2 == section_3:
#             print('Треугольник равносторонний')
#         elif section_1 != section_2 and section_2 != section_3 and section_1 != section_3:
#             print('Треугольник разносторонний')
#         else:
#             print('Треугольник равнобедренный')
#     else:
#         print('Треугольник не существует')
# else:
#     print('Введено что-то не то')

# task 8
# 8. Определить, является ли год, который ввел пользователем, високосным или не високосным.

# year = input('Введите номер года ')
#
# validation = True if year.isdigit() else False
#
# if validation and (year := int(year)):
#
#     if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
#         print(f'{year} год високосный')
#     else:
#         print(f'{year} год не високосный')
# else:
#     print('Введено что-то не то')

# task 9
# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# three_numbers = input('Введите три целых положительных числа через пробел ').split()
# validation = True if len(three_numbers) == 3 and all((el.isdigit() for el in three_numbers)) else False
# if validation:
#     ma_x, mi_d, mi_n = sorted(list(map(int, three_numbers)), reverse=True)
#     print(f'Самое большое число {ma_x}, среднее {mi_d}, маленькое {mi_n}')
# else:
#     print('Введенные данные не соответствуют задаче')
