# В Python присутствует строгая иерархия исключений,
# вершиной которой является тип BaseException.

# Тип BaseException является классом самого верхнего уровня
# и базовым для всех прочих классов исключений.

# Дерево встроенных исключений выглядит так:
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#            +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning
#
# Тип Exception – базовый класс для большинства встроенных в Python исключений.
# Именно его, а не BaseException,
# необходимо наследовать при создании пользовательского класса исключения.


# Обработчик исключений может поймать не только указанные типы исключений, но и всех их потомков.


# Если нужен доступ к сгенерированному исключению как к объекту
# то используется специальный синтаксис.
# try:
#     nums = [10, 5, 20, 25]
#     print(nums[100])
# except (KeyError, IndexError) as err:    # записываем сгенерированное исключение в переменную err
#     print(err)
#     print(type(err))
# выводит:
# list index out of range
# <class 'IndexError'>

#  - dir()
# Выводит все 1 Атрибуты объекта сгенерированного исключения
#
# try:
#     print(1 / 0)
# except ZeroDivisionError as err:
#     print(dir(err))

# выводит:
# ['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__',
#  '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
#  '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__',
#  '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
#  '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__',
#  '__traceback__', 'args', 'with_traceback']


# Если при обработке всех исключений одним блоком except
# мы хотим получить доступ к объекту исключения, то нужно явно указать его тип.
#
# синтаксически неверен!!!
# try:
#     х = 1 / 0
# except as err:
#     print(err)
#
# верен!!!
# try:
#     х = 1 / 0
# except Exception as err:
#     print(err)


#   - exc_infо() из модуля sys
# возвращает кортеж из трех значений:
# -типа исключения
# -значения объекта с трассировочной информацией об исключении
# -которое в данный момент обрабатывается.
# from sys import exc_info
# try:
#     х = 1 / 0
# except Exception as err:
#     print(exc_info())
# выводит:
# (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x000001BEEF80E840>)
#
# Преобразовать эти значения в удобочитаемый вид позволяет модуль traceback


