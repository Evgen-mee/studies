# cама возможность вызова с любыми типами аргументов никак не ограничивается.
# def greet(name: str) -> str:
#     return f'Hello {name}!'
# типы принимаемых параметров, записываются после имени параметров:
# ("имя параметра": "тип принимаего параметра" )
#
# тип возвращаемого значения функции записывается после знака ->
# def greet(name: str) -> (возвращаемый тип функции):

# Если некоторый аргумент имеет значение по умолчанию,
# то его тип должен предшествовать значению по умолчанию:
# def greet(name: str = 'world') -> str:
#     return f'Hello, {name}!'


# можно использовать аннотации типов
# не являющиеся коллекциями!!!!
# int, float, bool, str, NoneType.

# можно объявлять типы переменных вообще в любом месте программы
# name: str = 'Timur'
# age: int = 29
# height: float = 171.5
# is_married: bool = False
#
# Можно также аннотировать переменные, не назначая им сразу значения:
# surname: str
# gender: bool

# коллекции
# list, tuple, set, dict
# Нужно знать не только с каким типом
# коллекции работаем но и что храниться в самой коллекции
#
# до версии 3.9
# использовать отдельные типы из модуля typing
# типы из модуля typing указываются с заглавной буквы
# from typing import List
# def sum_square(nums: List[int]) -> int:
#     total = 0
#     for i in nums:
#         total += i ** 2
#     return total
# или
# from typing import List, Tuple, Dict, Set
# numbers: List[int]                                # тип всех элементов списка
# person: Tuple[str, int, bool]                     # тип каждого элемента кортежа
# prices: Dict[str, int]                            # тип ключей, тип значений
# answers: Set[float]                               # тип всех элементов множества
#
#
# с Python 3.9
# можно использовать стандартные классы
# ничего ниоткуда не импортируя
# numbers: list[int]                                # тип всех элементов списка
# person: tuple[str, int, bool]                     # тип каждого элемента кортежа
# prices: dict[str, int]                            # тип ключей, тип значений
# answers: set[float]                               # тип всех элементов множества


# Атрибут __annotations__
# Доступ к использованным в функции аннотациям
# аннотации представлены в виде словаря,
# где ключами являются названия параметров, а значениями – их типы
# возвращаемое функцией значение хранится в записи с ключом return
#
# def print_hello(num1: int, num2: int, num3: int) -> float:
#     return (num1 + num2 + num3) / 3
# print(print_hello.__annotations__)
# выводит словарь:
# {'num1': <class 'int'>,
# 'num2': <class 'int'>,
# 'num3': <class 'int'>,
# 'return': <class 'float'>}

def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    res = {}
    for k, v in enumerate(matrix, 1):
        res[k] = v
    return res

matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]
print(matrix_to_dict(matrix))


