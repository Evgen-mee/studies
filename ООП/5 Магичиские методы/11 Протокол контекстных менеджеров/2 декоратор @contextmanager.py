# Декоратор @contextmanager позволяет создать контекстный менеджер на основе функции,
# автоматически предоставляя оба требуемых метода __enter__() и __exit__()

# Обычно с помощью декоратора @contextmanager создают относительно несложные контекстные менеджеры

# Контекстные менеджеры созданные с помощью декоратора @contextmanager являются одноразовыми

# При использовании контекстных менеджеров на основе функций мы можем добиться аналогичного поведения,
# если будем возвращать лямбда-функцию
# from time import perf_counter, sleep
# from contextlib import contextmanager
#
# @contextmanager
# def timer():
#     start = perf_counter()
#     end = 0
#     yield lambda : (start, end)
#     end = perf_counter()
#
# with timer() as manager:
#     sleep(1.4)
#     print(manager())            # вызов внутри блока with
#
# print(manager())                # вызов после блока with
# start, end = manager()
# print('Затраченное время:', end - start)

# Для обработки исключений в контекстных менеджерах на основе функций
# мы должны использовать конструкцию try-except-finally
# class CustomContextManager:
#     def __enter__(self):
#         print('Вход в контекстный менеджер...')
#         return 'Python generation!'
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print('Выход из контекстного менеджера...')
#         if isinstance(exc_value, IndexError):
#             print(f'Тип возникшего исключения: {exc_type}')
#             print(f'Текст исключения: {exc_value}')
#             return True                                 # подавляем возбужденное исключение IndexError
#         return False
#
# с использованием декоратора @contextmanager можно переписать в виде:
#
# from contextlib import contextmanager
#
# @contextmanager
# def custom_context_manager():
#     print('Вход в контекстный менеджер...')                      # выполняется __enter__()
#     try:
#         yield 'Python generation!'                               # возвращаем __enter__() если нет ошибок
#     except IndexError as error:                                  # проверка на индекс
#         print(f'Тип возбужденного исключения: {type(error)}')    # напечатали exc_type
#         print(f'Текст исключения: {error}')                      # напечатали  exc_value
#     except:                           # если исключение не планируется подавлять, оно должно быть возбуждено повторно
#         raise          # return False
#     finally:
#         print('Выход из контекстного менеджера...')
#
# with custom_context_manager() as manager:
#     print(manager)
#
# выводит:
# Вход в контекстный менеджер...
# Python generation!
# Выход из контекстного менеджера...

