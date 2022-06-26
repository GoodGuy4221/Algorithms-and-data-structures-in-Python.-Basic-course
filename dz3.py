# lesson 3
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


# result = {n: tuple(el for el in range(2, 100) if el % n == 0) for n in range(2, 10)}
#
# for k, v in result.items():
#     print(f'Для числа {k} кратны {len(v)} чисел, кратные числа', *v, sep=', ')

# task 2
# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.


# first_array = [8, 3, 15, 6, 4, 2]
#
# second_array = [str(index) for index, el in enumerate(first_array, 1) if el % 2 == 0]
#
# print('Индексы четных элементов первого массива:', ' '.join(second_array))

# task 3
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы


# import random
#
# array_of_random_integers = [random.randint(0, 100) for _ in range(12)]
#
# print(array_of_random_integers)
#
# ma_x, mi_n = max(array_of_random_integers), min(array_of_random_integers)
# index_ma_x, index_mi_n = array_of_random_integers.index(ma_x), array_of_random_integers.index(mi_n)
# array_of_random_integers[index_ma_x], array_of_random_integers[index_mi_n] = array_of_random_integers[index_mi_n], \
#                                                                              array_of_random_integers[index_ma_x]
# print(array_of_random_integers)

# task 4
# 4. Определить, какое число в массиве встречается чаще всего.

# my_list = [70, 60, 69, 70, 35, 28, 99, 12, 5, 88, 70, 51]
# print(max(set(my_list), key=my_list.count))


# task 5
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

# import random
#
# array_of_random_numbers = [random.randint(-100, 100) for _ in range(12)]
# print(array_of_random_numbers)
#
# maximum_negative_element = max(filter(lambda n: n < 0, array_of_random_numbers))
#
# print(f'Индекс максимального отрицательного элемента: {array_of_random_numbers.index(maximum_negative_element)} и '
#       f'значение: {maximum_negative_element}')

# task 6
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# import random
#
# one_dimensional_array = [random.randint(0, 100) for _ in range(12)]
# print(one_dimensional_array)
#
# min_index_el, max_index_el = sorted(
#     (one_dimensional_array.index(max(one_dimensional_array)), one_dimensional_array.index(min(one_dimensional_array))))
# min_index_el += 1
#
# result = one_dimensional_array[min_index_el:max_index_el]
#
# print(f'Сумма элементов: {sum(result)}, массив: {result}. Срез от: {min_index_el} до: {max_index_el}')


# task 7
# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# import random
#
# one_array_of_integers = [random.randint(0, 100) for _ in range(12)]
# print(one_array_of_integers)
#
# one_array_of_integers.sort()
#
# print(f'Первый наименьший элемент: {one_array_of_integers[0]}, второй: {one_array_of_integers[1]}')


# task 8
# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

# message = 'Введите четыре элемента: {}-ой строки через пробел: '
# result = [[*(m := tuple(map(int, input(message.format(el)).split()))), sum(m)] for el in range(1, 5)]
# print(*result, sep='\n')

# task 9
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

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
