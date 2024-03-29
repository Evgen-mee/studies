# чтобы Python мог правильно распознать такой текст, пользуемся разными:
#
# если в тексте нужны одинарные кавычки, то для обрамления такого текста используем двойные кавычки;
# если в тексте нужны двойные кавычки, то обрамляем его одинарными.
# Результатом выполнения кода:
#
# print('В тексте есть "двойные" кавычки')
# print("В тексте есть 'одинарные' кавычки")
# будет:
#
# В тексте есть "двойные" кавычки
# В тексте есть 'одинарные' кавычки

# num1 = -6      # унарный минус
# num2 = 17 - 7  # бинарный минус


# Результатом работы следующей программы:
#
# print(10 // 3)
# print(-10 // 3)
# будут числа:
#
# 3   # округление в меньшую сторону
# -4  # округление в меньшую сторону

# последняя цифра числа определяется всегда как остаток от деления числа на 10 (% 10).
# Чтобы отщепить последнюю цифру от числа, необходимо разделить его нацело на 10 (// 10).

# Для удобного чтения чисел можно использовать символ подчеркивания:
#
# num1 = 25_000_000
# num2 = 25000000
# print(num1)
# print(num2)
# Результатом выполнения такого кода будет:
#
# 25000000
# 25000000

# abs() приобразовывает модуль числа отрицательные в положительные

# min (1,2,3,4,5) и max(,233,56,6786) Находит меньшие и большее число

# pow(2,3) ВОЗВОДИМ в степень

# round (7,4) ОКРУГЛЯЕТ К БЛИЖАШЕМУ ЦЕЛОМУ 0.5 = 0 все остальные 1.5 = 2

# round (1.342425,2) при перадачи второго параметра указываем сколько знаков после запятой

# math.ceil(5.2) ОКРУГЛЕНИЕ К БОЛЬШЕМУ ЧИСЛУ

# math.floor(5.2) ОКРУГЛЕНИЕ К МЕНЬШЕМУ ЧИСЛУ

# match.factorial(6) ФАКТОРИАЛ

# match.round (7.6) ОТБРАСЫВАЕТ дробную часть как int

#match.log2 (4) ЛОГАРИФМ

#match.sqrt (4) КОРЕНЬ ИЗ КВАДРАТА

# Примечание 1. Тройные кавычки в Python используются для многострочного (multiline) текста. Например,
#
# text = '''Python is an interpreted, high-level, general-purpose programming language.
# Created by Guido van Rossum and first released in 1991, Python design
# philosophy emphasizes code readability with its notable use of significant whitespace.'''
# Примечание 2. На первый взгляд может показаться странным, что можно использовать как одинарные, так и двойные кавычки, однако такой подход позволяет очень легко добавлять в строку нужные кавычки:
#
# s1 = 'Мы можем использовать в одиночных кавычках двойные кавычки "Война и мир"'
# s2 = "Мы можем использовать в двойных кавычках одиночные кавычки 'Война и мир'"
# print(s1)
# print(s2)
# Результатом выполнения такого кода будет:
#
# Мы можем использовать в одиночных кавычках двойные кавычки "Война и мир"
# Мы можем использовать в двойных кавычках одиночные кавычки 'Война и мир'

# записать число в лист
# s=[int(i) for i in input()]

# В одну строку
# [print('YES' if '.' in i and '@' in i else 'NO') for i in [input()]]

# в f строке можно создавать переменную
# f'Футбольная команда {(name := input())} имеет длину {len(name)} символов'


# циклы, повторяющиеся определенное количество раз (for, счетные циклы, counting loops);
# циклы, повторяющиеся до наступления определенного события (while, условные циклы, conditional loops).


# range(10)	0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# range(1, 10)	1, 2, 3, 4, 5, 6, 7, 8, 9
# range(3, 7)	3, 4, 5, 6
# range(7, 3)	пустая последовательность
# range(2, 15, 3)	2, 5, 8, 11, 14
# range(9, 2, -1)	9, 8, 7, 6, 5, 4, 3
# range(3, 10, -2)	пустая последовательность

