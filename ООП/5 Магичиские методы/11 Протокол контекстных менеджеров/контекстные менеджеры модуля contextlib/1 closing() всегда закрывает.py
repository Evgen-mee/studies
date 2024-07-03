# Функция closing() используется для построения контекстных менеджеров из объектов,
# которые предоставляют метод close(), но не реализуют протокол контекстного менеджера
# (отсутствуют методы __enter__() и __exit__()).


# В случае отсутствия метода close() у объекта возбуждается исключение AttributeError

# from contextlib import contextmanager
# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()


# from contextlib import closing
#
# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def close(self):                # будет вызываться всегда, даже если в блоке with возникает ошибка.
#         print('Пока,', self.name)
#
#
# with closing(Cat('Кемаль')) as cat:
#     print('Привет,', cat)

# выводит:
# Привет, Кемаль
# Пока, Кемаль