# lesson 5

# task 1
# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

# number_of_enterprises = int(input('Введите количество предприятий -> '))
#
# enterprises = collections.namedtuple('enterprises', 'name quarter_1 quarter_2 quarter_3 quarter_4 year')
#
# name_enterprises = []
#
# for index, number in enumerate(range(1, number_of_enterprises + 1)):
#     user_input = input(
#         f'Введите данные {number}-го предприятия через пробел: наименование, прибыль за 4 квартала -> ').split()
#
#     name_enterprises.append(user_input[0])
#     user_input.remove(name_enterprises[index])
#     quarterly_profits = tuple(map(float, user_input))
#     year_profit = sum(quarterly_profits)
#
#     name_enterprises[index] = enterprises(name=name_enterprises[index], quarter_1=quarterly_profits[0],
#                                           quarter_2=quarterly_profits[1],
#                                           quarter_3=quarterly_profits[2], quarter_4=quarterly_profits[3],
#                                           year=year_profit)
#
# average_profit = 0
#
# for profit in range(number_of_enterprises):
#     average_profit += name_enterprises[profit].year
#
# average_profit /= number_of_enterprises
#
# print(f'Средняя прибыль за год для всех {number_of_enterprises} предприятий, {round(average_profit)}')
#
# for name in name_enterprises:
#     if (profit := name.year) > average_profit:
#         print(
#             f'Прибыль предприятия {name.name} {round(profit)}, выше средней на {round(profit - average_profit)} чего то там')
#     else:
#         print(
#             f'Прибыль предприятия {name.name} {round(profit)}, ниже средней на {round(average_profit - profit)} чего то там')

# task 2
# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# first_entered_hexadecimal_number = collections.deque(input('Введите первое шестнадцатеричное число -> ').upper())
# second_entered_hexadecimal_number = collections.deque(input('Введите второе шестнадцатеричное число -> ').upper())
#
# hex_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
#            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
#            0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
#            10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
#
#
# def adds_two_hexadecimal_numbers(number_1, number_2):
#     result = collections.deque()
#     additionally = 0
#
#     if len(number_2) > len(number_1):
#         number_1, number_2 = number_2, number_1
#
#     n_1 = number_1.copy()
#     n_2 = number_2.copy()
#     while n_1:
#
#         if n_2:
#             k = hex_num[n_1.pop()] + hex_num[n_2.pop()] + additionally
#
#         else:
#             k = hex_num[n_1.pop()] + additionally
#
#         additionally = 0
#
#         if k < 16:
#             result.appendleft(hex_num[k])
#
#         else:
#             result.appendleft(hex_num[k - 16])
#             additionally = 1
#
#     if additionally:
#         result.appendleft('1')
#
#     return ''.join(result)
#
#
# def multiplies_two_hexadecimal_numbers(number_1, number_2):
#     number_1, number_2 = int(''.join(number_1), base=16), int(''.join(number_2), base=16)
#     result = hex(number_1 * number_2).upper()
#     return result[2:]
#
#
# print(
#     f'Сумма {first_entered_hexadecimal_number} и {second_entered_hexadecimal_number} = {adds_two_hexadecimal_numbers(first_entered_hexadecimal_number, second_entered_hexadecimal_number)}')
# print(
#     f'Произведение {first_entered_hexadecimal_number} и {second_entered_hexadecimal_number} = {multiplies_two_hexadecimal_numbers(first_entered_hexadecimal_number, second_entered_hexadecimal_number)}')
