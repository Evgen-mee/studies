#  Коллекция __slots__
# можно прописывать в любом классе
# УМЕНЬШАЕТ обьем памяти класса почти в 4 раза
# ускоряет работу с переменными __slots__

# позволяет прописать какие будут РАЗРЕШЕННЫЕ локальные свойства в экземляре класса
# добавить новый атрибут в экземпляр не получиться вылитет ошибка

# если в класс добавили __slots__
# то __dict__ в экземплярах нем не формируется

# class Point:
#     __slots__ = ("x", "y") # кроме этих атрибутов в экземпляре другие создать не получиться
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y



# Как работает __slots__ с property и при наследовании

# @property работает в  __slots__
# так как __slots__  накладывает ограничения только на экземпляр а не на класс

# если наследоваться от класса в котором используется __slots__
# то наследник не наследует __slots__ и мы можем создавать в нем любые 1 Атрибуты
# 1 Атрибуты родителя не попадут в __dict__ наследника они так же остануться __slots__

# что бы в наследнике ЗАПРЕТИТЬ создание атрибутов кроме родительских
# нужно в классе наследника прописать
# __slots__ = ()
# в таком случае наследник работает по колекции __slots__ родителя

# что бы добавить разрешенный атрибут кроме родительского __slots__
#  нужно в классе наследника прописать
# __slots__ = "нужные атрибут", и обязательно запятая!
# в таком случае наследник работает по колекции __slots__ родителя
# и атрибутам указаных в наследнике в __slots__ = "нужные атрибут",