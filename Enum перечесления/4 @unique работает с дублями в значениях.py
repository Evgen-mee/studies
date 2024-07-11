# Элементы перечисления, имеющие одинаковые значения, являются одним и тем же объектом,
# который был создан раньше

# from enum import Enum
#
# class Weekday(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7
#     Monday = 1                           # одинаковое значение ссылается на MONDAY
#
#
# print(Weekday.MONDAY)                    # Weekday.MONDAY
# print(Weekday.Monday)                    # Weekday.MONDAY
# print(Weekday.MONDAY is Weekday.Monday)  # True
#
# Элементы с одинаковыми значениями, созданные позже, не учитываются при итерировании по перечислению
# for day in Weekday:
#     print(day.name, '->', day.value)
#
# выводит:       # Monday не вывелось!!!!
# MONDAY -> 1
# TUESDAY -> 2
# WEDNESDAY -> 3
# THURSDAY -> 4
# FRIDAY -> 5
# SATURDAY -> 6
# SUNDAY -> 7


# декоратор приведет к возбуждению исключения, если в перечислении значения каких-либо элементов совпадают
# from enum import Enum, unique
# @unique
# class Weekday(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7
#     Monday = 1
#
# приводит к возбуждению исключения:
# ValueError: duplicate values found in <enum 'Weekday'>: Monday -> MONDAY

