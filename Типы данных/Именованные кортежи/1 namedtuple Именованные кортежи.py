# Именованные кортежи (тип namedtuple) — это подтип обычных кортежей в Python.
# У них те же функции, что и у обычных, но их значения можно получать как с помощью индекса
# (например, [0]), так и с помощью имени через точку (например, .name).

# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])     # объявляем тип Point именованного кортежа
# point = Point(3, 7)                                             # создаем именованный кортеж Point
#
# print(point)                # Point(x=3, y=7)
# print(point.x, point.y)     # 3 7
# print(point[0], point[1])   # 3 7
# print(type(point))          # <class '__main__.Point'>