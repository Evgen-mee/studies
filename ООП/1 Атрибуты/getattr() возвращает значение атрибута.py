# принимает три аргумента:
# obj — объект
# name — имя атрибута
# default — значение по умолчанию

# метод getattr(Point,"a", False) позволяет при обращении к НЕСУЩЕСТВУЮЩЕМУ свойству избежать ошибки
# если метод класса не существует в данном классе то вернется третий аргумент метода getattr(Point,"a", False)
# False

# возвращает значение атрибута name объекта obj.
# Если объект obj не имеет атрибута name, возвращается значение по умолчанию default.
# Если значение по умолчанию не указано, возбуждается исключение AttributeError
#
# class Cat:
#     pass
#
# cat = Cat()
# cat.name = 'Кемаль'
# print(getattr(cat, 'name'))         # Кемаль
# print(getattr(cat, 'age', None))    # None


# можно получать значения атрибутов класса через экземпляры этого класса
# class Cat:
#     night_vision = True
#     paws_count = 4
#
# cat = Cat()
# print(getattr(cat, 'night_vision'))   # True
# print(getattr(cat, 'paws_count'))     # 4
