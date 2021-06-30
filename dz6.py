# lesson 6
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

# py --version -> Python 3.9.6 ОС: Windows 10 x64 19043.1081

import sys


def show_size(x: object) -> print:
    '''Возвращает размер объекта в памяти, по умолчанию в байтах.

    :param x: объект
    :return: print
    '''

    print(f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx)

# _______________________________________________________________________________
# message = 'Введите четыре элемента: {}-ой строки через пробел: '
# result = [[*(m := tuple(map(int, input(message.format(el)).split()))), sum(m)] for el in range(1, 5)]
# print(*result, sep='\n')
#
# show_size(result)
# input X4 1 2 3 4
# size= 88, object= [[1, 2, 3, 4, 10], [1, 2, 3, 4, 10], [1, 2, 3, 4, 10], [1, 2, 3, 4, 10]]
# size= 120, object= [1, 2, 3, 4, 10]
# int= 28

# _______________________________________________________________________________
# message = 'Введите четыре элемента: {}-ой строки через пробел: '
# result = ((*(m := tuple(map(int, input(message.format(el)).split()))), sum(m)) for el in range(1, 5))
# print(*result, sep='\n')
#
# show_size(result)
# size= 112, object= <generator object <genexpr> at 0x000001EAA2EBCD60>


# _______________________________________________________________________________
# import random
#
# matrix = [[random.randint(0, 100) for el in range(5)] for _ in range(5)]
# print(*matrix, sep='\n')
#
# result = 0
#
# for el in range(5):
#     range_matrix = 100
#     for n in range(5):
#         if matrix[n][el] < range_matrix:
#             range_matrix = matrix[n][el]
#     if range_matrix > result:
#         result = range_matrix
#
# print(f'{result = }')
#
# show_size(matrix)
# size= 120, object= [[22, 42, 60, 59, 7], [13, 49, 91, 96, 69], [59, 28, 41, 84, 17], [39, 54, 33, 72, 32], [91, 24, 3, 49, 8]]
# size= 120, object= [22, 42, 60, 59, 7]
# size= 28, object= 22

# _______________________________________________________________________________
# result = {n: tuple(el for el in range(2, 100) if el % n == 0) for n in range(2, 10)}
#
# for k, v in result.items():
#     print(f'Для числа {k} кратны {len(v)} чисел, кратные числа', *v, sep=', ')
#
# show_size(result)
# # size= 360, object= result
# _______________________________________________________________________________
