# lesson 7

# task 1
# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random

#
# array_ = [random.randint(-100, 100) for _ in range(12)]
#
#
# def descending_bubble_sort(arr):
#     array = arr.copy()
#     position = 1
#
#     while position < len(array):
#         switch = True
#         for ind in range(len(array) - position):
#             if array[ind] < array[ind + 1]:
#                 array[ind], array[ind + 1] = array[ind + 1], array[ind]
#                 switch = False
#
#         if switch:
#             break
#         position += 1
#
#     return array
#
#
# print(array_)
# print(descending_bubble_sort(array_))

# task 2
# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

# array_ = [round(random.uniform(0, 50), 2) for _ in range(12)]
#
#
# def merging_two_arrays(first_arr, second_arr):
#     result, length_1, length_2 = [], len(first_arr), len(second_arr)
#     ind_1, ind_2 = 0, 0
#
#     while ind_1 < length_1 and ind_2 < length_2:
#
#         if first_arr[ind_1] <= second_arr[ind_2]:
#             result.append(first_arr[ind_1])
#             ind_1 += 1
#         else:
#             result.append(second_arr[ind_2])
#             ind_2 += 1
#
#     result += first_arr[ind_1:] + second_arr[ind_2:]
#     return result
#
#
# def split_merge_array(arr):
#     half_length = len(arr) // 2
#     arr_1, arr_2 = arr[:half_length], arr[half_length:]
#
#     if len(arr_1) > 1:
#         arr_1 = split_merge_array(arr_1)
#     if len(arr_2) > 1:
#         arr_2 = split_merge_array(arr_2)
#
#     return merging_two_arrays(arr_1, arr_2)
#
#
# print(f'{array_}')
# print(f'{split_merge_array(array_)}')

# task 3
# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.

# m = 12
# array_ = [random.randint(0, 100) for _ in range(2 * m + 1)]
#
#
# def divide_into_parts(array, border):
#     less, equal, more = [], [], []
#
#     for el in array:
#         if el < border:
#             less.append(el)
#         elif el > border:
#             more.append(el)
#         elif el == border:
#             equal.append(el)
#         else:
#             print('Случилось непредвиденное')
#
#     return less, equal, more
#
#
# def borderline(array, average_index):
#     border = array[random.randrange(0, len(array))] if not len(array) == 0 else 0
#     less, middle, more = divide_into_parts(array, border)
#
#     if len(less) == average_index:
#         return less
#     elif len(less) < average_index <= len(less) + len(middle):
#         return middle
#     elif len(less) > average_index:
#         return borderline(less, average_index)
#     else:
#         return borderline(more, average_index - len(less) - len(middle))
#
#
# def median(array):
#     return max(borderline(array, len(array) // 2 + 1))
#
#
# print(f'{array_} - рандомный')
# median_ = median(array_)
#
# array_.sort()
# print(f'{median_} - медиана, {array_.index(median_)} - индекс медианы, {len(array_)} - длина списка')
# print(f'{array_} - отсортированный')
