# Функция month() календарь на месяц оформленный вид из даты
# month(year, month, w=0, l=0) возвращает календарь на месяц в многострочной строке.

# Аргументами функции являются: year (год), month (месяц),
# w (ширина столбца даты) и l (количество строк, отводимые на неделю).

# import calendar
# print(calendar.month(2021, 9))
# print(calendar.month(2021, 10))
# print(calendar.month(2021, 9, w=3))
# print(calendar.month(2021, 9, l=2))
# print(calendar.month(2021, 9, w=5, l=2))
# выводит:

#    September 2021
# Mo Tu We Th Fr Sa Su
#        1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30

#     October 2021
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31

#        September 2021
# Mon Tue Wed Thu Fri Sat Sun
#           1   2   3   4   5
#   6   7   8   9  10  11  12
#  13  14  15  16  17  18  19
#  20  21  22  23  24  25  26
#  27  28  29  30

#    September 2021
#
# Mo Tu We Th Fr Sa Su
#
#        1  2  3  4  5
#
#  6  7  8  9 10 11 12
#
# 13 14 15 16 17 18 19
#
# 20 21 22 23 24 25 26
#
# 27 28 29 30

#               September 2021
#
#  Mon   Tue   Wed   Thu   Fri   Sat   Sun
#
#                1     2     3     4     5
#
#    6     7     8     9    10    11    12
#
#   13    14    15    16    17    18    19
#
#   20    21    22    23    24    25    26
#
#   27    28    29    30