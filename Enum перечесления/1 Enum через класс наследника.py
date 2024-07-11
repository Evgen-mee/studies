# имена элементов перечисления рекомендуется записывать в верхнем регистре
# Элементы перечисления являются функциональными константами, и представляют собой экземпляры класса перечисления.

# элементы перечисления являются экземплярами класса перечисления!!!!!

# перечисления используются для представления констант,
# изменение значений их элементов невозможно, и приводит к возбуждению исключения

# Элементы перечисления являются хешируемыми, то есть мы можем использовать их в качестве ключей в словарях,
# а также в качестве элементов в множествах.


# имеют атрибуты name и value, в которых содержатся их имена и значения соответственно
# определены методы __str__() и __repr__() для информативного строкового представления


# элементы перечислений принимают любые типы


# Перечисления являются итерируемыми объектами!!!!

# По умолчанию перечисления не поддерживают операции сравнения с помощью операторов >, <, >= и <=,
# поэтому для их сортировки необходимо использовать ключевую функцию


# Можем получть доступ разными способами !!!!!
# print(Weekday.MONDAY)                         # точечная нотация с указанием имени элемента
# print(Weekday['MONDAY'])                      # доступ по ключу в виде имени элемента
# print(Weekday(1))                             # вызов перечисления с аргументом в виде значения элемента


# Каждый элемент перечисления является синглтоном
# при сравнении элементов удобно пользоваться более быстрыми операторами is и is not
#
# day = Weekday.MONDAY
#
# print(day is Weekday.MONDAY)          # True
# print(day is Weekday.TUESDAY)         # False
# print(day is not Weekday.MONDAY)      # False
# print(day is not Weekday.WEDNESDAY)   # True
#
# сравнение с помощью операторов == и !=, по сути, является сравнением на идентичность,
# результатом сравнения элементов с их фактическими значениями всегда будет False
# что бы сравнить используем value
# (Weekday.MONDAY.value) == 1 # True
# (Weekday.MONDAY) == 1 # False


# Если значениями элементов перечисления являются последовательные целые числа,
# начиная с 1, мы можем не прописывать их явно, а воспользоваться функцией auto() из модуля enum
# from enum import Enum, auto
#
# class Weekday(Enum):
#     MONDAY = auto()        # 1
#     TUESDAY = auto()       # 2
#     WEDNESDAY = auto()     # 3


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
#
#
# print(str(Weekday.MONDAY))    # Weekday.MONDAY
# print(repr(Weekday.MONDAY))   # <Weekday.MONDAY: 1>
# print(Weekday.MONDAY.name)    # MONDAY
# print(Weekday.MONDAY.value)   # 1







