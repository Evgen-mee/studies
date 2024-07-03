# используется для построения контекстных менеджеров, которые игнорируют заданные типы исключений.

# полностью подавляет исключения

# Контекстный менеджер, возвращаемый функцией suppress(), является реентерабельным

# from contextlib import contextmanager
# @contextmanager
# def suppress(*exceptions):
#     try:
#         yield
#     except Exception as error:
#         if type(error) not in exceptions:
#             raise


# from contextlib import suppress
#
# with suppress(ValueError):
#     num = int('python')
# print('beegeek')
#
# with suppress(TypeError, ZeroDivisionError):
#     num = 1 / 0
# print('pygen')
#
#
# выводит:
# beegeek
# pygen