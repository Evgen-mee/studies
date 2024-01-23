# Чтобы не писать каждый раз функции,
# определяющие такие стандартные математические
# операции как сумма или произведение:
#
# можно использовать уже реализованные функции из модуля operator
#
# from operator import *
# a + b	add(a, b)
# obj in seq	contains(seq, obj)
# a / b	truediv(a, b)
# a // b	floordiv(a, b)
# a ** b	pow(a, b)
# a % b	mod(a, b)
# a * b	mul(a, b)
# -a	neg(a)
# a - b	sub(a, b)
# a < b	lt(a, b)
# a <= b	le(a, b)
# a == b	eq(a, b)
# a != b	ne(a, b)
# a >= b	ge(a, b)
# a > b	gt(a, b)
#
# from operator import *     #  импортируем все функции
#
# print(add(10, 20))         #  сумма
# print(floordiv(20, 3))     #  целочисленное деление
# print(neg(9))              #  смена знака
# print(lt(2, 3))            #  проверка на неравенство <
# print(lt(10, 8))           #  проверка на неравенство <
# print(eq(5, 5))            #  проверка на равенство ==
# print(eq(5, 9))            #  проверка на равенство ==

# from operator import add
# from functools import reduce
#
# result = reduce(add, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(result)