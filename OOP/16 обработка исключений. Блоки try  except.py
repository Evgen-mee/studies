# Введение в обработку исключений. Блоки try / except

# таблица наследования
#                               BaseException
#                                    ^
#   _________________________________|____________________________________
#   ^                   ^                       ^                        ^
#   |                   |                       |                        |
# Exception        SystemExit             GeneratorExit       KeyboardInterrupt
#   ^
#   |
#   ----------------------------------------------------------------------
#   ^           ^         ^       ^        ^         ^         ^         ^
#   |           |         |       |        |         |         |         |
# Attribute  Arithmetic   EOF    Name    Lookup      OS       Type     Value
#  Error       Error     Error   Error    Error     Error     Error    Error
#               ^                          ^          ^
#               | - ZeroDivision           | - Index  | - FileNotFound
#               |    Error                 |   Error  |      Error
#               |                          |          |
#               | - FloatingPoint          | - Key    | - Interrupted
#               |      Error               |  Error   |      Error
#               |                                     |
#               | - Overflow Error                    | - Permission
#                                                     |      Error
#                                                     |
#                                                     | - TimeOut Error
# если укажем Arithmetic Error (Базовый класс)
# то будут отлавливаться все исключения  наследников
# ZeroDivision, FloatingPoint, Overflow Error

# что бы понять где ошибка
# вначале прописываем узконаправленные исключения
# а затем Exception


# если написать просто except:
# это равнозначно Exception
# except(не указываем тип ошибки): == Exception


# исключения делятся на две группы
# в момент исполнения
# исключения в момент компиляции

# try значит попробывать

# исключения используют что бы:
# программа аварийно не завершилась
# пользователь получил информацию где и какая ошибка

try:
    x, y = map(int, input().split())
    res = x / y # возможно второе исключение ZeroDivision Error
except ValueError:
    print("Ошибка типа данных")
except ZeroDivisionError:
    print("деление на ноль недопустимо")

# Если отлавливаем несколько исключений можно записать
except (ValueError, ZeroDivisionError):

# можно использовать вложенные блоки
def get_number(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x