# lesson 4

# task 1
# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках практического задания первых трех уроков.

import timeit
import cProfile
import random

# def array_search(list_, to_where, number):
#     for index in range(to_where):
#         if list_[index] == number:
#             return index
#     return -1

# def test_array_search():
#     test_list = [45, 67, 34, 1, 0, 25, 4, 9]
#     result = array_search(test_list, 3, 34)
#     if result == 2:
#         return 'ok'
#     else:
#         return 'fail'

# def test_array_search_2():
#     test_list = [45, 67, 34, 1, 0, 25, 4, 9]
#     result = array_search(test_list, 7, 100)
#     if result == -1:
#         return 'ok'
#     else:
#         return 'fail'
#
# def test_array_search_3():
#     test_list = [45, 12, 34, 1, 12, 25, 12, 9]
#     result = array_search(test_list, 7, 12)
#     if result == 1:
#         return 'ok'
#     else:
#         return 'fail'

# print(test_array_search())
# print(timeit.timeit(test_array_search))
# cProfile.run('test_array_search')


# посчитать сумму чисел в массиве

# arr = [random.randint(0, 100) for n in range(990)]
#
#
# def counting_in_a_loop(arr):
#     sum_ = 0
#     for el in arr:
#         sum_ += el
#     return sum_
#
#
# def recursive_counting(arr):
#     if not arr:
#         return 0
#     else:
#         sum_ = recursive_counting(arr[1:])
#         sum_ = sum_ + arr[0]
#         return sum_


# print(counting_in_a_loop(arr))
# print(recursive_counting(arr))

# cProfile.run('counting_in_a_loop(arr)')
# cProfile.run('recursive_counting(arr)')

# в цикле посчитать ничего не стоит по нулям, а в рекурсивной функции 0.011
# после 990 рекурсий профайлер ругается, а python после 998
# сложность O(n) линейная


# task 2
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена


# def no_eratosthenes(n=12):
#     sieve = []
#     for k in range(2, n):
#         switch = True
#         for c in range(2, k):
#             if k % c == 0:
#                 switch = False
#         if switch:
#             sieve.append(k)
#     return f'Для чисел от 0 до {n}, простыми являются {sieve}'


# def eratosthenes(n=12):
#     sieve = (a for a in range(2, n + 1) if
#              a not in (c for ob in (list(range(2 * k, n + 1, k)) for k in range(2, n // 2)) for c in ob))
#     return f'Для чисел от 0 до {n}, простыми являются {tuple(sieve)}'


# print(no_eratosthenes(25))
# print(eratosthenes(25))

# cProfile.run("no_eratosthenes(12)")
# cProfile.run("eratosthenes(12)")

# print(timeit.timeit(no_eratosthenes))
# print(timeit.timeit(eratosthenes))