# while условие:
#     блок кода1
# else:
#     блок кода2
# Блок кода2, указанный в else, будет выполнен, когда штатным образом завершается цикл while или for.


# В Python можно использовать смайлики emoji👍

# если длина строки s равна len(s), то при положительной нумерации слева направо, последний
# элемент имеет индекс равный len(s) - 1,
# а при отрицательной индексации справа налево, первый элемент имеет индекс равный -len(s).


# исла в 2-ичную систему нашел интересную функцию -Format.
#
# P.S. кто не смог решить можете воспользоваться a = format(a, 'b') , b в этом случае и переводит значение нашей переменной в 2-ичную систему.
#
# s - строка, можно не указывать, используется по умолчанию;
# b - двоичный формат;
# с - преобразует целое число в символ Unicode;
# d - десятичный формат;
# e - научный формат, со строчной буквой e;
# E - научный формат, с E верхним регистром;
# f - формат чисел с плавающей запятой;
# F - формат чисел с плавающей запятой, верхний регистр;
# g - общий формат, нижний регистр;
# G - общий формат, верхний регистр;
# o - Восьмеричный формат;
# x - шестнадцатеричный формат, нижний регистр;
# X - шестнадцатеричный формат, верхний регистр;
# n - формат целых чисел;
# %- Процентный формат. Умножает число на 100 и использует f для вывода. В конце ставится %;
# #- альтернативный вариант вывода указанного формата, работает с форматами b, o, x.

# Матрицы
# сначала всегда указывается строка, а затем — столбец1
# rows, cols = 3, 4  # rows - количество строк, cols - количество столбцов
# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]
#
# for r in range(rows):
#     for c in range(cols):
#         print(matrix[r][c], end=' ')
#     print()
#
# 2 3 1 0
# 9 4 6 8
# 4 7 2 7
#
# перебора элементов матрицы по столбцам можно использовать следующий код:
# rows, cols = 3, 4  # rows - количество строк, cols - количество столбцов
#
# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]
#
# for c in range(cols):
#     for r in range(rows):
#         print(matrix[r][c], end=' ')
#     print()
#
# 2 9 4
# 3 4 7
# 1 6 2
# 0 8 7
#

# n = 3
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# for i in range(n):
#     for j in range(n):
#         print(a[n - i - 1][n - j - 1], end=' ')
#     print()
#
# 9 8 7
# 6 5 4
# 3 2 1

# Исходная строка не обрезается, даже если в ней больше символов, чем нужно.
# Строковый метод ljust() выравнивает текст по ширине, добавляя пробелы в конец текста.
# использует вместо пробела другой символ, если передать ему второй аргумент, необязательный.
# print('a'.ljust(5, '*'))
# a****
#
# Строковый метод rjust() выравнивает текст по ширине, добавляя пробелы в начало текста.
# print('a'.rjust(3))
# ⎵⎵a
#
# rows, cols = 3, 4  # rows - количество строк, cols - количество столбцов
#
# matrix  = [[277, -930, 11, 0],
#            [9, 43, 6, 87],
#            [4456, 8, 290, 7]]
#
# for r in range(rows):
#     for c in range(cols):
#         print(str(matrix[r][c]).ljust(6), end='')
#     print()
#
# 277   -930  11    0
# 9     43    6     87
# 4456  8     290   7
#
#
# Матрица с одинаковым количеством строк и столбцов называется квадратной. У квадратной матрицы есть две диагонали:
#
# главная: проходит из верхнего левого в правый нижний угол матрицы;
# побочная: проходит из нижнего левого в правый верхний угол матрицы.




def foo(x):
    return sorted(set([int(i) for i in x if x.count(i) > 1]))


print(foo(a, b, c))