# lesson 8

# task 1
# 1. Определить количество различных подстрок с использованием хеш-функции.
# Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib

# def returns_substrings(line: str):
#     assert len(line) > 0, 'Строка не может быть пустой'
#
#     hash_set = set()
#
#     for i in range(len(line)):
#         if not (h := hashlib.sha1(line[i].encode('utf-8')).hexdigest()) in hash_set:
#             hash_set.add(h)
#
#     print(hash_set)
#
#     return len(hash_set)
#
#
# l_str = input('Введите строку: ')
#
# print(f'В строке {l_str}, {returns_substrings(l_str)} подстрок')


# another variant


# def returns_substrings(line: str):
#     assert len(line) > 0, 'Строка не может быть пустой'
#     hash_set = set()
#
#     for inx in range(len(line) - 1):
#         for k in range(inx + 1, len(line) + 1):
#             hash_set.add(hash(line[inx:k]))
#
#     count = len(hash_set) - 1
#
#     return count
#
#
# l_str = input('Введите строку: ')
# print(f'В строке {l_str}, {returns_substrings(l_str)} подстрок')


# task 2
# 2. Закодировать любую строку по алгоритму Хаффмана.


import collections

# class Leaf:
#     def __init__(self, key: str, value: int):
#         self.key = key
#         self.value = value
#
#
# class Node:
#     def __init__(self, value, left, right):
#         self.value = value
#         self.left = left
#         self.right = right
#
#
# class Huffman:
#     _data: list
#
#     def __init__(self):
#         self._code_table = {}
#         self._data = []
#         self._real_str = ''
#
#     def _make_list(self, real_str):
#         counter = dict(collections.Counter(real_str))
#         counter = collections.OrderedDict(sorted(counter.items(), key=lambda k: k[1], reverse=True))
#         for k, v in counter.items():
#             self._data.append(Leaf(k, v))
#         return True
#
#     def _huffman_tree(self):
#         while len(self._data) > 2:
#             a, b = self._data.pop(), self._data.pop()
#             trash = Node(b.value + a.value, b, a)
#             if trash.value > self._data[0].value:
#                 self._data.insert(0, trash)
#             elif trash.value < self._data[-1].value:
#                 self._data.append(trash)
#             else:
#                 for i in range(1, len(self._data)):
#                     if self._data[i - 1].value >= trash.value > self._data[i].value:
#                         self._data.insert(i, trash)
#                         break
#         self._data = Node(self._data[0].value + self._data[1].value, self._data[0], self._data[1])
#
#     def _huffman_recursion(self, data: Node, code=''):
#         if isinstance(data, Node):
#             self._huffman_recursion(data.left, code=code + '0')
#             self._huffman_recursion(data.right, code=code + '1')
#         elif isinstance(data, Leaf):
#             self._code_table[data.key] = code
#
#     def _encode(self):
#         result = []
#         for c in self._real_str:
#             result.append(self._code_table[c])
#         return ''.join(result)
#
#     def encode(self, real_str):
#         self.__init__()
#         self._real_str = real_str
#         self._make_list(real_str)
#         self._huffman_tree()
#         self._huffman_recursion(self._data)
#         code_str = self._encode()
#
#         return code_str
#
#     def decode(self, code_str, code_table=None):
#
#         if code_table:
#             self._code_table = code_table
#         decode_table = {v: k for k, v in self._code_table.items()}
#         result = []
#
#         i = 0
#         while i < len(code_str):
#             k = i + 1
#             while code_str[i:k] not in decode_table.keys():
#                 k += 1
#             result.append(decode_table[code_str[i:k]])
#             i = k
#
#         return ''.join(result)
#
#     def get_table_code(self):
#         if self._code_table:
#             return self._code_table
#         return False
#
#     def get_real_string_code(self):
#         if self._real_str:
#             result = []
#             for c in self._real_str:
#                 result.append(bin(ord(c))[2:].zfill(8))
#             return ''.join(result)
#         return False
#
#
# l_str = input('Введите строку: ')
# h = Huffman()
# code_s = h.encode(l_str)
# print(h.get_real_string_code())
# print(code_s)
# table = h.get_table_code()
# print(table)
# print(h.decode(code_s, table))
# print(h.decode(code_s))
