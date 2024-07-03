# используется для построения пустых контекстных менеджеров, которые ничего не делают.

# from contextlib import contextmanager
# @contextmanager
# def nullcontext(enter_result=None):
#     yield enter_result

# from contextlib import nullcontext
#
# with nullcontext(2077) as manager:
#     print(manager)
#
# with nullcontext('pygen') as manager:
#     print(manager)
#
# выводит:
# 2077
# pygen


# удобно использовать для создания необязательного контекстного менеджера
#
# from contextlib import suppress, nullcontext
#
# def my_function(ignore_exceptions=False):
#     if ignore_exceptions:
#         manager = suppress(Exception)  # игнорируем исключения
#     else:
#         manager = nullcontext()  # не игнорируем исключения
#
#     with manager:
#             # код