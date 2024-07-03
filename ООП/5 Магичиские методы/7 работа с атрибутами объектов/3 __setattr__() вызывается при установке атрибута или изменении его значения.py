# установка атрибута или изменение его значения внутри метода __setattr__()
# происходит напрямую через словарь атрибутов __dict__

# Вместо обращения к словарю атрибутов __dict__, метод __setattr__()
# может использовать свою базовую реализацию из класса object.

# срабатывает каждый раз когда идет присвоение атрибуту

# class Cat:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#
#
#     def __setattr__(self, attr, value):     # обращаемся к словарю
#         attr = '_' + attr                   # делаем атрибут защищенным
#         self.__dict__[attr] = value         # изменяем атрибуты в dict
#
#
#     def __setattr__(self, attr, value):         # обращаемся к obj
#         attr = '_' + attr                       # делаем атрибут защищенным
#         object.__setattr__(self, attr, value)   # изменяем атрибуты в dict
#
#
# cat = Cat('Кемаль', 'Британский')
#
# print(cat.__dict__)  # {'_name': 'Кемаль', '_breed': 'Британский'}


# можем запретить создавать какой либо атрибут экземпляра класса
# def __setattr__(self, key, value):
#     if key == "z":  # запретили создавать атрибут с именем "z"
#         raise AttributeError("Недопустимое имя атрибута")
#     else:
#         object.__setattr__(self, key, value)


# РАБОТА С **kwargs
# class DefaultObject:
#
#     def __init__(self, default=None, **kwargs):
#         self.default = default
#         for k, v in kwargs.items():
#             object.__setattr__(self, k, v)
#

# class AttrsNumberObject:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#
#     def __getattribute__(self, item):
#         if item == 'attrs_num':
#             return len(self.__dict__) + 1
#         return object.__getattribute__(self, item)

# ЗАПРЕЩАЕМ УДАЛЯТЬ И ИЗМЕНЯТЬ АТРИБУТЫ
# class Const:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#
#     def __setattr__(self, key, value):
#         if key in self.__dict__:
#             raise AttributeError('Изменение значения атрибута невозможно')
#         object.__setattr__(self, key, value)
#
#     def __delattr__(self, item):
#         raise AttributeError('Удаление атрибута невозможно')


# Запрещаем удалять, записывать и т.п.
# class ProtectedObject:
#     def __init__(self, **kwargs):
#         for k, v in kwargs.items():
#             object.__setattr__(self, k, v)
#
#     def __setattr__(self, key, value):
#         print(len(dict))
#         if key[0] == '_':
#             raise AttributeError('Доступ к защищенному атрибуту невозможен')
#         object.__setattr__(self, key, value)
#
#     def __getattribute__(self, item):
#         if item[0] == '_':
#             raise AttributeError('Доступ к защищенному атрибуту невозможен')
#         return object.__getattribute__(self, item)
#
#     def __delattr__(self, item):
#         if item[0] == '_':
#             raise AttributeError('Доступ к защищенному атрибуту невозможен')
#         object.__delattr__(self, item)









