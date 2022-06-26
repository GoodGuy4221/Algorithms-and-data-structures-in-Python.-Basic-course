# task 1
# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в
# качестве делителя.
# import sys
#
#
# def validation_operand():
#     operand = None
#     while not operand in ('0', '+', '-', '*', '/'):
#         operand = input('Не верно введен знак операции! Введите что-то из (0 - для выхода, +, -, *, /) -> ')
#     sys.exit() if operand == '0' else None
#     return operand
#
#
# def validation_numbers(sign_and_numbers):
#     try:
#         tuple(map(float, sign_and_numbers))
#     except ValueError:
#         return False
#     else:
#         return True
#
#
# def calculator():
#     switch = True
#     while switch:
#         sign_and_numbers = input(
#             'Введите знак операции (0 - для выхода, +, -, *, /) и два натуральных числа через пробел -> ').split()
#         exit = True if sign_and_numbers[0] == '0' else False
#         switch = True if not exit and len(sign_and_numbers) == 3 and (validation_numbers(
#             sign_and_numbers[1:3])) else False
#         if switch:
#             number_1, number_2 = map(int, sign_and_numbers[1:3])
#             operand = sign_and_numbers[0] if sign_and_numbers[0] in ('+', '-', '*', '/') else validation_operand()
#             print(f'Сумма {number_1} и {number_2} = {number_1 + number_2}') if operand == '+' else None
#             print(f'Вычитание из {number_1}, {number_2} = {number_1 - number_2}') if operand == '-' else None
#             print(f'Произведение {number_1} и {number_2} = {number_1 * number_2}') if operand == '*' else None
#             print(
#                 f'Деление {number_1} на {number_2} = {round(number_1 / number_2, 2)}') if operand == '/' and not number_2 == 0 else None
#             print('Ошибка деления на ноль!') if operand == '/' and number_2 == 0 else None
#         elif not exit:
#             print('Введены некорректные числа')
#             calculator()
#
#
# calculator()

# task 2
# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# def count_even_and_odd_numbers(number):
#     even, odd = 0, 0
#     if type(number) == str and number.isdigit():
#         for el in number:
#             if int(el) % 2 == 0:
#                 even += 1
#             else:
#                 odd += 1
#     else:
#         return count_even_and_odd_numbers(str(number))
#     return f'У числа {number}, {even} четных и {odd} не четных цифры.'

# print(count_even_and_odd_numbers(input('Введите натуральное число ')))
# print(count_even_and_odd_numbers(1234567890))

# task 3
# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.


# reverse_number = lambda number: number[::-1] if type(number) == str else str(number)[::-1]
#
# number = input('Введите натуральное число: ')
# print(f'Для числа: {number} обратное число: {reverse_number(number)}')
# print(reverse_number(1234567890))


# def recursion(number, count=1):
#     number = str(number) if not type(number) == str else number
#     if len(number) == count:
#         return number
#     return number[-count] + recursion(number[0:-count])
#
#
# print(recursion(123456789))
# print(recursion(1000))

# task 4
# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.


# def find_the_sum_of_n_elements(n):
#     n = int(n) if not type(n) == int else n
#     count, result = 1, 0
#     for el in range(n):
#         result += count
#         count /= -2
#     return f'Сумма {n} элементов = {result}'
#
#
# print(find_the_sum_of_n_elements(
#     input('Введите натуральное желаемое количество элементов ряда чисел: 1 -0.5 0.25 -0.125... ')))

# task 5
# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

# for count, code in enumerate(range(32, 128), 1):
#     print(f'{code:4}: {chr(code)}', end=' ' if not count % 10 == 0 else '\n')

# task 6
# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное
# пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.


# import random
#
# number = random.randint(0, 100)
#
# for attempt in range(10, 0, -1):
#     user_number = input(f'Отгадайте натуральное число от 0 до 100, осталось попыток {attempt}: ')
#     user_number = int(user_number) if user_number.isdigit() else None
#     if number == user_number:
#         print(f'Ура, Вы отгадали, это {number}!')
#         break
#     elif user_number < number:
#         print(f'Больше!')
#     else:
#         print(f'Меньше!')
# else:
#     print(f'Эх, все попытки закончились, отгадать нужно было {number}')


# task 7
# 7. Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.

# n, o = 12, 0
#
# for el in range(1, n + 1):
#     o += el
# m = n * (n + 1) // 2
# print(f'{o == m}')

# task 8
# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


# def counting_the_occurrence_of_a_character(sequence, symbol):
#     count = 0
#
#     for el in sequence:
#         if el == symbol:
#             count += 1
#     return sequence, symbol, count
#
#
# result = counting_the_occurrence_of_a_character(input('Введите последовательность чисел '),
#                                                 input('Какую цифру нужно посчитать? '))
#
# print(f'В последовательности: {result[0]}, символ: {result[1]}, встречается: {result[2]} раз(а)')


# task 9
# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

# numbers = input('Введите натуральные числа через пробел ').split()
#
#
# def determine_the_sum_of_the_digits_of_a_number(number):
#     number = str(number) if not type(number) == str else number
#     sum = 0
#     for el in number:
#         sum += int(el)
#     return sum
#
#
# max_number = 0
# sum_max_number = 0
# for el in numbers:
#     if (s := determine_the_sum_of_the_digits_of_a_number(el)) > sum_max_number:
#         max_number, sum_max_number = el, s
#
# print(f'Наибольшее: {max_number}, его сумма чисел: {sum_max_number}')
