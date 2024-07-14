# Декорирование класса позволяет модифицировать поведение и содержание класса без изменения его исходного кода
# мы модифицируем исходный класс и возвращаем его же

# добавляет экземплярам декорируемого класса атрибут
# import functools
#
# def add_attr_to_instances(cls):                # принимает в качестве аргумента класс
#     old_init = cls.__init__                    # сохраняем исходный инициализатор
#
#     @functools.wraps(old_init)
#     def new_init(self, *args, **kwargs):       # функция заменяет собой инициализатор класса
#         old_init(self, *args, **kwargs)
#         self.attr = None                       # добавляем экземпляру класса атрибут attr
#
#     cls.__init__ = new_init                    # заменяем исходный инициализатор новым
#     return cls
#
# @add_attr_to_instances
# class MyClass:
#     pass
#
# obj = MyClass()
#
# print(obj.attr)


# принимает произвольное количество именованных аргументов и добавляет их экземплярам в качестве атрибута
# import functools
#
# def add_attr_to_instances(**attrs):                   # Принимаем именнованные аргументы
#     def decorator(cls):                               # принимает в качестве аргумента класс
#         old_init = cls.__init__                       # сохраняем исходный инициализатор
#
#         @functools.wraps(old_init)
#         def new_init(self, *args, **kwargs):          # функция заменяет собой инициализатор класса
#             old_init(self, *args, **kwargs)           # вызываем исходный инициализатор
#             self.__dict__.update(attrs)               # добавляем атрибуты экземпляру декорируемого класса
#
#         cls.__init__ = new_init                       # заменяем исходный инициализатор новым
#         return cls
#
#     return decorator
#
# @add_attr_to_instances(first_attr=1, second_attr=2)
# class MyClass:
#     pass
#
# obj = MyClass()
#
# print(obj.first_attr)   # 1
# print(obj.second_attr)  # 2


# считает количество созданных экземпляров декорируемого класса
# import functools
#
# def count_instances(cls):                        # принимает в качестве аргумента класс
#     old_init = cls.__init__                      # сохраняем исходный инициализатор
#     cls.count = 0                                # счетчик созданных экземпляров декорируемого класса
#
#     @functools.wraps(old_init)
#     def new_init(self, *args, **kwargs):         # функция заменяет собой инициализатор класса
#         old_init(self, *args, **kwargs)           # вызываем исходный инициализатор
#         cls.count += 1                           # увеличение счетчика на единицу
#
#     cls.__init__ = new_init                      # заменяем исходный инициализатор новым
#     return cls
#
#
# @count_instances
# class MyClass:
#     pass
#
#
# print(MyClass.count)
#
# for _ in range(10):
#     obj = MyClass()
#
# print(MyClass.count)
# выводит:
# 0
# 10

