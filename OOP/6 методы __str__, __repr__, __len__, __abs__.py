#Магические методы __str__, __repr__, __len__, __abs__

# метод __str__() для отображения информации об обьекте класса для пользователей

# метод __repr__() для отображения информации об обьекте класса для режима отладки

# метод __len__() позволяет применить функцию len() к экземплярам класса

# метод __abs__() позволяет применить функцию abs() к экземплярам класса


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"


class Point:
    def __init__(self, *args):
        self.__coords = args


    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))
