#  Наследование в объектно-ориентированном программировании
# Параметр self в родительском классе может ссылаться не только на себя но и на потомков
# методы и 1 Атрибуты в потомках можно переопределять

# наследуемся class Потомок(Родительский класс):

# добавление в потомка методов и атрибутов называется расширением базового класса

# super() возвращает ссылку на обьект посредник
# применение super() называется делегированием
#

# иницилизатор потомка и родителя
# если определен иницилизатор в родителе и определить иницилизатор в потомке
# то отработают оба иницилизатора и потомок будет иметь 1 Атрибуты двух иницилизаторов
# class Потомок
# def __init__(self,x1,y2,y1,x2, fill=None): иницилизатор потомка
# super().__init__(x1,y2,y1,x2) вызвали иницилизатор родителя и передали в него параметры
# ИНИЦИАЛИЗАТОР РОДИТЕЛЯ ВЫЗЫВАЕМ ПЕРВОЙ СТРОЧКОЙ!!!

#Синголтон и наследование
class Singleton:
    _instance = None
    _instance_base = None # дочерних может быть только 1 экземпляр

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls._instance_base is None:
                cls._instance_base = object.__new__(cls)
            return cls._instance_base

        if  cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

class Game(Singleton):
    def __init__(self, name):
        if "name" not in self.__dict__:
            self.name = name



# Функция issubclass(). Наследование от встроенных типов и от object
# object базовый класс всех классов
# при создании любых классов происходит наследование от object

# метод issubclass(насдедник, родитель) вернет True если классы наследовались
# работает только с классами НЕ С ЭКЗЕМПЛЯРАМИ

# метод isinstance(ЭКЗЕМПЛЯР насдедник, родитель)
# работает с классами и экземплярами

# так как все Типы данных классы то мы можем наследоваться от них
# и переопределять методы

class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))