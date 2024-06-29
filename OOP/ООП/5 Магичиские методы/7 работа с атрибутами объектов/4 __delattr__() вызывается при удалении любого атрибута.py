# Метод __delattr__() вызывается при удалении атрибута.

# Вместо обращения к словарю атрибутов __dict__,
# метод __delattr__() может использовать свою базовую реализацию из класса object

# class Cat:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#
#     def __delattr__(self, attr):         # удаление через __dict__
#         print(f'Удаляю атрибут {attr}')
#         del self.__dict__[attr]
#
#     def __delattr__(self, attr):        # удаление через object
#         print(f'Удаляю атрибут {attr}')
#         object.__delattr__(self, attr)
#
#
#
# cat = Cat('Кемаль', 'Британский')
#
# del cat.name
# print(cat.__dict__) # Удаляю атрибут name # {'breed': 'Британский'}
#
# del cat.breed
# print(cat.__dict__) # Удаляю атрибут breed # {}