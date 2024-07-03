# переносит последовательность обратных вызовов в новый контекстный менеджер ExitStack и возвращает его

# from contextlib import ExitStack
# class Greeter:
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('Привет,', self.name)
#         return self.name
#
#     def __exit__(self, *args, **kwargs):
#         print('Пока,', self.name)
#
#
# with ExitStack() as stack:
#     stack.enter_context(Greeter('Гвидо'))
#     stack.enter_context(Greeter('Трей'))
#     stack.enter_context(Greeter('Алан'))
#     new_stack = stack.pop_all()
#     print('Завершение блока with')
#
# выводит:
# Привет, Гвидо
# Привет, Трей
# Привет, Алан
# Завершение блока with


# исходная последовательность обратных вызовов становится пустой, поэтому после завершения блока with
# не выполняется ни одного вызова метода __exit__()

# Теперь все они находятся в новом контекстном менеджере, и для их вызова необходимо воспользоваться именно им.


# from contextlib import ExitStack
# class Greeter:
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('Привет,', self.name)
#         return self.name
#
#     def __exit__(self, *args, **kwargs):
#         print('Пока,', self.name)
#
#
# with ExitStack() as stack:
#     stack.enter_context(Greeter('Гвидо'))
#     stack.enter_context(Greeter('Трей'))
#     stack.enter_context(Greeter('Алан'))
#     new_stack = stack.pop_all()
#     print('Завершение блока with')
#
# new_stack.close()
#
# выводит:
# Привет, Гвидо
# Привет, Трей
# Привет, Алан
# Завершение блока with
# Пока, Алан
# Пока, Трей
# Пока, Гвидо